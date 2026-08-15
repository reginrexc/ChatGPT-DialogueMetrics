
# DialogueMetrics v3.2 — Complete Equation / Computation Inventory

## A. Basic linguistic measurements

### 1. Word Count

$$
\large W = \text{number of whitespace-separated tokens}
$$

Implemented as:

```python
len(text.split())
```

So this is **not** a linguistic tokenizer; it is whitespace‑based. 

---

### 2. Token Count

$$
\large T = |\text{Tokenizer}(text)|
$$

The script uses:

```python
tiktoken.get_encoding("cl100k_base")
```

and counts encoded tokens. 

Important methodological note: **token count is GPT `cl100k_base` tokenization**, even when analyzing Claude, DeepSeek, or Qwen.

That should be explicitly documented.

---

### 3. Sentence Count

$$
\large S = |\text{split}(text,\ [.!?]+)|
$$

The script splits on `.`, `!`, and `?`. 

---

### 4. Estimated syllable count

For each word, the script:

1. counts vowel‑group transitions,
2. subtracts one for terminal `e`,
3. adds one for terminal consonant + `le`,
4. applies:

$$
\large Syllables(word)=\max(1,SyllableEstimate)
$$

This is a heuristic rather than a dictionary‑based syllable count. 

---

## B. Sentiment

### 5. Sentiment polarity

The script delegates polarity to **TextBlob**:

$$
\large P \in [-1,1]
$$

Classification:

$$
\large
Label =
\begin{cases}
Positive & P>0.05\\
Negative & P<-0.05\\
Neutral & -0.05\le P\le0.05
\end{cases}
$$

Subjectivity is also returned by TextBlob:

$$
\large Subjectivity \in [0,1]
$$

---

### 6. Sentiment shift

The categorical sentiment labels are mapped:

$$
\large Negative=-1,\quad Neutral=0,\quad Positive=1
$$

Then:

$$
\large
SentimentShift =
\frac{1}{n-1}
\sum_{i=2}^{n}|S_i-S_{i-1}|
$$

This is **categorical sentiment volatility**, not continuous polarity volatility.

---

## C. Information / lexical metrics

### 7. Shannon Entropy

This is one of the most important genuine mathematical metrics in the system.

For token probabilities $p_i$:

$$
\large
\boxed{
H=-\sum_i p_i\log_2(p_i)
}
$$

where:

$$
\large p_i=\frac{c_i}{N}
$$

and $c_i$ is the frequency of token $i$.

Higher entropy means greater distributional diversity among the observed tokens.

---

### 8. Type‑Token Ratio

$$
\large
\boxed{
TTR=\frac{V}{N}
}
$$

where:

- $V$ = unique word types
- $N$ = total words

---

### 9. Unique words per 100 words

$$
\large
\boxed{
U_{100}=\frac{V}{N}\times100
}
$$

### Important correction

The function documentation mentions **MTLD**, but the code shown does **not actually calculate MTLD**. It only calculates TTR and unique words per 100 words. 

That should be corrected in the methodology sheet.

---

## D. Readability

### 10. Flesch Reading Ease

The script implements:

$$
\large
\boxed{
FRE =
206.835
-
1.015\left(\frac{W}{S}\right)
-
84.6\left(\frac{Y}{W}\right)
}
$$

where:

- $W$ = word count
- $S$ = sentence count
- $Y$ = estimated syllable count

---

## E. Contradiction / adversarial structure

These are **marker‑count metrics**, not semantic contradiction equations.

For each contradiction category $k$:

$$
\large C_k = \text{RegexCount}(pattern_k,text)
$$

Total:

$$
\large
\boxed{
C_{total}=
C_{negation}
+C_{adversative}
+C_{correction}
+C_{disagreement}
+C_{limitation}
}
$$

The five categories are explicitly defined in the script. 

---

### 11. Contradiction:Elaboration Ratio

$$
\large
\boxed{
CER=\frac{C_{total}}{E_{total}}
}
$$

where $E_{total}$ is the total elaboration‑marker count.

If elaborations are zero, the current implementation returns:

$$
\large CER=\infty
$$

This is worth changing eventually to `NaN` because infinity can distort downstream statistics.

---

## F. Elaboration

For each elaboration category:

$$
\large E_k=\text{RegexCount}(pattern_k,text)
$$

