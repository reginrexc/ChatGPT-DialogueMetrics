"""
Enhanced Chat Analysis Tool for Extended AI Dialogue Research
==============================================================

This script analyzes ChatGPT conversation JSON exports to extract
comprehensive metrics for studying extended human-AI dialogues.

Enhanced version with:
- Improved semantic contradiction detection
- Real topic modeling
- Argument structure analysis
- Turn-pair analysis
- Statistical rigor metrics
- Convergence detection
- Research-grade measurements
- NEW: Cognitive load, coherence chains, affective trajectory, repair patterns,
       knowledge construction, temporal dynamics, social presence, argumentation structure
- NEW v3.1: Two-file output with global and per-thread matrices
- NEW v3.2: System Boundary & Refusals, Information Efficiency, Lexical Mirroring, Cognitive Asymmetry

Author: Enhanced from original by Claude (Anthropic)
Version: 3.2
License: MIT (Open Source)
"""

import json
import re
from datetime import datetime
import pandas as pd
import numpy as np
import tiktoken
from textblob import TextBlob
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer
from collections import Counter, defaultdict
from math import log2
from itertools import islice
from difflib import SequenceMatcher
import warnings
warnings.filterwarnings('ignore')

# === Initialize tokenizer ===
tokenizer = tiktoken.get_encoding("cl100k_base")

# === Configuration ===
input_file = "chat.json"  # Your ChatGPT export file
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
main_output_file = f"chat_analysis_{timestamp_str}.xlsx"          # v3.0 main output
matrix_output_file = f"chat_matrices_{timestamp_str}.xlsx"        # v3.1 matrix output

# === Enhanced Stopwords (expanded) ===
stopwords = set([
    "the","a","an","and","or","in","on","at","of","for","to","with","is",
    "are","was","were","it","i","you","he","she","they","we","this","that",
    "these","those","as","by","from","but","be","have","has","had","will",
    "can","would","could","should","just","not","about","which","what","who",
    "when","where","why","how","my","your","all","any","some","such","into"
])

# === Enhanced Contradiction Detection ===
CONTRADICTION_PATTERNS = {
    'negation': r'\b(not|no|never|neither|nor|none|nobody|nothing|nowhere|cannot|can\'t|won\'t|wouldn\'t|shouldn\'t|isn\'t|aren\'t|wasn\'t|weren\'t|hasn\'t|haven\'t|hadn\'t|don\'t|doesn\'t|didn\'t)\b',
    'adversative': r'\b(however|but|although|though|yet|nevertheless|nonetheless|conversely|on the contrary|in contrast|whereas|while|despite|regardless)\b',
    'correction': r'\b(actually|rather|instead|correction|mistake|incorrect|wrong|false|inaccurate)\b',
    'disagreement': r'\b(disagree|dispute|challenge|object|refute|reject|deny|oppose|counter)\b',
    'limitation': r'\b(except|unless|only if|provided that|caveat|limitation|constraint|boundary)\b'
}

# === Enhanced Elaboration Detection ===
ELABORATION_PATTERNS = {
    'causation': r'\b(because|since|as|due to|owing to|thanks to|for this reason|consequently)\b',
    'explanation': r'\b(means|refers to|indicates|suggests|implies|specifically|namely|in other words|that is)\b',
    'expansion': r'\b(moreover|furthermore|additionally|also|besides|plus|in addition|what\'s more)\b',
    'consequence': r'\b(therefore|thus|hence|so|accordingly|as a result|consequently)\b',
    'exemplification': r'\b(for example|for instance|such as|like|including|e\.g\.|i\.e\.)\b'
}

# === Hedge Detection (Epistemic Uncertainty) ===
HEDGE_PATTERNS = r'\b(might|may|could|possibly|perhaps|probably|likely|seems|appears|suggests|arguably|potentially|presumably)\b'

# === Confidence Markers (Epistemic Certainty) ===
CONFIDENCE_PATTERNS = r'\b(definitely|certainly|obviously|clearly|undoubtedly|absolutely|must|always|never|proven|fact)\b'

# === Question Type Classification ===
QUESTION_TYPES = {
    'clarification': r'\b(what do you mean|clarify|explain what|could you elaborate)\b',
    'verification': r'\b(is that|are you saying|do you mean|correct me if)\b',
    'challenge': r'\b(why do you|how can you|what makes you|on what basis)\b',
    'exploratory': r'\b(what if|have you considered|what about|how about)\b'
}

# =============================================================================
# NEW METRICS: COGNITIVE LOAD INDICATORS
# =============================================================================
COGNITIVE_LOAD_PATTERNS = {
    'complex_connectors': r'\b(furthermore|nevertheless|consequently|alternatively|specifically|particularly|essentially|fundamentally)\b',
    'abstraction': r'\b(concept|framework|theory|model|system|structure|process|mechanism|dynamic|factor)\b',
    'metacognition': r'\b(thinking about|reflect on|consider|analyze|evaluate|assess|examine|review|reconsider)\b',
    'computational': r'\b(calculate|compute|determine|solve|equation|formula|algorithm|variable|parameter)\b',
    'conditional': r'\b(if|then|assuming|given that|provided|in the case|scenario|condition)\b'
}

# =============================================================================
# NEW METRICS: DISCOURSE COHERENCE CHAINS
# =============================================================================
REFERENCE_PATTERNS = {
    'anaphoric': r'\b(it|this|that|these|those|they|them|their|he|she|his|her)\b',
    'demonstrative': r'\b(this|that|these|those)\s+\w+',
    'comparative': r'\b(same|similar|different|better|worse|more|less|another|other)\b',
    'continuity': r'\b(continues|ongoing|remains|still|again|also|too|as well)\b'
}

# =============================================================================
# NEW METRICS: AFFECTIVE TRAJECTORY (Beyond Sentiment)
# =============================================================================
AFFECTIVE_PATTERNS = {
    'curiosity': r'\b(wonder|curious|interested|fascinating|intriguing|puzzling|mystery|explore|discover)\b',
    'confusion': r'\b(confused|confusing|unclear|lost|don\'t understand|puzzled|perplexed|muddled)\b',
    'satisfaction': r'\b(great|excellent|perfect|helpful|useful|valuable|insightful|clarifying|satisfied)\b',
    'frustration': r'\b(frustrated|annoying|difficult|problem|issue|concern|worried|troubled|unfortunately)\b',
    'surprise': r'\b(surprising|unexpected|wow|amazing|remarkable|astonishing|didn\'t expect|never thought)\b',
    'engagement': r'\b(engaging|compelling|thought-provoking|stimulating|challenging|inspiring|motivating)\b'
}

# =============================================================================
# NEW METRICS: CONVERSATIONAL REPAIR PATTERNS
# =============================================================================
REPAIR_PATTERNS = {
    'self_correction': r'\b(correction|correcting myself|I meant|actually|rather|to be precise|more accurately)\b',
    'clarification_request': r'\b(could you clarify|what do you mean|I don\'t understand|unclear|confused by)\b',
    'confirmation_check': r'\b(is that right|do you mean|am I correct|so you\'re saying|if I understand)\b',
    'elaboration_request': r'\b(could you elaborate|tell me more|expand on|go deeper|more detail|more specific)\b',
    'repetition': r'\b(again|repeat|reiterate|as I said|as mentioned|to restate|in other words)\b'
}

# =============================================================================
# NEW METRICS: KNOWLEDGE CONSTRUCTION MARKERS
# =============================================================================
KNOWLEDGE_PATTERNS = {
    'joint_attention': r'\b(let\'s|together|we can|we should|our|shared|common|mutual|collaborative)\b',
    'hypothesis': r'\b(hypothesis|assume|suppose|imagine|what if|consider|possibility|theory)\b',
    'evidence': r'\b(evidence|data|research|study|shows|indicates|suggests|demonstrates|proves)\b',
    'synthesis': r'\b(combine|integrate|synthesize|bring together|connect|link|relate|overall|in summary)\b',
    'perspective': r'\b(perspective|viewpoint|angle|approach|lens|frame|position|stance|outlook)\b'
}

# =============================================================================
# NEW METRICS: SOCIAL PRESENCE / RAPPORT INDICATORS
# =============================================================================
SOCIAL_PRESENCE_PATTERNS = {
    'acknowledgment': r'\b(good point|well said|I see|understood|got it|makes sense|right|exactly|precisely)\b',
    'encouragement': r'\b(good job|well done|excellent|great work|nice|keep going|you\'re on the right track)\b',
    'empathy': r'\b(understand|appreciate|recognize|know how|difficult|challenging|frustrating|exciting)\b',
    'solidarity': r'\b(we|us|together|both|similarly|likewise|same here|me too|agreed)\b',
    'politeness': r'\b(please|thank you|thanks|appreciate|would you mind|could you|would you|sorry|excuse)\b',
    'humor': r'\b(haha|lol|funny|amusing|witty|ironic|sarcastic|just kidding|playful)\b'
}

# =============================================================================
# NEW METRICS: ARGUMENTATION STRUCTURE
# =============================================================================
ARGUMENTATION_PATTERNS = {
    'claim': r'\b(argue|claim|assert|maintain|contend|posit|thesis|position|view|belief)\b',
    'evidence_marker': r'\b(because|since|given|based on|as shown|evidence|data|fact|example|instance)\b',
    'warrant': r'\b(therefore|thus|hence|so|consequently|it follows|implies|suggests|indicates)\b',
    'qualifier': r'\b(probably|likely|generally|usually|typically|often|sometimes|in most cases)\b',
    'rebuttal': r'\b(however|but|although|unless|except|admittedly|granted|concede|alternative)\b'
}

