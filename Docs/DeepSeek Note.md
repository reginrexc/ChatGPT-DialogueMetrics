## DeepSeek Contributions (v3.2)

Building on the robust **v3.1 matrix architecture** (which introduced two‑file output with global and per‑thread transition/correlation matrices), DeepSeek added a suite of **cognitive coupling metrics** designed to quantify the dynamic interplay between user and assistant. These metrics are computed per message and appear as new columns in every conversation sheet of the main Excel output (`chat_analysis_TIMESTAMP.xlsx`). They are also included in the correlation matrices of the separate matrix file (`chat_matrices_TIMESTAMP.xlsx`), enabling exploration of their relationships with all other dialogue features.

### 1. Information Efficiency Index (IEI)
**Formula:**  
`IEI_Efficiency = Shannon Entropy / Word Count`

**Interpretation:**  
IEI measures how densely information is packed into a message.  
- **High IEI** → the speaker conveys many unique ideas in few words; characteristic of expert, concise communication.  
- **Low IEI** → verbose or repetitive language; may indicate exploratory thinking, uncertainty, or low engagement.

**Usage:** Track IEI over time to see when the user becomes more (or less) information‑dense. Compare with assistant responses to gauge whether the AI matches the user’s efficiency.

### 2. Lexical Mirroring (Syntactic Alignment)
**Formula:**  
`Lexical_Mirroring = |significant_words(prev_turn) ∩ significant_words(current_turn)| / |significant_words(prev_turn)|`  
where *significant words* are those with length ≥4 characters (filtering out short function words).

**Interpretation:**  
Lexical mirroring quantifies how much the current speaker borrows distinctive vocabulary from the previous turn.  
- **High mirroring** → strong alignment; the speaker is actively listening and building on the partner’s language.  
- **Low or dropping mirroring** → potential breakdown in mutual understanding; the speaker may be ignoring the previous turn or introducing a completely new topic.

**Usage:** A sudden drop in mirroring often marks the exact moment an interaction becomes dysfunctional – invaluable for diagnosing conversation failures.

### 3. Cognitive Asymmetry
**Formula:**  
`Cognitive_Asymmetry = abs(Readability(current) - Readability(previous))`

**Interpretation:**  
Readability (Flesch Reading Ease) reflects linguistic complexity. The asymmetry captures abrupt shifts in complexity between consecutive turns.  
- **Large asymmetry** → a sharp change in how the message is structured; may signal emotional arousal, topic shift, or a mismatch in cognitive load.  
- **Sustained low asymmetry** → stable, predictable exchange.

**Usage:** Combine with mirroring: when asymmetry spikes while mirroring drops, you have identified a coordination breakdown.

### 4. Refusal Markers (System Boundary Invocations)
**Pattern:**  
`REFUSAL_PATTERNS = r'\b(as an ai|cannot|unable|sorry|policy|guidelines|restricted|harmful|legal advice|medical advice|violate)\b'`

**Interpretation:**  
Counts how often the assistant (or user) explicitly references the AI’s limitations or ethical boundaries.  
- **High refusal count** in assistant messages → the conversation frequently hits the model’s guardrails; may indicate user requests that fall outside allowed domains.  
- **Refusals in user messages** (rare) could be ironic or meta‑comments about the AI’s capabilities.

**Usage:** Monitor refusal frequency to assess how often the conversation approaches the system’s epistemic limits, and whether this correlates with user frustration or disengagement.

### Integration with the v3.1 Matrix Output
All four metrics are numerical and are therefore included in:
- **Global correlation matrix** (`Global_Correlation` sheet) – see how they relate to sentiment, cognitive load, argument quality, etc.  
- **Per‑thread correlation matrices** – examine their behaviour within individual conversations.

### Why These Metrics Matter
Together, they provide a **real‑time lens on cognitive alignment** between human and AI. While earlier metrics (e.g., sentiment, contradictions) capture the *content* of the dialogue, these new ones capture the *dynamics* of understanding and misalignment. They allow researchers to pinpoint the exact moment when two speakers stop coordinating – a crucial capability for studying human‑AI interaction, designing better conversational agents, and evaluating dialogue quality.

*DeepSeek contribution – v3.2, February 2025*