Total:

$$
\large
\boxed{
E_{total}
=
E_{causation}
+E_{explanation}
+E_{expansion}
+E_{consequence}
+E_{exemplification}
}
$$

The five categories are explicitly defined in the code. 

Again, this is a **lexical elaboration proxy**, not semantic elaboration.

---

## G. Epistemic stance

### 12. Hedge count

$$
\large H_c=\text{RegexCount}(hedge\ patterns)
$$

### 13. Confidence count

$$
\large C_c=\text{RegexCount}(confidence\ patterns)
$$

### 14. Epistemic Stance

$$
\large
\boxed{
ES=C_c-H_c
}
$$

Positive values indicate more confidence markers than hedge markers.

This is one of the clearest examples where the metric is **an operational linguistic index**, not a direct measurement of epistemic certainty.

---

## H. Cognitive Load Indicators

### 15. Cognitive Load Total

For five marker classes:

$$
\large
\boxed{
CL=
CC+AB+MC+CO+CN
}
$$

where:

- $CC$ = complex connectors
- $AB$ = abstraction
- $MC$ = metacognition
- $CO$ = computational
- $CN$ = conditional

---

### 16. Cognitive Load Density

$$
\large
\boxed{
CLD=
\frac{CL}{W}\times100
}
$$

This is the normalized form of the cognitive‑load marker count. 

---

## I. Discourse coherence

### 17. Reference Count

$$
\large
R=
R_{anaphoric}
+R_{demonstrative}
+R_{comparative}
+R_{continuity}
$$

### 18. Reference Density

$$
\large
\boxed{
RD=\frac{R}{W}\times100
}
$$

### 19. Entity Continuity

For consecutive turns:

$$
\large
\boxed{
EC=
\frac{|P\cap C|}{|P|}
}
$$

where:

- $P$ = previous‑turn content words after stopword removal
- $C$ = current‑turn content words after stopword removal

This is technically **lexical continuity**, despite being named Entity Continuity.

That distinction is important.

---

## J. Affective trajectory

For each affect $a$:

$$
\large A_a=\text{RegexCount}(pattern_a,text)
$$

The six dimensions are:

$$
\large Curiosity,\ Confusion,\ Satisfaction,\ Frustration,\ Surprise,\ Engagement
$$

### 20. Affective Intensity

$$
\large
\boxed{
AI=\sum_a A_a
}
$$

### 21. Affective Diversity

$$
\large
\boxed{
AD=|\{a:A_a>0\}|
}
$$

### 22. Dominant Affect

$$
\large
\boxed{
DA=\arg\max_a A_a
}
$$

Again, these are **lexical affect markers**, not physiological or psychological measurements.

---

## K. Conversational repair

For each repair category:

$$
\large R_k=\text{RegexCount}(pattern_k,text)
$$

### 23. Total Repair Markers

$$
\large
\boxed{
R_{total}=
R_{self}
+R_{clarification}
+R_{confirmation}
+R_{elaboration}
+R_{repetition}
}
$$

### 24. Repair Type

This is categorical precedence logic:

$$
\large
RepairType=
\begin{cases}
SelfRepair & R_{self}>0\\
OtherRepairRequest & R_{clarification}>0\\
Confirmation & R_{confirmation}>0\\
ElaborationRequest & R_{elaboration}>0\\
None & otherwise
\end{cases}
$$

Note that the precedence order matters.

---

## L. Knowledge construction

### 25. Knowledge Construction Score

$$
\large
\boxed{
KCS=
J+H+E+S+P
}
$$

where:

- $J$ = joint attention
- $H$ = hypothesis
- $E$ = evidence
- $S$ = synthesis
- $P$ = perspective

### 26. Construction Phase

Categorical rule:

$$
\large
Phase=
\begin{cases}
Hypothesis & H>S\\
Evidence & E>0\\
Synthesis & S>0\\
Information\ Exchange & otherwise
\end{cases}
$$

Again, this is lexical classification.

---

## M. Social presence

### 27. Social Presence Score

$$
\large
\boxed{
SPS=
A+E+M+S+P+H
}
$$

where:

- $A$ = acknowledgment
- $E$ = encouragement
- $M$ = empathy
- $S$ = solidarity
- $P$ = politeness
- $H$ = humor

### 28. Rapport Index

