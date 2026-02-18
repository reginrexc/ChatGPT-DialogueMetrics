# LEGAL JUSTIFICATION FOR RCNM

## Research Commons Non-Monetization License

---

## PURPOSE OF THIS DOCUMENT

The [Declaration of Hope and Intent](DECLARATION.md) explains why RCNM was built. The [Principles](LICENSE-PRINCIPLES.md) explain how its architecture serves those motivations. This document provides the **legal arguments** supporting RCNM's enforceability—its doctrinal foundations, strategic design choices, and responses to anticipated challenges.

This is **advocacy**, not binding text. Courts may reject these arguments. But they are **coherent, grounded in existing law, and designed to maximize enforceability** of RCNM's core protections.

---

## PART I: FOUNDATIONAL DOCTRINES

### 1. CONTRACT LAW BASIS

#### 1.1 License as Unilateral Contract Offer

RCNM operates as a **unilateral contract offer**:

| Element | RCNM Implementation |
|---------|---------------------|
| Offer | Author makes Software available with stated terms |
| Acceptance | User obtains, uses, or modifies the Software |
| Consideration (Author) | Provision of Software and associated rights |
| Consideration (User) | Agreement to terms, attribution, share-alike compliance, and (in AI contexts) training value through interaction |

#### 1.2 Consideration in AI-Assisted Context

Traditional consideration is **bilateral exchange**. In AI-assisted production, consideration is **reciprocal and ongoing**:

- Author provides: Software, capabilities, outputs
- User provides: Attribution, share-alike release, **training data through interaction**

The user's prompts, corrections, and usage patterns **improve the model**. This is **not gratuitous**; it is **valuable consideration** that supports contract enforceability.

#### 1.3 Promissory Estoppel

Even if consideration is challenged, **promissory estoppel** may enforce RCNM terms:

- Author makes **clear and definite promise** (non-monetization, permanence)
- User **reasonably relies** on that promise (invests labor, builds dependencies)
- **Injustice** can be avoided only by enforcing the promise

Users who build projects on RCNM-licensed software **detrimentally rely** on its continued availability. Courts may enforce to prevent injustice.

---

### 2. COPYRIGHT DOCTRINE

#### 2.1 Scope of Protection

RCNM acknowledges copyright's **idea-expression distinction**:

| Protected | Not Protected |
|-----------|---------------|
| Specific code (expression) | Underlying ideas |
| Documentation (expression) | Methods, systems, processes |
| Creative arrangement | Functional requirements |

RCNM **does not claim** to expand copyright beyond statutory limits. It **supplements** copyright with **contractual restrictions** on what copyright permits but contract can limit.

#### 2.2 Contractual Supplementation

Copyright law **allows** owners to impose conditions beyond statutory rights:

- Copyright owner can license **narrowly** (only certain uses)
- Copyright owner can require **reciprocal obligations** (share-alike)
- Copyright owner can **waive** certain rights (irrevocability)

RCNM uses these **permissive features** of copyright law, not its **expansive** features.

#### 2.3 AI-Generated Content Status

Copyright status of AI-generated content is **unsettled**:

| Jurisdiction | Trend |
|--------------|-------|
| United States | Human authorship required; pure AI output likely uncopyrightable |
| European Union | AI-assisted works may have copyright in human creative choices |
| United Kingdom | Computer-generated works have 50-year protection |
| Other jurisdictions | Varying, evolving |

RCNM **grants permissions to the extent copyright exists**. If no copyright exists, RCNM operates as **public dedication with conditions**—a **conditional gift to the commons**.

---

### 3. MORAL RIGHTS (DROIT MORAL)

#### 3.1 Inalienable Rights

In many jurisdictions (EU, Latin America, parts of Asia), **moral rights** are:

- **Inalienable**: Cannot be transferred or waived
- **Perpetual**: Survive death and copyright transfer
- **Enforceable**: Protect integrity of the work

#### 3.2 RCNM's Invocation

RCNM explicitly invokes **right of integrity**:

&gt; "The Author invokes any applicable moral rights (droit moral) of integrity to prevent distortion, mutilation, or modification of the work that would violate the principles of non-monetization and commons-based access."

This provides **posthumous enforcement mechanism** in jurisdictions recognizing moral rights.

#### 3.3 Strategic Function

Even in jurisdictions **not** recognizing moral rights, the invocation:

- Signals **intent** for courts interpreting ambiguous terms
- Supports **contractual interpretation** favoring permanence
- Creates **evidentiary basis** for estoppel claims

---