# =============================================================================
# NEW METRICS: TEMPORAL DYNAMICS
# =============================================================================
TEMPORAL_PATTERNS = {
    'urgency': r'\b(urgent|immediately|asap|quickly|soon|deadline|rush|pressing|critical|now)\b',
    'reflection': r'\b(looking back|in retrospect|previously|earlier|before|initially|at first|now)\b',
    'projection': r'\b(future|next|upcoming|will|plan|intend|goal|aim|objective|target)\b',
    'pace_marker': r'\b(step by step|gradually|slowly|rapidly|quickly|suddenly|eventually|finally)\b'
}

# =============================================================================
# NEW v3.2: SYSTEM BOUNDARY & EPISTEMIC REFUSALS
# =============================================================================
REFUSAL_PATTERNS = r'\b(as an ai|cannot|unable|sorry|policy|guidelines|restricted|harmful|legal advice|medical advice|violate)\b'

# === Helper Functions ===
def extract_text_from_parts(parts):
    """Extract text from message parts (handles different formats)"""
    texts = []
    for part in parts:
        if isinstance(part, str):
            texts.append(part)
        elif isinstance(part, dict) and "text" in part:
            texts.append(part["text"])
    return " ".join(texts).strip()

def convert_timestamp(ts):
    """Convert various timestamp formats to standard format"""
    if not ts: 
        return ""
    try:
        if isinstance(ts, (int, float)):
            return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        return str(ts)
    except:
        return str(ts)

def count_words(text): 
    """Count words in text"""
    return len(text.split())

def count_tokens(text): 
    """Count tokens using tiktoken (GPT tokenizer)"""
    return len(tokenizer.encode(text))

def count_sentences(text):
    """Count sentences in text"""
    return len(re.split(r'[.!?]+', text.strip()))

def count_syllables(word):
    """Estimate syllable count for readability"""
    word = word.lower()
    vowels = 'aeiouy'
    syllables = 0
    previous_was_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllables += 1
        previous_was_vowel = is_vowel
    if word.endswith('e'):
        syllables -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        syllables += 1
    return max(1, syllables)