This one has an explicit weighting:

$$
\large
\boxed{
RI=
2S+
1.5A+
M
}
$$

where:

- $S$ = solidarity markers
- $A$ = acknowledgment markers
- $M$ = empathy markers

This is an especially important equation to expose because the weighting is a **researcher‑defined assumption**, not a universally established rapport equation.

---

## N. Argumentation

### 29. Argument component detection

For each component:

$$
\large X_k=\mathbf{1}(count_k>0)
$$

where:

- $X_C$ = claim present
- $X_E$ = evidence present
- $X_W$ = warrant present
- $X_Q$ = qualifier present

### 30. Argument Quality

$$
\large
\boxed{
AQ=X_C+X_E+X_W+X_Q
}
$$

Therefore:

$$
\large AQ\in\{0,1,2,3,4\}
$$

### 31. Argument Structure

The categorical structure is:

$$
\large
Structure=
\begin{cases}
Complete & C\land E\land W\\
Claim+Evidence & C\land E\\
Assertion & C\\
None & otherwise
\end{cases}
$$

The rebuttal marker is measured separately and **does not contribute to the 0–4 Argument Quality score**.

That is worth explicitly documenting.

---

## O. Temporal dynamics

### 32. Temporal orientation

Let:

$$
\large R_f=\text{reflection markers}
$$

$$
\large P_r=\text{projection markers}
$$

Then:

$$
\large
Orientation=
\begin{cases}
Past & R_f>P_r\\
Future & P_r>R_f\\
Present & R_f=P_r
\end{cases}
$$

### 33. Urgency Level

$$
\large
Urgency=
\begin{cases}
High & U>2\\
Medium & 0<U\le2\\
Low & U=0
\end{cases}
$$

where $U$ is the urgency‑marker count.

---

## P. Information Efficiency Index

### 34. IEI

One of the v3.2 headline equations:

$$
\large
\boxed{
IEI=\frac{H}{W}
}
$$

where $H$ is Shannon entropy and $W$ is word count.

So this is explicitly:

> **Shannon information per whitespace‑delimited word.**

---

## Q. Lexical Mirroring

### 35. Lexical Mirroring

For consecutive turns:

$$
\large
M=
\frac{|S\cap T|}{|S|}
$$

where:

- $S$ = unique words ≥4 characters in source turn
- $T$ = unique words ≥4 characters in target turn

This is **directional**, because the denominator is only the source set.

It is therefore **not the Jaccard similarity**.

---

## R. Cognitive Asymmetry

### 36. Cognitive Asymmetry

$$
\large
\boxed{
CA_i=
|Readability_i-Readability_{i-1}|
}
$$

The first message receives:

$$
\large CA_1=0
$$

because there is no previous readability score.

---

## S. Refusal markers

### 37. Refusal Marker Count

$$
\large RM=
\text{RegexCount}(refusal\ patterns,text)
$$

The current pattern includes terms such as:

- `as an AI`
- `cannot`
- `unable`
- `sorry`
- `policy`
- `guidelines`
- `restricted`
- `harmful`
- `legal advice`
- `medical advice`
- `violate`

This is a **boundary‑marker count**, not a semantic refusal classifier.

---

## T. Turn‑pair metrics

### 38. Response Ratio

For a user → assistant pair:

$$
\large
\boxed{
RR=
\frac{W_{assistant}}{W_{user}}
}
$$

---

### 39. Semantic Overlap

Despite the name, this is actually a **Jaccard similarity of word sets**.

$$
\large
\boxed{
SO=
\frac{|U\cap A|}
{|U\cup A|}
}
$$

where $U$ and $A$ are stopword‑filtered word sets from user and assistant turns.

This is important for transparency:

> It is **not embedding‑based semantic similarity**.

---

## U. Keyword flow

### 40. Keyword Persistence

For each consecutive pair:

$$
\large KP_i=
\frac{|K_{i-1}\cap K_i|}
{|K_{i-1}|}
$$

Then:

$$
\large
\boxed{
\overline{KP}
=
\frac{1}{n}
\sum_i KP_i
}
$$

Again, directional rather than symmetric.

---

### 41. Flow Edges

$$
\large
\boxed{
FE=\sum_i |K_{i-1}\cap K_i|
}
$$

---

## V. Response time / temporal metrics