## PART II: SPECIFIC MECHANISMS

### 4. IRREVOCABILITY AND POSTHUMOUS BINDING

#### 4.1 Irrevocability Under Contract Law

Licenses can be **irrevocable** if:

- Supported by **consideration** (present here)
- **Reliance** is induced and foreseeable (present here)
- No **public policy** violation (commons preservation is favored policy)

#### 4.2 Posthumous Binding Under Estate Law

Challenge: Heirs inherit property rights, including copyright.

Response:

| Mechanism | Function |
|-----------|----------|
| Moral rights invocation | Integrity right survives death, enforceable by estate or community |
| Constructive trust | License creates trust for commons benefit, limiting estate discretion |
| Evidence of intent | Clear documentation prevents heirs claiming author wanted change |

**Limitation**: In jurisdictions with **strong heir property rights** and **no moral rights**, posthumous binding may fail. RCNM mitigates through **multiplicity**—distributed copies persist regardless of heir actions.

#### 4.3 Pre-Death Amendment Window

The **conditional right to amend** (Section 4.4) strengthens irrevocability:

- Shows author **contemplated** change but **chose not to**
- Creates **procedural barrier** to impulsive change
- 15-day delay allows **community intervention**

---

### 5. PARENT-CHILD INDEPENDENCE AND ORPHAN MECHANISM

#### 5.1 Scope of Author Authority

Fundamental principle: **Author can only license what Author owns**.

| Author Owns | Author Does Not Own |
|-------------|---------------------|
| Original code, documentation | Third-party contributions |
| Original architectural choices | Child Repository modifications |
| Original creative expression | Derivative creative expression by others |

#### 5.2 Contractual Cannot-Bind-Third-Parties

General contract law: **contracts bind parties, not third parties**.

RCNM's orphan mechanism **does not** purport to bind third parties. It **recognizes** that:

- Child Repository creators **own their contributions**
- Author **never had authority** to re-license those contributions
- Upon Author's attempted re-licensing, Children **automatically** become independent (no new binding occurs; existing rights simply **become visible**)

#### 5.3 Anti-Assignment Principle

Contracts **personal to the parties** cannot be assigned without consent. RCNM argues:

- Child Repository relationships are **personal to the community**
- Author **cannot assign** what community members own
- Any purported assignment is **void** as to community contributions

---

### 6. STRUCTURAL FIXATION

#### 6.1 License Covenant Running With the Code

RCNM attempts to create a **covenant running with the Software**:

- **Touches and concerns** the Software (restricts use)
- **Related to** the Software (preserves commons status)
- **Runs with** the Software (binds subsequent possessors)

#### 6.2 Temporal Locking

Base structure is **fixed at moment of Child creation**:

- Subsequent parent license changes **cannot retroactively alter** past events
- Fixed structure is **severed** from parent's future authority
- This is **not** binding future action; it is **recognizing** past fixation

#### 6.3 Limitation: No Binding of Bona Fide Purchasers

If a third party **independently** reimplements structure without accessing RCNM-licensed code:

- **No contract formed**
- **No copyright infringement** (ideas not protected)
- RCNM **does not bind** them

**Acceptance**: RCNM does not prevent independent innovation. It prevents **extraction by those who accessed the commons**.

---

### 7. AI FAIR USE SHIELD

#### 7.1 The Conditional Consent Doctrine

Core argument: AI model holders face **impossible choice**:

| Position | Training Data | Output Claims |
|----------|-------------|-------------|
| A: Consent required | Must obtain explicit authorization | **Cannot claim outputs** (no valid training base) |
| B: Fair use permitted | Fair use permits unconsented training | **Cannot claim outputs** (reciprocal fair use) |

**Either way, output claims fail.**

#### 7.2 Reciprocal Fair Use

If model holder relies on **fair use** for training:

- Fair use is **permissive**, not **proprietary**
- Fair use **does not generate ownership rights**
- User's **transformative use** of outputs is equally fair

**Parity is mandatory**, not optional.

#### 7.3 Unconscionability

Retroactive output claims are **unconscionable**:

- Model holder **retains benefit**: user training contributions
- Model holder **denies exchange**: unencumbered outputs
- **Inequality of bargaining power**: individual user vs. corporate platform
- **Surprise**: Terms of Service silent on output ownership

#### 7.4 Promissory Estoppel in AI Context

- Model holder **promises** general access with implied output freedom
- User **relies** on this promise (invests labor, builds projects)
- Model holder **attempts to retract** promise through patent claims
- **Injustice** can be avoided only by enforcing implied promise