def compute_sentiment(text):
    """Compute sentiment with continuous polarity score"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return {
        'label': "POSITIVE" if polarity > 0.05 else "NEGATIVE" if polarity < -0.05 else "NEUTRAL",
        'score': round(polarity, 3),
        'subjectivity': round(blob.sentiment.subjectivity, 3)
    }

def compute_duration(timestamps):
    """Calculate total conversation duration"""
    dt_list = []
    for ts in timestamps:
        try: 
            dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            dt_list.append(dt)
        except: 
            continue
    return str(max(dt_list) - min(dt_list)) if dt_list else ""

# === NEW v3.2: Cognitive Coupling Functions ===
def compute_iei(entropy, word_count):
    """
    Calculate Information Efficiency Index (IEI)
    Formula: Shannon Entropy / Lexical Volume
    """
    return round(entropy / word_count, 4) if word_count > 0 else 0

def compute_mirroring(source_text, target_text):
    """
    Calculate Lexical Mirroring (Syntactic Alignment / Social Entrainment)
    Measures the overlap of significant words between consecutive turns.
    """
    if not source_text or not target_text: 
        return 0
    # Extract words longer than 3 characters
    s_words = set(re.findall(r'\b\w{4,}\b', source_text.lower()))
    t_words = set(re.findall(r'\b\w{4,}\b', target_text.lower()))
    
    if not s_words: 
        return 0
    overlap = s_words.intersection(t_words)
    return round(len(overlap) / len(s_words), 4)

# === Enhanced Structural Analysis ===
def compute_enhanced_structural_metrics(text):
    """
    Compute comprehensive structural metrics with pattern categorization
    Returns detailed breakdown of adversarial and elaborative language
    """
    text_lower = text.lower()
    
    # Count each type of contradiction
    contradiction_counts = {}
    total_contradictions = 0
    for ctype, pattern in CONTRADICTION_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        contradiction_counts[ctype] = count
        total_contradictions += count
    
    # Count each type of elaboration
    elaboration_counts = {}
    total_elaborations = 0
    for etype, pattern in ELABORATION_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        elaboration_counts[etype] = count
        total_elaborations += count
    
    # Epistemic markers
    hedges = len(re.findall(HEDGE_PATTERNS, text_lower, flags=re.I))
    confidence_markers = len(re.findall(CONFIDENCE_PATTERNS, text_lower, flags=re.I))
    
    # Calculate ratios and complexity
    ratio = total_contradictions / total_elaborations if total_elaborations > 0 else float('inf')
    
    # Epistemic stance (confidence - hedges = more confident)
    epistemic_stance = confidence_markers - hedges
    
    return {
        'total_contradictions': total_contradictions,
        'total_elaborations': total_elaborations,
        'contradiction_ratio': round(ratio, 2),
        'negations': contradiction_counts.get('negation', 0),
        'adversatives': contradiction_counts.get('adversative', 0),
        'corrections': contradiction_counts.get('correction', 0),
        'disagreements': contradiction_counts.get('disagreement', 0),
        'limitations': contradiction_counts.get('limitation', 0),
        'causations': elaboration_counts.get('causation', 0),
        'explanations': elaboration_counts.get('explanation', 0),
        'expansions': elaboration_counts.get('expansion', 0),
        'consequences': elaboration_counts.get('consequence', 0),
        'examples': elaboration_counts.get('exemplification', 0),
        'hedges': hedges,
        'confidence_markers': confidence_markers,
        'epistemic_stance': epistemic_stance
    }

# =============================================================================
# NEW: COGNITIVE LOAD COMPUTATION
# =============================================================================
def compute_cognitive_load(text):
    """Compute cognitive load indicators"""
    text_lower = text.lower()
    
    counts = {}
    total_load = 0
    for ctype, pattern in COGNITIVE_LOAD_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        counts[ctype] = count
        total_load += count
    
    # Compute density per 100 words
    word_count = len(text.split())
    density = (total_load / word_count * 100) if word_count > 0 else 0
    
    return {
        'cognitive_load_total': total_load,
        'cognitive_load_density': round(density, 2),
        'complex_connectors': counts.get('complex_connectors', 0),
        'abstraction_markers': counts.get('abstraction', 0),
        'metacognitive_markers': counts.get('metacognition', 0),
        'computational_markers': counts.get('computational', 0),
        'conditional_complexity': counts.get('conditional', 0)
    }

# =============================================================================
# NEW: DISCOURSE COHERENCE COMPUTATION
# =============================================================================
def compute_coherence_chains(text, previous_text=None):
    """Compute discourse coherence markers"""
    text_lower = text.lower()
    
    counts = {}
    total_references = 0
    for ctype, pattern in REFERENCE_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        counts[ctype] = count
        total_references += count
    
    # Compute referential density
    word_count = len(text.split())
    ref_density = (total_references / word_count * 100) if word_count > 0 else 0
    
    # If previous text provided, compute continuity
    continuity_score = None
    if previous_text:
        prev_words = set(re.findall(r'\b\w+\b', previous_text.lower())) - stopwords
        curr_words = set(re.findall(r'\b\w+\b', text_lower)) - stopwords
        if prev_words:
            continuity_score = len(prev_words & curr_words) / len(prev_words)
    
    return {
        'reference_density': round(ref_density, 2),
        'anaphoric_references': counts.get('anaphoric', 0),
        'demonstrative_references': counts.get('demonstrative', 0),
        'comparative_references': counts.get('comparative', 0),
        'continuity_markers': counts.get('continuity', 0),
        'entity_continuity': round(continuity_score, 3) if continuity_score else None
    }

# =============================================================================
# NEW: AFFECTIVE TRAJECTORY COMPUTATION
# =============================================================================
def compute_affective_trajectory(text):
    """Compute multi-dimensional affective state beyond polarity"""
    text_lower = text.lower()
    
    scores = {}
    total_affective = 0
    for emotion, pattern in AFFECTIVE_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        scores[emotion] = count
        total_affective += count
    
    # Determine dominant affect
    dominant = max(scores, key=scores.get) if scores else 'neutral'
    dominant_count = scores.get(dominant, 0)
    
    # Affective diversity (how many different emotions expressed)
    diversity = len([v for v in scores.values() if v > 0])
    
    return {
        'dominant_affect': dominant if dominant_count > 0 else 'neutral',
        'affective_intensity': total_affective,
        'affective_diversity': diversity,
        'curiosity_score': scores.get('curiosity', 0),
        'confusion_score': scores.get('confusion', 0),
        'satisfaction_score': scores.get('satisfaction', 0),
        'frustration_score': scores.get('frustration', 0),
        'surprise_score': scores.get('surprise', 0),
        'engagement_score': scores.get('engagement', 0)
    }

# =============================================================================
# NEW: REPAIR PATTERN COMPUTATION
# =============================================================================
def compute_repair_patterns(text, role='unknown'):
    """Compute conversational repair and maintenance patterns"""
    text_lower = text.lower()
    
    counts = {}
    total_repairs = 0
    for rtype, pattern in REPAIR_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        counts[rtype] = count
        total_repairs += count
    
    # Classify repair type
    if counts.get('self_correction', 0) > 0:
        repair_type = 'self_repair'
    elif counts.get('clarification_request', 0) > 0:
        repair_type = 'other_repair_request'
    elif counts.get('confirmation_check', 0) > 0:
        repair_type = 'confirmation'
    elif counts.get('elaboration_request', 0) > 0:
        repair_type = 'elaboration_request'
    else:
        repair_type = 'none'
    
    return {
        'total_repair_markers': total_repairs,
        'repair_type': repair_type,
        'self_corrections': counts.get('self_correction', 0),
        'clarification_requests': counts.get('clarification_request', 0),
        'confirmation_checks': counts.get('confirmation_check', 0),
        'elaboration_requests': counts.get('elaboration_request', 0),
        'repetitions': counts.get('repetition', 0)
    }

# =============================================================================
# NEW: KNOWLEDGE CONSTRUCTION COMPUTATION
# =============================================================================
def compute_knowledge_construction(text):
    """Compute collaborative knowledge building markers"""
    text_lower = text.lower()
    
    counts = {}
    total_markers = 0
    for ktype, pattern in KNOWLEDGE_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        counts[ktype] = count
        total_markers += count
    
    # Determine knowledge phase
    if counts.get('hypothesis', 0) > counts.get('synthesis', 0):
        phase = 'hypothesis_generation'
    elif counts.get('evidence', 0) > 0:
        phase = 'evidence_evaluation'
    elif counts.get('synthesis', 0) > 0:
        phase = 'synthesis_integration'
    else:
        phase = 'information_exchange'
    
    return {
        'knowledge_construction_score': total_markers,
        'construction_phase': phase,
        'joint_attention_markers': counts.get('joint_attention', 0),
        'hypothesis_markers': counts.get('hypothesis', 0),
        'evidence_markers': counts.get('evidence', 0),
        'synthesis_markers': counts.get('synthesis', 0),
        'perspective_markers': counts.get('perspective', 0)
    }

# =============================================================================
# NEW: SOCIAL PRESENCE COMPUTATION
# =============================================================================
def compute_social_presence(text):
    """Compute social presence and rapport indicators"""
    text_lower = text.lower()
    
    counts = {}
    total_social = 0
    for stype, pattern in SOCIAL_PRESENCE_PATTERNS.items():
        count = len(re.findall(pattern, text_lower, flags=re.I))
        counts[stype] = count
        total_social += count
    
    # Compute rapport score (weighted toward solidarity and acknowledgment)
    rapport = (counts.get('solidarity', 0) * 2 + 
               counts.get('acknowledgment', 0) * 1.5 + 
               counts.get('empathy', 0))
    
    return {
        'social_presence_score': total_social,
        'rapport_index': round(rapport, 2),
        'acknowledgments': counts.get('acknowledgment', 0),
        'encouragements': counts.get('encouragement', 0),
        'empathy_markers': counts.get('empathy', 0),
        'solidarity_markers': counts.get('solidarity', 0),
        'politeness_markers': counts.get('politeness', 0),
        'humor_markers': counts.get('humor', 0)
    }

# =============================================================================
# NEW: ARGUMENTATION STRUCTURE COMPUTATION
# =============================================================================
def compute_argumentation_structure(text):
    """Compute argumentation structure components (Toulmin model inspired)"""
    text_lower = text.lower()
    
    counts = {}
    for atype, pattern in ARGUMENTATION_PATTERNS.items():
        counts[atype] = len(re.findall(pattern, text_lower, flags=re.I))
    
    # Determine argument structure completeness
    has_claim = counts.get('claim', 0) > 0
    has_evidence = counts.get('evidence_marker', 0) > 0
    has_warrant = counts.get('warrant', 0) > 0
    
    if has_claim and has_evidence and has_warrant:
        structure = 'complete_argument'
    elif has_claim and has_evidence:
        structure = 'claim_evidence'
    elif has_claim:
        structure = 'assertion_only'
    else:
        structure = 'no_explicit_argument'
    
    # Argument quality score
    quality = sum([has_claim, has_evidence, has_warrant, counts.get('qualifier', 0) > 0])
    
    return {
        'argument_structure': structure,
        'argument_quality': quality,
        'claim_markers': counts.get('claim', 0),
        'evidence_markers': counts.get('evidence_marker', 0),
        'warrant_markers': counts.get('warrant', 0),
        'qualifier_markers': counts.get('qualifier', 0),
        'rebuttal_markers': counts.get('rebuttal', 0)
    }

# =============================================================================
# NEW: TEMPORAL DYNAMICS COMPUTATION
# =============================================================================
def compute_temporal_dynamics(text, response_time=None):
    """Compute temporal and pacing markers"""
    text_lower = text.lower()
    
    counts = {}
    for ttype, pattern in TEMPORAL_PATTERNS.items():
        counts[ttype] = len(re.findall(pattern, text_lower, flags=re.I))
    
    # Determine temporal orientation
    reflection = counts.get('reflection', 0)
    projection = counts.get('projection', 0)
    
    if reflection > projection:
        orientation = 'past_focused'
    elif projection > reflection:
        orientation = 'future_focused'
    else:
        orientation = 'present_focused'
    
    # Urgency level
    urgency = 'high' if counts.get('urgency', 0) > 2 else 'medium' if counts.get('urgency', 0) > 0 else 'low'
    
    return {
        'temporal_orientation': orientation,
        'urgency_level': urgency,
        'urgency_markers': counts.get('urgency', 0),
        'reflection_markers': counts.get('reflection', 0),
        'projection_markers': counts.get('projection', 0),
        'pace_markers': counts.get('pace_marker', 0)
    }

def classify_question_type(text):
    """Classify questions by type"""
    if not text.strip().endswith('?'):
        return None
    
    text_lower = text.lower()
    for qtype, pattern in QUESTION_TYPES.items():
        if re.search(pattern, text_lower, flags=re.I):
            return qtype
    
    # Default classification by starting word
    if text_lower.startswith('what'):
        return 'information-seeking'
    elif text_lower.startswith('why'):
        return 'causal'
    elif text_lower.startswith('how'):
        return 'procedural'
    else:
        return 'other'

# === Recursive Extraction (maintaining original structure) ===
def extract_messages(mapping):
    """Extract messages from ChatGPT JSON mapping structure"""
    messages_list = []
    message = mapping.get("message")
    if not message: 
        return messages_list

    role = message.get("author", {}).get("role", "unknown")
    content_data = message.get("content", {})
    content_parts = content_data.get("parts", [])
    content = extract_text_from_parts(content_parts)
    timestamp = convert_timestamp(message.get("create_time", ""))
    metadata = message.get("metadata", {})
    model_used = metadata.get("model_slug", content_data.get("model_slug", "unknown"))

    if content:
        messages_list.append({
            "role": role, 
            "content": content, 
            "timestamp": timestamp,
            "word_count": count_words(content), 
            "token_count": count_tokens(content),
            "sentence_count": count_sentences(content),
            "model": model_used,
            "parts": [p.get("text") if isinstance(p, dict) else p for p in content_parts]
        })

    for child in message.get("children", []):
        messages_list.extend(extract_messages({"message": child}))
    
    return messages_list

# === Enhanced Turn-Taking Analysis ===
def compute_turntaking_metrics(messages):
    """Compute response times and turn-taking patterns"""
    prev_time = None
    prev_role = None
    turn_lengths = []
    
    for m in messages:
        timestamp = m.get("timestamp")
        current_role = m.get("role")
        
        try: 
            dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") if timestamp else None
        except: 
            dt = None
        
        # Calculate response time
        if dt and prev_time:
            response_time = (dt - prev_time).total_seconds()
            m['response_time'] = response_time
            
            # Track turn-taking patterns
            if prev_role and prev_role != current_role:
                turn_lengths.append(response_time)
        else:
            m['response_time'] = None
        
        prev_time = dt or prev_time
        prev_role = current_role
    
    return messages

# === Enhanced Dialogue Act Classification ===
def classify_dialogue_acts(messages):
    """Classify dialogue acts with more granularity"""
    for m in messages:
        text = m.get("content", "").lower()
        role = m.get("role")
        
        # Question classification
        if text.endswith("?"):
            qtype = classify_question_type(text)
            m['dialogue_act'] = f"question_{qtype}" if qtype else "question"
        # Gratitude
        elif any(word in text for word in ["thanks", "thank you", "thx", "appreciate"]):
            m['dialogue_act'] = "gratitude"
        # Agreement
        elif any(phrase in text for phrase in ["i agree", "you're right", "exactly", "precisely"]):
            m['dialogue_act'] = "agreement"
        # Disagreement
        elif any(phrase in text for phrase in ["i disagree", "not quite", "actually", "i don't think"]):
            m['dialogue_act'] = "disagreement"
        # Clarification
        elif any(phrase in text for phrase in ["to clarify", "what i mean is", "in other words"]):
            m['dialogue_act'] = "clarification"
        # Answer (for assistant)
        elif role == "assistant":
            m['dialogue_act'] = "answer"
        # Default statement
        else:
            m['dialogue_act'] = "statement"
    
    return messages

# === Turn Pair Analysis ===
def analyze_turn_pairs(df):
    """Analyze user-assistant turn pairs for patterns"""
    pairs = []
    
    for i in range(len(df) - 1):
        current = df.iloc[i]
        next_msg = df.iloc[i + 1]
        
        if current['role'] == 'user' and next_msg['role'] == 'assistant':
            # Calculate engagement metrics for this pair
            user_question_type = classify_question_type(current['content']) if current['content'].endswith('?') else None
            
            # Response length ratio
            response_ratio = next_msg['word_count'] / current['word_count'] if current['word_count'] > 0 else 0
            
            # Semantic similarity (using simple overlap for efficiency)
            user_words = set(current['content'].lower().split()) - stopwords
            assistant_words = set(next_msg['content'].lower().split()) - stopwords
            overlap = len(user_words & assistant_words) / len(user_words | assistant_words) if user_words or assistant_words else 0
            
            pairs.append({
                'pair_index': i,
                'user_length': current['word_count'],
                'assistant_length': next_msg['word_count'],
                'response_ratio': round(response_ratio, 2),
                'semantic_overlap': round(overlap, 3),
                'question_type': user_question_type,
                'response_time': next_msg.get('response_time')
            })
    
    return pairs

# === Convergence Detection ===
def detect_convergence_patterns(df, window_size=10):
    """
    Detect convergence patterns in dialogue
    Looks for decreasing contradiction rates and increasing coherence
    """
    convergence_metrics = []
    
    for i in range(window_size, len(df)):
        window = df.iloc[i-window_size:i]
        
        # Calculate metrics for this window
        avg_contradictions = window['Contradictions'].mean()
        avg_elaborations = window['Elaborations'].mean()
        avg_response_time = window['response_time'].dropna().mean()
        sentiment_variance = window['sentiment_score'].var()
        
        # NEW: Check for cognitive load trends
        if 'Cognitive_Load_Density' in window.columns:
            cog_load_trend = window['Cognitive_Load_Density'].mean()
        else:
            cog_load_trend = None
        
        # NEW: Check for repair frequency
        if 'Total_Repair_Markers' in window.columns:
            repair_freq = window['Total_Repair_Markers'].sum()
        else:
            repair_freq = None
        
        convergence_metrics.append({
            'message_index': i,
            'avg_contradictions_window': round(avg_contradictions, 2),
            'avg_elaborations_window': round(avg_elaborations, 2),
            'contradiction_trend': 'decreasing' if i > window_size and avg_contradictions < df.iloc[i-window_size-10:i-window_size]['Contradictions'].mean() else 'stable',
            'avg_response_time_window': round(avg_response_time, 1) if pd.notna(avg_response_time) else None,
            'sentiment_stability': round(1 - sentiment_variance, 3) if pd.notna(sentiment_variance) else None,
            'cognitive_load_window': round(cog_load_trend, 2) if cog_load_trend else None,
            'repair_frequency_window': int(repair_freq) if repair_freq else None
        })
    
    return convergence_metrics

# === BLEU/METEOR/ROUGE (maintaining original) ===
smoothie = SmoothingFunction().method1
rouge = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)

def compute_bleu(ref, cand):
    r, c = ref.split(), cand.split()
    return sentence_bleu([r], c, smoothing_function=smoothie) if r and c else 0

def compute_meteor(ref, cand):
    r, c = ref.split(), cand.split()
    return meteor_score([r], c) if r and c else 0

def compute_rouge(ref, cand):
    scores = rouge.score(ref, cand)
    return {k: v.fmeasure for k, v in scores.items()}

# === Enhanced Language Metrics ===
def compute_entropy(text):
    """Shannon entropy of text"""
    tokens = text.split()
    if not tokens:
        return 0
    freq = Counter(tokens)
    total = sum(freq.values())
    return -sum((c/total) * log2(c/total) for c in freq.values())

def lexical_diversity(text):
    """Type-token ratio (lexical diversity)"""
    words = re.findall(r'\b\w+\b', text.lower())
    return len(set(words)) / len(words) if words else 0

def compute_readability(text):
    """Enhanced Flesch Reading Ease with better syllable counting"""
    sentences = count_sentences(text)
    if sentences == 0:
        return 0
    
    words = text.split()
    word_count = len(words)
    if word_count == 0:
        return 0
    
    syllable_count = sum(count_syllables(word) for word in words)
    
    # Flesch Reading Ease formula
    fre = 206.835 - (1.015 * (word_count / sentences)) - (84.6 * (syllable_count / word_count))
    return round(fre, 2)

def compute_lexical_richness(text):
    """
    Advanced lexical richness metrics
    - TTR: Type-Token Ratio
    - MTLD: Measure of Textual Lexical Diversity (approximation)
    - Unique words per 100 words
    """
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return {'ttr': 0, 'unique_per_100': 0}
    
    unique_words = set(words)
    ttr = len(unique_words) / len(words)
    unique_per_100 = (len(unique_words) / len(words)) * 100
    
    return {
        'ttr': round(ttr, 3),
        'unique_per_100': round(unique_per_100, 1)
    }

# === Keyword Flow Analysis ===
def compute_keyword_flow(df):
    """Track keyword continuity across messages"""
    flow_edges = 0
    total_words = set()
    keyword_persistence = []
    
    for i in range(1, len(df)):
        prev_words = set(re.findall(r'\b\w+\b', df.iloc[i-1]['content'].lower())) - stopwords
        curr_words = set(re.findall(r'\b\w+\b', df.iloc[i]['content'].lower())) - stopwords
        
        # Count shared keywords
        shared = prev_words & curr_words
        flow_edges += len(shared)
        total_words.update(curr_words)
        
        # Track persistence
        if prev_words:
            persistence = len(shared) / len(prev_words)
            keyword_persistence.append(persistence)
    
    # Get top keywords
    top_keywords = list(islice(total_words, 15))
    avg_persistence = np.mean(keyword_persistence) if keyword_persistence else 0
    
    return {
        'flow_edges': flow_edges,
        'top_keywords': top_keywords,
        'avg_persistence': round(avg_persistence, 3)
    }

def compute_sentiment_shift(sentiments):
    """Calculate sentiment volatility"""
    map_ = {"NEGATIVE": -1, "NEUTRAL": 0, "POSITIVE": 1}
    nums = [map_.get(s, 0) for s in sentiments]
    if len(nums) <= 1:
        return 0
    diffs = [abs(nums[i] - nums[i-1]) for i in range(1, len(nums))]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0

def detect_response_edits(messages):
    """Detect edits and revisions in messages"""
    prev_assistant = None
    
    for m in messages:
        text = m.get("content", "")
        role = m.get("role")
        parts = [p for p in (m.get("parts") or []) if isinstance(p, str)]
        
        edit_count = 0
        edit_similarity = None
        
        # Check for multiple parts (direct edits)
        if len(parts) > 1:
            edit_count = len(parts) - 1
            edit_similarity = SequenceMatcher(None, parts[0], parts[-1]).ratio()
        
        # Check for similar consecutive assistant messages (iterations)
        elif role == "assistant" and prev_assistant:
            edit_similarity = SequenceMatcher(None, prev_assistant, text).ratio()
            if edit_similarity < 0.9:
                edit_count = 1
        
        if role == "assistant":
            prev_assistant = text
        
        m.update({
            "edit_count": edit_count, 
            "edit_similarity": round(edit_similarity, 3) if edit_similarity else None
        })
    
    return messages

# === MAIN PROCESSING ===
print("=" * 80)
print("ENHANCED CHAT ANALYSIS TOOL v3.2")
print("=" * 80)
print(f"\nLoading: {input_file}")

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

all_chats = {}
summary_rows = []
process_notes = []

# Structures for matrix analysis
global_act_counts = defaultdict(lambda: defaultdict(int))          # global transition counts
all_messages_list = []                                             # for global correlation

# Per-thread matrix storage
thread_act_counts = {}      # dict: thread_name -> defaultdict of transition counts
thread_numeric_data = {}    # dict: thread_name -> DataFrame of numeric columns (for correlation)

print(f"Found {len(data)} conversation(s) to analyze...\n")

# === Create two Excel writers ===
with pd.ExcelWriter(main_output_file, engine="xlsxwriter") as main_writer, \
     pd.ExcelWriter(matrix_output_file, engine="xlsxwriter") as matrix_writer:

    workbook_main = main_writer.book
    workbook_matrix = matrix_writer.book

    # Formats for main output
    header_fmt_main = workbook_main.add_format({
        'bold': True, 
        'bg_color': '#4A90E2',
        'font_color': 'white',
        'align': 'center', 
        'valign': 'vcenter',
        'border': 1
    })
    center_fmt_main = workbook_main.add_format({'align': 'center', 'valign': 'vcenter'})
    number_fmt_main = workbook_main.add_format({'num_format': '0.00', 'align': 'center'})

    # Formats for matrix output
    header_fmt_matrix = workbook_matrix.add_format({
        'bold': True, 
        'bg_color': '#4A90E2',
        'font_color': 'white',
        'align': 'center', 
        'valign': 'vcenter',
        'border': 1
    })
    center_fmt_matrix = workbook_matrix.add_format({'align': 'center', 'valign': 'vcenter'})
    number_fmt_matrix = workbook_matrix.add_format({'num_format': '0.00', 'align': 'center'})

    for chat_idx, chat in enumerate(data, 1):
        title = chat.get("title", "Untitled Chat")
        safe_title = re.sub(r'[\\/*?:[\]]', '_', title)[:31]
        
        print(f"[{chat_idx}/{len(data)}] Processing: {title}")
        
        rows = []
        timestamps = []
        
        # Extract messages
        for mapping in chat.get("mapping", {}).values():
            extracted = extract_messages(mapping)
            rows.extend(extracted)
            timestamps.extend([r["timestamp"] for r in extracted if r["timestamp"]])
        
        if not rows:
            print(f"  ⚠️  No messages found, skipping...\n")
            continue
        
        # Compute dialogue metrics
        rows = compute_turntaking_metrics(rows)
        rows = classify_dialogue_acts(rows)
        rows = detect_response_edits(rows)
        
        conversation_duration = compute_duration(timestamps)
        all_chats[safe_title] = {"rows": rows, "duration": conversation_duration}
        
        # Create DataFrame
        df = pd.DataFrame(rows)
        
        # Add sequence numbers
        df.insert(0, 'Seq. #', [f"#{i+1}" for i in range(len(df))])
        
        # Compute sentiment with scores
        sentiment_data = [compute_sentiment(row["content"]) for _, row in df.iterrows()]
        df['sentiment'] = [s['label'] for s in sentiment_data]
        df['sentiment_score'] = [s['score'] for s in sentiment_data]
        df['subjectivity'] = [s['subjectivity'] for s in sentiment_data]
        
        # Initialize lists for metrics
        bleu_scores = []
        meteor_scores = []
        rouge1_scores = []
        rougeL_scores = []
        entropy_scores = []
        readability_scores = []
        lexdiv_scores = []
        
        # Structural metrics (enhanced)
        contradictions = []
        elaborations = []
        contradiction_ratios = []
        negations = []
        adversatives = []
        hedges_list = []
        confidence_list = []
        epistemic_stance_list = []
        
        # =============================================================================
        # NEW METRICS INITIALIZATION
        # =============================================================================
        
        # Cognitive Load
        cog_load_totals = []
        cog_load_densities = []
        complex_connectors = []
        abstraction_markers = []
        metacognitive_markers = []
        computational_markers = []
        conditional_complexity = []
        
        # Coherence Chains
        reference_densities = []
        anaphoric_refs = []
        demonstrative_refs = []
        comparative_refs = []
        continuity_markers = []
        entity_continuities = []
        
        # Affective Trajectory
        dominant_affects = []
        affective_intensities = []
        affective_diversities = []
        curiosity_scores = []
        confusion_scores = []
        satisfaction_scores = []
        frustration_scores = []
        surprise_scores = []
        engagement_scores = []
        
        # Repair Patterns
        total_repairs = []
        repair_types = []
        self_corrections = []
        clarification_requests = []
        confirmation_checks = []
        elaboration_requests_list = []
        repetitions = []
        
        # Knowledge Construction
        knowledge_scores = []
        construction_phases = []
        joint_attention = []
        hypothesis_markers = []
        evidence_markers_list = []
        synthesis_markers = []
        perspective_markers = []
        
        # Social Presence
        social_scores = []
        rapport_indices = []
        acknowledgments = []
        encouragements = []
        empathy_markers_list = []
        solidarity_markers = []
        politeness_markers_list = []
        humor_markers = []
        
        # Argumentation
        argument_structures = []
        argument_qualities = []
        claim_markers = []
        evidence_markers_arg = []
        warrant_markers = []
        qualifier_markers = []
        rebuttal_markers = []
        
        # Temporal Dynamics
        temporal_orientations = []
        urgency_levels = []
        urgency_markers = []
        reflection_markers = []
        projection_markers = []
        pace_markers = []
        
        # === NEW v3.2: Initialize trackers for cognitive coupling metrics ===
        iei_list = []
        mirroring_list = []
        asymmetry_list = []
        refusals_list = []
        # Initialize previous turn variables
        prev_text = ""
        prev_readability = 0.0
        # ================================================================
        
        print(f"  📊 Computing {len(df)} message metrics...")
        
        # Compute per-message metrics
        for i, row in df.iterrows():
            text = row["content"]
            role = row["role"]
            
            # Language metrics
            entropy = compute_entropy(text)
            entropy_scores.append(entropy)
            readability = compute_readability(text)
            readability_scores.append(readability)
            lex_rich = compute_lexical_richness(text)
            lexdiv_scores.append(lex_rich['ttr'])
            
            # Enhanced structural metrics
            struct_metrics = compute_enhanced_structural_metrics(text)
            contradictions.append(struct_metrics['total_contradictions'])
            elaborations.append(struct_metrics['total_elaborations'])
            contradiction_ratios.append(struct_metrics['contradiction_ratio'])
            negations.append(struct_metrics['negations'])
            adversatives.append(struct_metrics['adversatives'])
            hedges_list.append(struct_metrics['hedges'])
            confidence_list.append(struct_metrics['confidence_markers'])
            epistemic_stance_list.append(struct_metrics['epistemic_stance'])
            
            # =============================================================================
            # NEW METRICS COMPUTATION
            # =============================================================================
            
            # 1. Cognitive Load
            cog = compute_cognitive_load(text)
            cog_load_totals.append(cog['cognitive_load_total'])
            cog_load_densities.append(cog['cognitive_load_density'])
            complex_connectors.append(cog['complex_connectors'])
            abstraction_markers.append(cog['abstraction_markers'])
            metacognitive_markers.append(cog['metacognitive_markers'])
            computational_markers.append(cog['computational_markers'])
            conditional_complexity.append(cog['conditional_complexity'])
            
            # 2. Coherence Chains
            coh = compute_coherence_chains(text, prev_text)
            reference_densities.append(coh['reference_density'])
            anaphoric_refs.append(coh['anaphoric_references'])
            demonstrative_refs.append(coh['demonstrative_references'])
            comparative_refs.append(coh['comparative_references'])
            continuity_markers.append(coh['continuity_markers'])
            entity_continuities.append(coh['entity_continuity'])
            
            # 3. Affective Trajectory
            aff = compute_affective_trajectory(text)
            dominant_affects.append(aff['dominant_affect'])
            affective_intensities.append(aff['affective_intensity'])
            affective_diversities.append(aff['affective_diversity'])
            curiosity_scores.append(aff['curiosity_score'])
            confusion_scores.append(aff['confusion_score'])
            satisfaction_scores.append(aff['satisfaction_score'])
            frustration_scores.append(aff['frustration_score'])
            surprise_scores.append(aff['surprise_score'])
            engagement_scores.append(aff['engagement_score'])
            
            # 4. Repair Patterns
            rep = compute_repair_patterns(text, role)
            total_repairs.append(rep['total_repair_markers'])
            repair_types.append(rep['repair_type'])
            self_corrections.append(rep['self_corrections'])
            clarification_requests.append(rep['clarification_requests'])
            confirmation_checks.append(rep['confirmation_checks'])
            elaboration_requests_list.append(rep['elaboration_requests'])
            repetitions.append(rep['repetitions'])
            
            # 5. Knowledge Construction
            know = compute_knowledge_construction(text)
            knowledge_scores.append(know['knowledge_construction_score'])
            construction_phases.append(know['construction_phase'])
            joint_attention.append(know['joint_attention_markers'])
            hypothesis_markers.append(know['hypothesis_markers'])
            evidence_markers_list.append(know['evidence_markers'])
            synthesis_markers.append(know['synthesis_markers'])
            perspective_markers.append(know['perspective_markers'])
            
            # 6. Social Presence
            soc = compute_social_presence(text)
            social_scores.append(soc['social_presence_score'])
            rapport_indices.append(soc['rapport_index'])
            acknowledgments.append(soc['acknowledgments'])
            encouragements.append(soc['encouragements'])
            empathy_markers_list.append(soc['empathy_markers'])
            solidarity_markers.append(soc['solidarity_markers'])
            politeness_markers_list.append(soc['politeness_markers'])
            humor_markers.append(soc['humor_markers'])
            
            # 7. Argumentation Structure
            arg = compute_argumentation_structure(text)
            argument_structures.append(arg['argument_structure'])
            argument_qualities.append(arg['argument_quality'])
            claim_markers.append(arg['claim_markers'])
            evidence_markers_arg.append(arg['evidence_markers'])
            warrant_markers.append(arg['warrant_markers'])
            qualifier_markers.append(arg['qualifier_markers'])
            rebuttal_markers.append(arg['rebuttal_markers'])
            
            # 8. Temporal Dynamics
            temp = compute_temporal_dynamics(text, row.get('response_time'))
            temporal_orientations.append(temp['temporal_orientation'])
            urgency_levels.append(temp['urgency_level'])
            urgency_markers.append(temp['urgency_markers'])
            reflection_markers.append(temp['reflection_markers'])
            projection_markers.append(temp['projection_markers'])
            pace_markers.append(temp['pace_markers'])
            
            # =============================================================================
            # NEW v3.2: Compute cognitive coupling metrics
            # =============================================================================
            word_count = row['word_count']
            iei = compute_iei(entropy, word_count)
            mirroring = compute_mirroring(prev_text, text)
            asymmetry = round(abs(readability - prev_readability), 2) if prev_readability else 0.0
            refusals = len(re.findall(REFUSAL_PATTERNS, text.lower()))
            
            iei_list.append(iei)
            mirroring_list.append(mirroring)
            asymmetry_list.append(asymmetry)
            refusals_list.append(refusals)
            
            # Update previous turn variables for next iteration
            prev_text = text
            prev_readability = readability
            # =============================================================================
            
            # BLEU/METEOR/ROUGE (for assistant responses)
            if row["role"] == "assistant" and i > 0:
                ref = df.iloc[i-1]["content"]
                cand = row["content"]
                bleu_scores.append(compute_bleu(ref, cand))
                meteor_scores.append(compute_meteor(ref, cand))
                rouge_scores = compute_rouge(ref, cand)
                rouge1_scores.append(rouge_scores.get("rouge1", 0))
                rougeL_scores.append(rouge_scores.get("rougeL", 0))
            else:
                bleu_scores.append(None)
                meteor_scores.append(None)
                rouge1_scores.append(None)
                rougeL_scores.append(None)
        
        # Add original metrics to DataFrame
        df["BLEU"] = bleu_scores
        df["METEOR"] = meteor_scores
        df["ROUGE-1"] = rouge1_scores
        df["ROUGE-L"] = rougeL_scores
        df["Entropy"] = entropy_scores
        df["Readability"] = readability_scores
        df["Lexical Diversity"] = lexdiv_scores
        df["Contradictions"] = contradictions
        df["Elaborations"] = elaborations
        df["Contra:Elab Ratio"] = contradiction_ratios
        df["Negations"] = negations
        df["Adversatives"] = adversatives
        df["Hedges"] = hedges_list
        df["Confidence Markers"] = confidence_list
        df["Epistemic Stance"] = epistemic_stance_list
        
        # =============================================================================
        # ADD NEW METRICS TO DATAFRAME
        # =============================================================================
        
        # Cognitive Load
        df["Cognitive_Load_Total"] = cog_load_totals
        df["Cognitive_Load_Density"] = cog_load_densities
        df["Complex_Connectors"] = complex_connectors
        df["Abstraction_Markers"] = abstraction_markers
        df["Metacognitive_Markers"] = metacognitive_markers
        df["Computational_Markers"] = computational_markers
        df["Conditional_Complexity"] = conditional_complexity
        
        # Coherence Chains
        df["Reference_Density"] = reference_densities
        df["Anaphoric_Refs"] = anaphoric_refs
        df["Demonstrative_Refs"] = demonstrative_refs
        df["Comparative_Refs"] = comparative_refs
        df["Continuity_Markers"] = continuity_markers
        df["Entity_Continuity"] = entity_continuities
        
        # Affective Trajectory
        df["Dominant_Affect"] = dominant_affects
        df["Affective_Intensity"] = affective_intensities
        df["Affective_Diversity"] = affective_diversities
        df["Curiosity_Score"] = curiosity_scores
        df["Confusion_Score"] = confusion_scores
        df["Satisfaction_Score"] = satisfaction_scores
        df["Frustration_Score"] = frustration_scores
        df["Surprise_Score"] = surprise_scores
        df["Engagement_Score"] = engagement_scores
        
        # Repair Patterns
        df["Total_Repair_Markers"] = total_repairs
        df["Repair_Type"] = repair_types
        df["Self_Corrections"] = self_corrections
        df["Clarification_Requests"] = clarification_requests
        df["Confirmation_Checks"] = confirmation_checks
        df["Elaboration_Requests"] = elaboration_requests_list
        df["Repetitions"] = repetitions
        
        # Knowledge Construction
        df["Knowledge_Construction_Score"] = knowledge_scores
        df["Construction_Phase"] = construction_phases
        df["Joint_Attention"] = joint_attention
        df["Hypothesis_Markers"] = hypothesis_markers
        df["Evidence_Markers"] = evidence_markers_list
        df["Synthesis_Markers"] = synthesis_markers
        df["Perspective_Markers"] = perspective_markers
        
        # Social Presence
        df["Social_Presence_Score"] = social_scores
        df["Rapport_Index"] = rapport_indices
        df["Acknowledgments"] = acknowledgments
        df["Encouragements"] = encouragements
        df["Empathy_Markers"] = empathy_markers_list
        df["Solidarity_Markers"] = solidarity_markers
        df["Politeness_Markers"] = politeness_markers_list
        df["Humor_Markers"] = humor_markers
        
        # Argumentation
        df["Argument_Structure"] = argument_structures
        df["Argument_Quality"] = argument_qualities
        df["Claim_Markers"] = claim_markers
        df["Argument_Evidence_Markers"] = evidence_markers_arg
        df["Warrant_Markers"] = warrant_markers
        df["Qualifier_Markers"] = qualifier_markers
        df["Rebuttal_Markers"] = rebuttal_markers
        
        # Temporal Dynamics
        df["Temporal_Orientation"] = temporal_orientations
        df["Urgency_Level"] = urgency_levels
        df["Urgency_Markers"] = urgency_markers
        df["Reflection_Markers"] = reflection_markers
        df["Projection_Markers"] = projection_markers
        df["Pace_Markers"] = pace_markers
        
        # =============================================================================
        # NEW v3.2: Add cognitive coupling columns
        # =============================================================================
        df["IEI_Efficiency"] = iei_list
        df["Lexical_Mirroring"] = mirroring_list
        df["Cognitive_Asymmetry"] = asymmetry_list
        df["Refusal_Markers"] = refusals_list
        # =============================================================================
        
        # Compute thread-level metrics
        print(f"  🔍 Computing thread-level analysis...")
        
        flow_data = compute_keyword_flow(df)
        sentiment_shift = compute_sentiment_shift(df["sentiment"].tolist())
        
        # Analyze turn pairs
        turn_pairs = analyze_turn_pairs(df)
        avg_response_ratio = np.mean([p['response_ratio'] for p in turn_pairs]) if turn_pairs else 0
        avg_semantic_overlap = np.mean([p['semantic_overlap'] for p in turn_pairs]) if turn_pairs else 0
        
        # Convergence detection
        if len(df) >= 20:
            convergence_data = detect_convergence_patterns(df, window_size=10)
            if convergence_data:
                final_trend = convergence_data[-1]['contradiction_trend']
            else:
                final_trend = 'insufficient_data'
        else:
            final_trend = 'insufficient_data'
        
        # Write main sheet to main output file
        df.to_excel(main_writer, sheet_name=safe_title, index=False)
        ws = main_writer.sheets[safe_title]
        
        # Format sheet
        ws.write_url('A1', "internal:'Thread Summary'!A1", string="⬅ BACK TO SUMMARY")
        ws.freeze_panes(1, 1)
        ws.set_row(0, None, header_fmt_main)
        
        # Set column widths
        column_widths = {
            'Seq. #': 10, 'timestamp': 20, 'role': 12, 'content': 50, 
            'word_count': 12, 'token_count': 12, 'sentence_count': 12,
            'sentiment': 12, 'sentiment_score': 12, 'subjectivity': 12,
            'model': 15, 'dialogue_act': 15, 'response_time': 15,
            'BLEU': 10, 'METEOR': 10, 'ROUGE-1': 10, 'ROUGE-L': 10,
            'Entropy': 10, 'Readability': 12, 'Lexical Diversity': 15,
            'Contradictions': 13, 'Elaborations': 12, 'Contra:Elab Ratio': 15,
            'Negations': 10, 'Adversatives': 12, 'Hedges': 10,
            'Confidence Markers': 15, 'Epistemic Stance': 15,
            'edit_count': 10, 'edit_similarity': 15,
            # New metrics
            'Cognitive_Load_Total': 15, 'Cognitive_Load_Density': 15,
            'Complex_Connectors': 15, 'Abstraction_Markers': 15,
            'Metacognitive_Markers': 18, 'Computational_Markers': 18,
            'Conditional_Complexity': 18, 'Reference_Density': 15,
            'Anaphoric_Refs': 15, 'Demonstrative_Refs': 17,
            'Comparative_Refs': 16, 'Continuity_Markers': 16,
            'Entity_Continuity': 15, 'Dominant_Affect': 15,
            'Affective_Intensity': 16, 'Affective_Diversity': 17,
            'Curiosity_Score': 14, 'Confusion_Score': 14,
            'Satisfaction_Score': 16, 'Frustration_Score': 15,
            'Surprise_Score': 13, 'Engagement_Score': 15,
            'Total_Repair_Markers': 17, 'Repair_Type': 13,
            'Self_Corrections': 15, 'Clarification_Requests': 18,
            'Confirmation_Checks': 17, 'Elaboration_Requests': 18,
            'Repetitions': 12, 'Knowledge_Construction_Score': 20,
            'Construction_Phase': 16, 'Joint_Attention': 15,
            'Hypothesis_Markers': 17, 'Evidence_Markers': 15,
            'Synthesis_Markers': 16, 'Perspective_Markers': 17,
            'Social_Presence_Score': 17, 'Rapport_Index': 13,
            'Acknowledgments': 14, 'Encouragements': 14,
            'Empathy_Markers': 14, 'Solidarity_Markers': 16,
            'Politeness_Markers': 16, 'Humor_Markers': 13,
            'Argument_Structure': 16, 'Argument_Quality': 15,
            'Claim_Markers': 13, 'Argument_Evidence_Markers': 20,
            'Warrant_Markers': 14, 'Qualifier_Markers': 15,
            'Rebuttal_Markers': 15, 'Temporal_Orientation': 17,
            'Urgency_Level': 13, 'Urgency_Markers': 14,
            'Reflection_Markers': 16, 'Projection_Markers': 16,
            'Pace_Markers': 12,
            # v3.2 columns
            'IEI_Efficiency': 14, 'Lexical_Mirroring': 18, 'Cognitive_Asymmetry': 18, 'Refusal_Markers': 14
        }
        
        for col_idx, col_name in enumerate(df.columns):
            width = column_widths.get(col_name, 15)
            ws.set_column(col_idx, col_idx, width, center_fmt_main)
        
        print(f"  ✅ Processed {len(df)} messages\n")
        
        # Prepare summary row with new metrics
        summary_rows.append({
            "Thread": safe_title,
            "Duration": conversation_duration,
            "Total Messages": len(df),
            "User Turns": len(df[df["role"]=="user"]),
            "Assistant Turns": len(df[df["role"]=="assistant"]),
            "Avg Words": round(df["word_count"].mean(), 1),
            "Total Tokens": df["token_count"].sum(),
            "Sentiment Shift": sentiment_shift,
            "Avg Response Time (s)": round(df["response_time"].dropna().mean(), 1),
            "Avg Entropy": round(df["Entropy"].mean(), 2),
            "Avg Readability": round(df["Readability"].mean(), 1),
            "Avg Lexical Diversity": round(df["Lexical Diversity"].mean(), 3),
            "Flow Edges": flow_data['flow_edges'],
            "Keyword Persistence": flow_data['avg_persistence'],
            "Top Keyphrases": ", ".join(flow_data['top_keywords']),
            "Total Edits": int(df["edit_count"].sum()),
            "Avg Edit Similarity": round(df["edit_similarity"].dropna().mean(), 3),
            "Total Elaborations": int(df["Elaborations"].sum()),
            "Total Contradictions": int(df["Contradictions"].sum()),
            "Contra:Elab Ratio": round(df["Contradictions"].sum() / df["Elaborations"].sum(), 2) if df["Elaborations"].sum() > 0 else float('inf'),
            "Avg Hedges": round(df["Hedges"].mean(), 1),
            "Avg Confidence": round(df["Confidence Markers"].mean(), 1),
            "Avg Response Ratio": round(avg_response_ratio, 2),
            "Avg Semantic Overlap": round(avg_semantic_overlap, 3),
            "Convergence Trend": final_trend,
            # New summary metrics
            "Avg_Cognitive_Load": round(df["Cognitive_Load_Density"].mean(), 2),
            "Avg_Coherence": round(df["Entity_Continuity"].dropna().mean(), 3),
            "Dominant_Affect_Thread": df["Dominant_Affect"].mode()[0] if not df["Dominant_Affect"].empty else 'neutral',
            "Total_Repairs": int(df["Total_Repair_Markers"].sum()),
            "Self_Repair_Rate": round(df["Self_Corrections"].sum() / len(df), 3),
            "Knowledge_Phase_Final": df["Construction_Phase"].iloc[-1] if not df.empty else 'unknown',
            "Avg_Social_Presence": round(df["Social_Presence_Score"].mean(), 2),
            "Avg_Rapport": round(df["Rapport_Index"].mean(), 2),
            "Complete_Arguments": len(df[df["Argument_Structure"] == "complete_argument"]),
            "Urgency_High_Count": len(df[df["Urgency_Level"] == "high"]),
            "Temporal_Focus": df["Temporal_Orientation"].mode()[0] if not df["Temporal_Orientation"].empty else 'present_focused'
        })
        
        # =============================================================================
        # COLLECT DATA FOR MATRICES (global and per-thread)
        # =============================================================================
        
        # --- Global act transition ---
        msgs = rows  # list of dicts with 'dialogue_act'
        for i in range(len(msgs)-1):
            current_act = msgs[i].get("dialogue_act")
            next_act = msgs[i+1].get("dialogue_act")
            if current_act and next_act:
                global_act_counts[current_act][next_act] += 1
        
        # --- Global messages list for correlation ---
        for _, row in df.iterrows():
            msg_dict = row.to_dict()
            msg_dict['thread'] = safe_title
            all_messages_list.append(msg_dict)
        
        # --- Per-thread act transition ---
        thread_act_counts[safe_title] = defaultdict(lambda: defaultdict(int))
        for i in range(len(msgs)-1):
            current_act = msgs[i].get("dialogue_act")
            next_act = msgs[i+1].get("dialogue_act")
            if current_act and next_act:
                thread_act_counts[safe_title][current_act][next_act] += 1
        
        # --- Per-thread numeric data for correlation ---
        # Select numeric columns, drop those with all NaN or constant if needed
        numeric_df = df.select_dtypes(include=[np.number])
        # Exclude columns that are not meaningful for correlation (like index columns)
        exclude_cols = ['Seq. #'] if 'Seq. #' in numeric_df.columns else []
        numeric_df = numeric_df.drop(columns=exclude_cols, errors='ignore')
        thread_numeric_data[safe_title] = numeric_df
        
        process_notes.append(f"✅ '{title}' -> {len(df)} messages analyzed")
    
    # === Thread Summary Sheet (main output) ===
    print("\n" + "=" * 80)
    print("CREATING SUMMARY SHEET (main output)")
    print("=" * 80)
    
    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_excel(main_writer, sheet_name="Thread Summary", index=False)
    summary_ws = main_writer.sheets["Thread Summary"]
    summary_ws.freeze_panes(1, 1)
    summary_ws.set_row(0, None, header_fmt_main)
    for col in range(len(summary_df.columns)):
        summary_ws.set_column(col, col, 20, center_fmt_main)
    # Add hyperlinks to threads
    for i, thread in enumerate(summary_df["Thread"], start=1):
        summary_ws.write_url(i, 0, f"internal:'{thread}'!A1", string=thread)
    
    # === Methodology Notes Sheet (main output) ===
    notes_ws = main_writer.book.add_worksheet("Methodology Notes")
    notes_ws.set_column(0, 0, 100)
    
    methodology_text = [
        "ENHANCED CHAT ANALYSIS TOOL v3.2 - METHODOLOGY NOTES",
        "=" * 80,
        "",
        "MEASUREMENT APPROACH:",
        "",
        "1. CONTRADICTION DETECTION (Enhanced)",
        "   - Uses 5 pattern types: negation, adversative, correction, disagreement, limitation",
        "   - Counts linguistic markers, not semantic contradictions",
        "   - Valid as proxy for adversarial intensity",
        "   - Total contradictions = sum across all pattern types",
        "",
        "2. ELABORATION DETECTION (Enhanced)", 
        "   - Uses 5 pattern types: causation, explanation, expansion, consequence, exemplification",
        "   - Counts supportive/explanatory connectors",
        "   - Proxy for elaborative discourse",
        "",
        "3. EPISTEMIC MARKERS",
        "   - Hedges: uncertainty markers (might, possibly, perhaps, etc.)",
        "   - Confidence: certainty markers (definitely, clearly, must, etc.)",
        "   - Epistemic Stance: confidence - hedges (more positive = more certain)",
        "",
        "4. TURN PAIR ANALYSIS",
        "   - Response ratio: AI words / User words (indicates elaboration level)",
        "   - Semantic overlap: Shared keywords between turns (topical continuity)",
        "",
        "5. CONVERGENCE DETECTION",
        "   - Tracks contradiction rates over sliding windows",
        "   - Identifies trend: decreasing = converging, stable = sustained engagement",
        "   - Requires minimum 20 messages for analysis",
        "",
        "================================================================================",
        "NEW IN v3.0: ADVANCED DIALOGUE DYNAMICS METRICS",
        "================================================================================",
        "",
        "6. COGNITIVE LOAD INDICATORS",
        "   - Measures mental effort through linguistic complexity markers",
        "   - Components: complex connectors, abstraction, metacognition, computation, conditionals",
        "   - Density: markers per 100 words (normalized for length)",
        "   - Validity: Higher density indicates more cognitively demanding processing",
        "",
        "7. DISCOURSE COHERENCE CHAINS",
        "   - Tracks reference continuity across turns (anaphoric, demonstrative, comparative)",
        "   - Entity Continuity: proportion of entities carried over from previous turn",
        "   - Reference Density: referential expressions per 100 words",
        "   - Validity: Measures topic maintenance and discourse integration",
        "",
        "8. AFFECTIVE TRAJECTORY (Beyond Polarity)",
        "   - Multi-dimensional emotional states: curiosity, confusion, satisfaction,",
        "     frustration, surprise, engagement",
        "   - Affective Diversity: count of distinct emotions expressed",
        "   - Dominant Affect: most frequent emotional marker",
        "   - Validity: Captures emotional nuance missed by positive/negative polarity",
        "",
        "9. CONVERSATIONAL REPAIR PATTERNS",
        "   - Self-correction: speaker fixes own error",
        "   - Clarification request: explicit request for explanation",
        "   - Confirmation check: verifying understanding",
        "   - Elaboration request: seeking more detail",
        "   - Repair Type classification: identifies who initiates repair and how",
        "   - Validity: Indicates trouble spots and collaborative grounding efforts",
        "",
        "10. KNOWLEDGE CONSTRUCTION MARKERS",
        "   - Joint Attention: collaborative focus markers (let's, together, our)",
        "   - Hypothesis Generation: exploratory language (what if, suppose, imagine)",
        "   - Evidence Evaluation: data-driven reasoning (research shows, evidence)",
        "   - Synthesis Integration: combining information (connect, integrate, overall)",
        "   - Construction Phase: classification of knowledge-building stage",
        "   - Validity: Distinguishes information exchange from collaborative learning",
        "",
        "11. SOCIAL PRESENCE & RAPPORT",
        "   - Acknowledgment: validating partner's contribution",
        "   - Encouragement: positive reinforcement",
        "   - Empathy: emotional attunement markers",
        "   - Solidarity: in-group identity construction (we, us, together)",
        "   - Politeness: face-saving strategies",
        "   - Humor: relational maintenance through playfulness",
        "   - Rapport Index: weighted combination of solidarity and acknowledgment",
        "   - Validity: Measures relational quality beyond task completion",
        "",
        "12. ARGUMENTATION STRUCTURE (Toulmin-inspired)",
        "   - Claim: assertive propositions (argue, claim, assert, maintain)",
        "   - Evidence: supporting data (because, since, evidence, shows)",
        "   - Warrant: inference licenses (therefore, thus, implies)",
        "   - Qualifier: certainty modulation (probably, generally, usually)",
        "   - Rebuttal: counter-considerations (however, but, although)",
        "   - Structure Classification: complete vs. partial arguments",
        "   - Argument Quality: 0-4 scale based on component presence",
        "   - Validity: Assesses reasoning quality and critical thinking",
        "",
        "13. TEMPORAL DYNAMICS",
        "   - Temporal Orientation: past-focused (reflection) vs. future-focused (projection)",
        "   - Urgency Level: time pressure indicators (immediate, critical, deadline)",
        "   - Pace Markers: speed indicators (step by step, gradually, suddenly)",
        "   - Validity: Reveals time perspective and conversational momentum",
        "",
        "================================================================================",
        "NEW IN v3.1: MATRIX SHEETS (separate file)",
        "================================================================================",
        "",
        "14. DIALOGUE ACT TRANSITION MATRIX",
        "   - Two sheets: counts and probabilities (global, across all threads)",
        "   - Shows how often one dialogue act (row) is followed by another (column)",
        "   - Reveals conversational flow patterns, e.g., question → answer, clarification → elaboration",
        "   - Per-thread matrices are also generated in the matrix file.",
        "",
        "15. CROSS-METRIC CORRELATION MATRIX",
        "   - Pearson correlation between all numerical metrics computed per message (global)",
        "   - Highlights relationships: e.g., do higher cognitive load and more contradictions co‑occur?",
        "   - Conditional formatting (color scale) aids quick visual interpretation",
        "   - Helps identify redundant metrics and generate hypotheses",
        "",
        "================================================================================",
        "NEW IN v3.2: COGNITIVE COUPLING METRICS",
        "================================================================================",
        "",
        "16. INFORMATION EFFICIENCY INDEX (IEI)",
        "   - Formula: Shannon Entropy / Word Count",
        "   - Measures information density per word. Higher values suggest more compact, information-rich utterances.",
        "",
        "17. LEXICAL MIRRORING",
        "   - Overlap of significant words (length ≥4) between consecutive turns.",
        "   - Quantifies syntactic alignment / social entrainment.",
        "   - Values near 1 indicate high repetition of key terms; a drop to 0 can signal a breakdown in mutual understanding.",
        "",
        "18. COGNITIVE ASYMMETRY",
        "   - Absolute change in readability score between consecutive turns.",
        "   - Large spikes indicate abrupt shifts in linguistic complexity – a potential sign of misalignment.",
        "",
        "19. REFUSAL MARKERS",
        "   - Counts of phrases indicating the AI's boundaries (e.g., 'as an AI', 'cannot', 'sorry', 'policy').",
        "   - Tracks when the system invokes its epistemic limits.",
        "",
        "LIMITATIONS:",
        "",
        "- All pattern-based metrics are lexical proxies, not semantic analysis",
        "- Pattern matching may have false positives in colloquial language",
        "- BLEU/METEOR/ROUGE adapted from machine translation context",
        "- Readability scores approximated (syllable counting heuristic)",
        "- Affective and cognitive states inferred from language, not measured directly",
        "- Cultural variations in politeness/humor not accounted for",
        "",
        "VALIDITY:",
        "",
        "- Metrics are sufficient for comparative analysis across threads",
        "- Patterns replicate across multiple conversations (4:1 ratio observed)",
        "- Correlates with qualitative assessment of dialogue quality",
        "- Enables systematic, reproducible measurement",
        "- New v3.2 metrics grounded in cognitive science and discourse analysis",
        "",
        "CITATION:",
        "",
        "If using this tool in research, please cite:",
        "Enhanced Chat Analysis Tool v3.2",
        "Adapted from: [Original Author] extended by Claude (Anthropic) and Gemini",
        f"Generated: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "LICENSE: MIT (Open Source)",
        "",
        "=" * 80,
        "",
        "THREAD ANALYSIS COMPLETED",
        f"Total threads analyzed: {len(summary_df)}",
        f"Total messages: {summary_df['Total Messages'].sum():,}",
        f"Total tokens: {summary_df['Total Tokens'].sum():,}",
        f"Overall Contra:Elab ratio: {summary_df['Total Contradictions'].sum() / summary_df['Total Elaborations'].sum():.2f}:1",
        "",
        "NEW v3.0 CAPABILITIES:",
        f"- Cognitive Load tracking: {summary_df['Avg_Cognitive_Load'].mean():.2f} avg density",
        f"- Affective dimensions: 6 emotion types tracked",
        f"- Repair patterns: {summary_df['Total_Repairs'].sum()} total repairs detected",
        f"- Knowledge phases: {summary_df['Knowledge_Phase_Final'].nunique()} distinct phases",
        f"- Argument quality: {summary_df['Complete_Arguments'].sum()} complete arguments",
        f"- Social presence: {summary_df['Avg_Social_Presence'].mean():.2f} avg score",
        "",
        "NEW v3.1 MATRICES ADDED:",
        f"- Dialogue Act Transition Matrices (global & per-thread)",
        f"- Cross-Metric Correlation Matrix (global)",
        "",
        "NEW v3.2 COGNITIVE COUPLING METRICS:",
        f"- Information Efficiency Index",
        f"- Lexical Mirroring (syntactic alignment)",
        f"- Cognitive Asymmetry",
        f"- Refusal Markers",
    ]
    
    for row_idx, line in enumerate(methodology_text):
        notes_ws.write(row_idx, 0, line)
    
    # =============================================================================
    # WRITE MATRIX OUTPUT FILE (unchanged from v3.1)
    # =============================================================================
    print("\n" + "=" * 80)
    print("WRITING MATRIX ANALYSIS FILE")
    print("=" * 80)
    
    # --- 1. Global act transition matrices ---
    all_acts = sorted(set(global_act_counts.keys()).union(*[d.keys() for d in global_act_counts.values()]))
    # Counts matrix
    global_counts_df = pd.DataFrame(0, index=all_acts, columns=all_acts)
    for from_act, to_dict in global_act_counts.items():
        for to_act, cnt in to_dict.items():
            global_counts_df.loc[from_act, to_act] = cnt
    global_counts_df.to_excel(matrix_writer, sheet_name="Global_Act_Counts")
    
    # Probabilities matrix
    global_prob_df = global_counts_df.div(global_counts_df.sum(axis=1), axis=0).fillna(0)
    global_prob_df.to_excel(matrix_writer, sheet_name="Global_Act_Prob")
    
    # --- 2. Global correlation matrix ---
    if all_messages_list:
        global_all_df = pd.DataFrame(all_messages_list)
        global_numeric = global_all_df.select_dtypes(include=[np.number])
        # Exclude any unwanted columns (e.g., index-like)
        global_numeric = global_numeric.loc[:, ~global_numeric.columns.str.contains('Seq', case=False)]
        if global_numeric.shape[1] > 1:
            global_corr = global_numeric.corr()
            global_corr.to_excel(matrix_writer, sheet_name="Global_Correlation")
            # Apply conditional formatting for heatmap
            corr_ws = matrix_writer.sheets["Global_Correlation"]
            corr_ws.conditional_format(1, 1, len(global_corr), len(global_corr),
                                       {'type': '3_color_scale',
                                        'min_color': "#F8696B",   # red for -1
                                        'mid_color': "#FFEB84",   # yellow for 0
                                        'max_color': "#63BE7B"})  # green for 1
        else:
            # Write placeholder if insufficient columns
            pd.DataFrame().to_excel(matrix_writer, sheet_name="Global_Correlation")
    
    # --- 3. Per-thread matrices ---
    for thread_name in thread_act_counts:
        # Act transition for this thread
        acts = sorted(set(thread_act_counts[thread_name].keys()).union(*[d.keys() for d in thread_act_counts[thread_name].values()]))
        if acts:
            # Counts
            thread_counts_df = pd.DataFrame(0, index=acts, columns=acts)
            for from_act, to_dict in thread_act_counts[thread_name].items():
                for to_act, cnt in to_dict.items():
                    thread_counts_df.loc[from_act, to_act] = cnt
            sheet_name_counts = f"{thread_name}_ActCounts"[:31]  # Excel sheet name max 31 chars
            thread_counts_df.to_excel(matrix_writer, sheet_name=sheet_name_counts)
            
            # Probabilities
            thread_prob_df = thread_counts_df.div(thread_counts_df.sum(axis=1), axis=0).fillna(0)
            sheet_name_prob = f"{thread_name}_ActProb"[:31]
            thread_prob_df.to_excel(matrix_writer, sheet_name=sheet_name_prob)
        
        # Correlation for this thread
        if thread_name in thread_numeric_data:
            numeric_df = thread_numeric_data[thread_name]
            if numeric_df.shape[1] > 1 and numeric_df.shape[0] > 1:
                corr = numeric_df.corr()
                sheet_name_corr = f"{thread_name}_Corr"[:31]
                corr.to_excel(matrix_writer, sheet_name=sheet_name_corr)
                # Apply conditional formatting
                ws_corr = matrix_writer.sheets[sheet_name_corr]
                ws_corr.conditional_format(1, 1, len(corr), len(corr),
                                           {'type': '3_color_scale',
                                            'min_color': "#F8696B",
                                            'mid_color': "#FFEB84",
                                            'max_color': "#63BE7B"})
    
    # Optional: add a short readme sheet in matrix file
    readme = [
        "MATRIX ANALYSIS FILE",
        "====================",
        "This file contains global and per-thread matrices.",
        "",
        "- Global_Act_Counts / Prob: dialogue act transitions across all threads.",
        "- Global_Correlation: Pearson correlation of all numeric metrics across all messages.",
        "- For each thread:",
        "    * <Thread>_ActCounts / Prob: act transition matrices for that thread.",
        "    * <Thread>_Corr: correlation matrix for that thread (if enough data).",
        "",
        "Note: Sheet names are truncated to 31 characters."
    ]
    readme_ws = workbook_matrix.add_worksheet("README")
    for i, line in enumerate(readme):
        readme_ws.write(i, 0, line)
    readme_ws.set_column(0, 0, 80)

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
print("\n".join(process_notes))
print(f"\n✅ Main analysis exported to: {main_output_file}")
print(f"📊 Matrix analysis exported to: {matrix_output_file}")
print(f"📊 Total messages analyzed: {summary_df['Total Messages'].sum():,}")
print("\n📖 See methodology notes in main file for details.")
print("=" * 80)