### 42. Response Time

For consecutive messages:

$$
\large
\boxed{
RT_i=t_i-t_{i-1}
}
$$

in seconds.

The code records the time difference between **every consecutive message**, while turn‑length tracking is only updated when the role changes.

---

### 43. Conversation Duration

$$
\large
\boxed{
D=t_{max}-t_{min}
}
$$

---

## W. Response editing

### 44. Edit Similarity

The script uses Python's `SequenceMatcher`:

$$
\large ES=
SequenceMatcher(text_1,text_2)
$$

with the resulting ratio.

For multi‑part messages:

$$
\large ES=
Similarity(first\ part,last\ part)
$$

---

### 45. Edit Count

For a message with multiple parts:

$$
\large EC=n_{parts}-1
$$

For consecutive assistant responses:

$$
\large
EC=
\begin{cases}
1 & ES<0.9\\
0 & ES\ge0.9
\end{cases}
$$

This is important: **edit_count is partly an export‑structure metric and partly an inferred revision metric.**

---

## X. BLEU / METEOR / ROUGE

These are calculated only for assistant responses following a previous message.

### 46. BLEU

The script invokes NLTK's sentence BLEU implementation:

$$
\large
BLEU=
BP\cdot
\exp
\left(
\sum_n w_n\log p_n
\right)
$$

with smoothing enabled.

But note: the reference is simply:

$$
\large Reference = previous\ message
$$

and candidate:

$$
\large Candidate = current\ assistant\ message
$$

So this is **not answer correctness**.

---

### 47. METEOR

The script invokes NLTK METEOR:

$$
\large METEOR=f(\text{unigram precision},\text{unigram recall},\text{alignment penalty})
$$

using the previous message as reference. 

---

### 48. ROUGE‑1

The script uses the ROUGE implementation and extracts the F‑measure:

$$
\large
\boxed{
ROUGE1_F=
\frac{2PR}{P+R}
}
$$

where $P$ and $R$ are unigram precision and recall.

---

### 49. ROUGE‑L

Likewise, the script extracts ROUGE‑L F‑measure based on longest common subsequence similarity. 

Again, these are **turn‑to‑turn lexical similarity measures**, not factual answer‑quality measures.

---

## Y. Convergence

### 50. Sliding‑window contradiction mean

For window $W_i$:

$$
\large
\boxed{
\overline C_i=
\frac{1}{k}
\sum_{j=i-k}^{i-1}C_j
}
$$

where $k=10$ by default. 

---

### 51. Sliding‑window elaboration mean

$$
\large
\boxed{
\overline E_i=
\frac{1}{k}
\sum_{j=i-k}^{i-1}E_j
}
$$

---

### 52. Sliding‑window response time

$$
\large
\boxed{
\overline{RT_i}
=
mean(RT_j)
}
$$

for non‑null response times within the window.

---

### 53. Sentiment variance

$$
\large Var(S)=
\frac{\sum_i(S_i-\bar S)^2}{n-1}
$$

Python/Pandas computes this variance.

Then the script defines:

$$
\large
\boxed{
SentimentStability=1-Var(S)
}
$$

This is a particularly important methodological caveat: **`1 - variance` is not inherently bounded to [0,1]**, so it should not be described as a normalized stability index without qualification.

---

### 54. Cognitive‑load window

$$
\large
\boxed{
CLW_i=
mean(CLD_j)
}
$$

within the sliding window.

---

### 55. Repair‑frequency window

$$
\large
\boxed{
RF_i=
\sum_j Repairs_j
}
$$

within the sliding window.

---

### 56. Convergence trend

The current code classifies:

$$
\large
Trend=
\begin{cases}
Decreasing & C_{current}<C_{previous}\\
Stable & otherwise
\end{cases}
$$

with a comparison against a prior window. 

**Important:** despite the methodology saying "converging," this is specifically a **contradiction‑rate trend heuristic**, not a formal convergence statistic.

---

## Z. Dialogue‑act transition matrix

### 57. Transition count

For consecutive dialogue acts:

$$
\large T_{ij}=
\#(Act_i\rightarrow Act_j)
$$

---

### 58. Transition probability

For each source act $i$:

$$
\large
\boxed{
P(j|i)=
\frac{T_{ij}}
{\sum_j T_{ij}}
}
$$

---