---

## PART III: COMPARATIVE ANALYSIS

### 8. WHY EXISTING LICENSES ARE INSUFFICIENT

#### 8.1 Permissive Licenses (MIT, Apache, BSD)

| Feature | RCNM Advantage |
|---------|---------------|
| Allow commercial sale | RCNM prohibits |
| Permit proprietary derivatives | RCNM mandates share-alike |
| Enable institutional capture | RCNM resists through irrevocability |

#### 8.2 Copyleft Licenses (GPL, AGPL)

| Feature | RCNM Advantage |
|---------|---------------|
| Allow commercial sale (with source) | RCNM prohibits sale entirely |
| Permit "support" monetization | RCNM prohibits tool monetization |
| Allow private modifications | RCNM mandates public release |
| Do not protect logical structure | RCNM attempts contractual protection |

#### 8.3 Non-Commercial Licenses (CC BY-NC)

| Feature | RCNM Advantage |
|---------|---------------|
| Prohibit all commercial use | RCNM permits commercial use, prohibits sale |
| Too restrictive for adoption | RCNM balances access and protection |

---

## PART IV: ANTICIPATED CHALLENGES AND RESPONSES

### 9. "UNENFORCEABLE AMBIGUITY"

**Challenge**: Terms like "logical structure" and "monetization" are vague; courts reject ambiguous licenses.

**Response**:

- **Contextual interpretation**: Examples provided (Section 14.3) create interpretive framework
- **Good faith presumption**: Community governance resolves edge cases
- **Strategic function**: Ambiguity deters risk-averse actors even if litigated uncertainty exists

### 10. "OVERREACHING COPYRIGHT"

**Challenge**: RCNM claims control beyond copyright's scope.

**Response**:

- **Contractual, not copyright**: "Logical structure" protection is **contractual waiver**, not copyright claim
- **User voluntarily agrees**: Those who reject terms do not use Software
- **Copyright minimalism**: RCNM grants only permissions copyright allows; additional restrictions are contractual

### 11. "NO CONSIDERATION"

**Challenge**: Users give nothing of value; license is gratuitous and revocable.

**Response**:

- **Training data as consideration**: User interactions improve AI systems
- **Reliance as substitute**: Promissory estoppel if consideration fails
- **Network effects**: User adoption creates value for all participants

### 12. "PUBLIC POLICY AGAINST RESTRAINT"

**Challenge**: Irrevocability and posthumous binding violate public policy favoring alienability.

**Response**:

- **Commons preservation is favored policy**: Courts protect charitable trusts, public dedications
- **Limited scope**: Applies only to specific AI-assisted works, not all property
- **Temporal limitation**: Posthumous binding ends when copyright expires

---

## PART V: ENFORCEMENT STRATEGY

### 13. LAYERED ENFORCEMENT PRIORITY

| Priority | Mechanism | Goal |
|----------|-----------|------|
| 1 | Technical | Persistence through forking, cryptography, distribution |
| 2 | Social | Compliance through reputation, community norms |
| 3 | Contractual | Enforcement through agreement interpretation |
| 4 | Copyright | Last-resort litigation for egregious violations |

### 14. DEFENSIVE LITIGATION

RCNM is designed for **defensive** use:

- **Affirmative defense**: Against patent/copyright claims by model holders
- **Declaratory judgment**: Establishing freedom to operate
- **Counterclaim**: For bad faith litigation by extractors

**Not designed for**: Aggressive enforcement against independent innovators.

---

## CONCLUSION: AN EXPERIMENT IN LEGAL ARCHITECTURE

RCNM is **not doctrinally conservative**. It stretches contract law, invokes moral rights, and creates novel mechanisms (orphan status, structural fixation). It accepts **uncertainty** in exchange for **alignment with its goals**.

These arguments are **coherent enough to be litigated**, **novel enough to establish precedent**, and **grounded enough to survive dismissal**. They will not win every case. They will **deter many violations**, **persuade some courts**, and **demonstrate that alternatives are possible**.

The goal is not **perfect enforceability**. It is **sufficient enforceability** to protect the commons while demonstrating that **legal architecture can serve values beyond enclosure**.

Read the [Declaration](DECLARATION.md) for the human motivation.
Read the [Principles](LICENSE-PRINCIPLES.md) for the architectural logic.
Read the [Legal Text](LICENSE-FULL.md) for the operative terms.

Then decide if this experiment is worth joining.

---

**Research Commons Non-Monetization License**
**Version 1.0 | February 2026**