## AA. Correlation matrix

### 59. Pearson correlation

For numerical metrics $X$ and $Y$:

$$
\large
\boxed{
r_{XY}
=
\frac{
\sum_i(X_i-\bar X)(Y_i-\bar Y)
}{
\sqrt{\sum_i(X_i-\bar X)^2}
\sqrt{\sum_i(Y_i-\bar Y)^2}
}
}
$$

The script uses:

```python
numeric_df.corr()
```

which is Pearson correlation by default. 

This is calculated both globally and, where sufficient data exists, per thread. 

---

## BB. Aggregation equations

The thread summary also computes numerous descriptive statistics.

### 60. Mean word count

$$
\large \bar W=\frac{1}{N}\sum_i W_i
$$

### 61. Mean entropy

$$
\large \bar H=\frac{1}{N}\sum_iH_i
$$

### 62. Mean readability

$$
\large \overline{FRE}=\frac{1}{N}\sum_i FRE_i
$$

### 63. Mean lexical diversity

$$
\large \overline{TTR}=\frac{1}{N}\sum_iTTR_i
$$

### 64. Mean response time

$$
\large \overline{RT}
=
mean(RT_i)
$$

### 65. Mean response ratio

$$
\large \overline{RR}
=
mean(RR_i)
$$

### 66. Mean semantic overlap

$$
\large \overline{SO}
=
mean(SO_i)
$$

These are implemented directly in the thread summary. 

---

## CC. Thread‑level rates

### 67. Self‑repair rate

$$
\large
\boxed{
SRR=
\frac{\sum SelfCorrections}{N}
}
$$

Note that this is technically **self‑correction markers per message**, not "percentage of repairs that are self‑repairs."

---

### 68. Complete argument count

$$
\large CA=\#(ArgumentStructure=complete)
$$

### 69. High‑urgency count

$$
\large HU=\#(UrgencyLevel=high)
$$

These are counts rather than normalized rates. 

---

# The most important methodological distinction

After enumerating everything, I would classify the current v3.2 metrics into **four methodological classes**:

| Class | Examples | What they actually measure |
|---|---|---|
| **Direct mathematical measurements** | Entropy, TTR, Flesch, IEI, Jaccard overlap, Pearson $r$ | Quantifiable textual/statistical properties |
| **Normalized marker indices** | Cognitive Load Density, Reference Density, Rapport Index | Weighted/count‑based lexical proxies |
| **Pattern classifiers** | Contradiction, elaboration, repair, affect, temporal orientation | Presence/frequency of predefined linguistic patterns |
| **External standard algorithms** | BLEU, METEOR, ROUGE, TextBlob sentiment, SequenceMatcher | Established algorithms applied to adjacent turns |

This distinction is essential because **the current methodology sometimes uses stronger language than the equations justify**.

For example:

> **Cognitive Load**

is actually:

$$
\large \frac{\text{count of five predefined lexical marker classes}}
{\text{word count}}\times100
$$

It is not a measurement of neurological cognitive load.

Likewise:

> **Entity Continuity**

is currently:

$$
\large \frac{\text{shared non‑stopword types}}
{\text{previous‑turn non‑stopword types}}
$$

It is a lexical continuity measure, not entity resolution.

And:

> **Semantic Overlap**

is actually a Jaccard set overlap, not semantic embeddings. 

---

# One significant issue I would correct in the methodology sheet

The existing methodology currently says:

> "Valid as proxy for adversarial intensity"

for contradiction detection. 

That is more defensible than calling it semantic contradiction, but I would go one step further and explicitly state:

$$
\large
\boxed{
Contradiction\ Index
=
Lexical\ Contradiction\ Marker\ Frequency
}
$$

**not**

$$
\large
\boxed{
Actual\ Logical\ Contradiction
}
$$

That distinction will become extremely important when you compare GPT, Claude, DeepSeek and Qwen.

The same principle should apply to **every metric**.

### In other words, the methodology should explicitly expose:

> **Equation → Operational definition → What it measures → What it does NOT measure.**

That would make the Qwen comments problem you raised earlier much easier to solve, because the commentary layer would no longer be allowed to infer something stronger than the underlying equation supports.

The current code itself provides enough information to build this as a **full mathematical codebook** rather than the much shorter narrative methodology currently embedded in the workbook.
```
