# ChatGPT-DialogueMetrics

A comprehensive multi-dimensional analysis tool for studying extended human-AI dialogues, developed through cross-model collaboration.

---

## Overview

ChatGpt-DialogueMetrics analyzes ChatGPT conversation exports to extract 86+ metrics across cognitive, epistemic, emotional, social, and relational dimensions. The tool enables researchers, students, and independent learners to gain quantitative insights into their dialogue patterns with AI systems.

### What It Does

- Analyzes extended AI dialogue conversations (JSON format)
- Computes 86+ comprehensive metrics
- Generates Excel reports with multiple analysis sheets
- Measures cognitive load, sentiment, argumentation, and more
- Requires only basic hardware (4GB RAM sufficient)
- Completely free and open-source

---

## Development Model: Cross-AI Collaboration

### Collaborative Architecture

This tool emerged through a unique cross-model development process where each AI system contributed distinct analytical perspectives. The development involved **five AI systems** and **one human participant**, each playing separate but complementary roles.

### Role Distribution

#### AI Contributions (Technical Implementation)

**ChatGPT (OpenAI) - Foundation Layer (v1.0)**
- Base architecture and code structure
- 23 foundation metrics (dialogue mechanics, quality scores)
- Initial pattern detection framework
- Excel output implementation
- Contribution: ~30% of metrics, 100% of initial structure

**Claude (Anthropic) - Epistemic Enhancement (v2.0)**
- 5-type contradiction taxonomy (negation, adversative, correction, disagreement, limitation)
- 5-type elaboration classification
- Epistemic stance measurement (hedges vs confidence markers)
- Turn-pair analysis between messages
- Convergence detection algorithms
- Contribution: +6 metrics, epistemic depth layer

**Kimi (Moonshot AI) - Cognitive-Social Expansion (v3.0)**
- Cognitive load indicators (abstraction, metacognition, complexity)
- Affective trajectory tracking (curiosity, confusion, satisfaction, frustration)
- Conversational repair patterns
- Knowledge construction markers
- Social presence and rapport indicators
- Argument structure analysis (claims, evidence, warrants, rebuttals)
- Contribution: +57 metrics, holistic experience layer

**DeepSeek (DeepSeek AI) - Systematic Organization (v3.1)**
- Code architecture refinement
- Theoretical framework categorization
- Clean modular structure
- 8-domain organizational system
- Documentation enhancement
- Contribution: Structural coherence, systematic organization

**Gemini (Google DeepMind) - Relational Dynamics (v3.2)**
- Information Efficiency Index (entropy per word)
- Lexical mirroring (syntactic alignment)
- Cognitive asymmetry measurement
- System boundary detection (refusal markers)
- Contribution: Coupling metrics, interaction dynamics

#### Human Contribution (Cross-Model Integration)

**The User's Role: Bridge Between AI Systems**

Rather than orchestrating or directing development, the user functioned as:

1. **Problem Identifier**
   - Recognized need for comprehensive dialogue analysis
   - Identified gap in accessible measurement tools
   - Defined practical use case (analyzing own research dialogues)

2. **Cross-Model Integrator**
   - Brought code from ChatGPT to Claude for review
   - Carried enhanced version from Claude to Kimi
   - Connected Kimi's expansion to DeepSeek for organization
   - Linked DeepSeek's structure to Gemini for coupling metrics
   - Served as communication channel between otherwise isolated systems

3. **Quality Validator**
   - Tested code on real dialogue data (2,557 messages, 52 days)
   - Verified metrics produced meaningful outputs
   - Identified usability issues (Excel navigation, performance)
   - Confirmed functionality across iterations

4. **Design Decision Maker**
   - Chose modular architecture (enable/disable metrics)
   - Set accessibility constraints (4GB RAM maximum)
   - Decided against feature creep (computational efficiency)
   - Determined output format (Excel with multiple sheets)
   - Planned chunking strategy for large files

5. **Documentation Contributor**
   - Transparent process documentation
   - Usage guidelines creation
   - Sample data preparation (privacy-preserving)
   - Installation script requirements

**Contribution Summary:**
- System design decisions: ~20% of value
- Cross-model integration: Essential bridging function
- Quality validation: Real-world testing
- Technical implementation: 0% (all AI-generated)
- Metric definitions: 0% (from existing research literature)

### Why This Model Matters

**Not a Traditional Development Process:**
- Not: One developer coding from specifications
- Not: Team of human programmers dividing tasks
- Not: AI assistant helping single human programmer
- But: Multiple AI systems contributing autonomous expertise

**Cross-Model Advantages:**
1. **Perspective Diversity** - Each AI brought different analytical frameworks
2. **Expertise Integration** - Combined strengths without requiring human expertise
3. **Rapid Development** - Weeks instead of months or years
4. **Accessibility** - No programming background needed to initiate
5. **Transparency** - All AI contributions documented and attributable

**Human Role Was Essential But Different:**
- Not coding expertise (AI provided implementation)
- Not domain expertise (AI provided metric frameworks)
- But: Integration function (connecting isolated AI systems)
- And: Quality judgment (testing on real data)
- And: Design decisions (accessibility, modularity, constraints)

### Implications

This development model demonstrates:
- AI systems can contribute complementary expertise when bridged
- Non-experts can facilitate cross-model development
- Quality tools can emerge from collaborative AI processes
- Human contribution shifts from implementation to integration
- Transparency about roles strengthens rather than weakens credibility

---

## Features

### Comprehensive Metrics (86+)

**Dialogue Mechanics (ChatGPT Layer)**
- Word count, token count, sentence count
- Response time, edit patterns
- Basic quality scores (BLEU, METEOR, ROUGE)
- Entropy and readability

**Epistemic Structure (Claude Layer)**
- 5-type contradiction detection
- 5-type elaboration patterns
- Epistemic stance (hedges vs confidence)
- Turn-pair interaction analysis
- Convergence trajectory

**Cognitive-Social-Emotional (Kimi Layer)**
- Cognitive load indicators (4 types)
- Affective states (6 dimensions)
- Repair mechanisms (5 patterns)
- Knowledge construction (5 markers)
- Social presence (8 indicators)
- Argument structure (7 components)

**Relational Dynamics (Gemini Layer)**
- Information efficiency (entropy/word)
- Lexical mirroring (vocabulary alignment)
- Cognitive asymmetry (load distribution)
- System boundaries (refusal detection)

### Modular Design

- **Enable/Disable Metrics:** Users can activate only needed measurements
- **Extensible Structure:** Others can add custom metrics
- **Clean Architecture:** Well-organized code for modification
- **Documented Patterns:** Clear pattern libraries for understanding

### Accessibility Focus

**Hardware Requirements:**
- RAM: 4GB recommended (2GB minimum)
- CPU: Any dual-core processor (2015+)
- Storage: 500MB for tool and dependencies
- OS: Windows, macOS, or Linux

**Cost:**
- Software: $0 (completely free)
- Dependencies: $0 (all open-source)
- Development: $0 (free-tier AI used)
- Total: $0

**Performance:**
- 8MB JSON file: 2-5 minutes processing
- Memory usage: 400-700MB
- Runs on 7-year-old laptops
- No GPU or specialized hardware needed

### Output Format

**Excel Workbook with Multiple Sheets:**
1. **Message-Level Analysis:** All metrics per message
2. **Summary Statistics:** Aggregate patterns
3. **Correlation Matrix:** Relationships between metrics
4. **Trajectory Analysis:** Evolution over time
5. **User vs Assistant:** Comparative patterns

**Easy to interpret:**
- Hyperlinked navigation
- Frozen header rows
- Color-coded sections
- Clear column labels

---

## Installation

### Quick Start

Choose your platform:

**Linux/macOS:**
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

**Windows:**
```cmd
install_dependencies.bat
```

**Cross-Platform (Python):**
```bash
python3 install_dependencies.py
```

**Manual (pip):**
```bash
pip install -r requirements.txt
```

See `INSTALLATION.md` for detailed instructions, troubleshooting, and virtual environment setup.

---

## Usage

### Basic Workflow

1. **Export Your ChatGPT Conversation**
   - Go to ChatGPT Settings → Data Controls → Export Data
   - Download the `conversations.json` file
   - Place in the same directory as the script

2. **Run Analysis**
   ```bash
   python3 chat_analysis.py
   ```

3. **Review Results**
   - Open generated Excel file
   - Explore metrics across sheets
   - Interpret patterns in your dialogue

### For Large Files

If your JSON file is very large (>50MB):

1. Use the chunking utility (if provided)
2. Process chunks individually
3. Aggregate results

See documentation for large file handling.

### Customization

**Disable Unwanted Metrics:**
- Edit script to comment out metric groups
- Reduces processing time
- Simplifies output

**Add Custom Metrics:**
- Follow existing pattern structure
- Add to appropriate category
- Document for reproducibility

---

## Sample Data

### Available Samples

This repository includes **stripped sample data** showing output format:
- Correlation matrices
- Metric structures
- Sheet organization
- Value ranges

**Important:** Sample data has all conversation content removed for privacy.

### Using Sample Data

✓ **Allowed:** Learning tool format, understanding metrics, evaluating utility
✗ **Requires Permission:** Research use, publication, redistribution

See `DATA_README.md` for complete usage terms and permission process.

### Generate Your Own Data

For research or analysis:
1. Export your own ChatGPT conversations
2. Run this tool on your data
3. Full context and content available
4. No privacy concerns (your own data)
5. Freely publishable (your intellectual property)

---

## Research Applications

### Who Should Use This Tool

**Independent Researchers:**
- No institutional access needed
- No expensive software required
- Analyze your own research dialogues
- Build evidence for your work

**Graduate Students:**
- Study AI-assisted research processes
- Analyze learning patterns
- Track cognitive development
- Document methodology

**Educators:**
- Understand student-AI interactions
- Evaluate AI tutoring effectiveness
- Research learning patterns
- Improve pedagogical approaches

**Anyone Curious:**
- Understand how you think with AI
- Discover your dialogue patterns
- Learn through self-examination
- Quantify collaboration quality

### Research Questions Enabled

- How does cognitive load evolve during extended AI collaboration?
- What affective patterns predict sustained engagement?
- How do contradictions and elaborations balance in productive dialogue?
- What distinguishes successful from unsuccessful AI-assisted research?
- How does epistemic stance shift as understanding develops?
- What social dynamics enable intense intellectual challenge?

---

## Limitations and Scope

### What This Tool Does

✓ Measures linguistic patterns in dialogue
✓ Quantifies structural features
✓ Tracks metrics across conversations
✓ Reveals behavioral patterns

### What This Tool Does NOT Do

✗ Measure semantic truth or accuracy
✗ Validate theoretical correctness
✗ Determine quality of ideas
✗ Replace expert judgment
✗ Understand deep meaning

### Appropriate Use

**Good for:**
- Studying dialogue patterns
- Comparing across conversations
- Tracking changes over time
- Self-examination and learning
- Methodology research

**Not good for:**
- Determining correctness of content
- Evaluating argument validity
- Making truth claims
- Replacing domain expertise

---

## Technical Details

### Dependencies

- Python 3.8+
- numpy, pandas
- openpyxl, xlsxwriter
- textblob, nltk
- rouge-score
- tiktoken

See `requirements.txt` for versions.

### Architecture

**Modular Design:**
- Pattern libraries (regex-based detection)
- Metric computation functions
- Data aggregation layer
- Output generation (Excel)

**Performance:**
- Single-pass processing where possible
- Efficient pattern matching
- Memory-conscious design
- Scalable to large conversations

### Code Quality

- Research-grade implementation
- Comprehensive pattern libraries
- Error handling throughout
- Documented metric definitions
- Clean, readable structure

---

## Contributing

### Ways to Contribute

1. **Use and Provide Feedback**
   - Test on your conversations
   - Report bugs or issues
   - Suggest improvements
   - Share use cases

2. **Add Metrics**
   - Propose new measurements
   - Implement additional patterns
   - Document theoretical basis
   - Submit pull requests

3. **Improve Documentation**
   - Clarify instructions
   - Add examples
   - Translate to other languages
   - Create tutorials

4. **Share Results**
   - Publish research using this tool
   - Cite properly
   - Share findings with community
   - Contribute to methodology development

### Contribution Guidelines

- Maintain modular structure
- Document all additions
- Respect accessibility constraints (no high-end hardware requirements)
- Follow existing code style
- Provide clear commit messages

---

## Citation

### How to Cite This Tool

**Academic Papers:**
```
[Regin Rex]. (2024). ChatGpt-DialogueMetrics 
A multi-AI collaborative dialogue analysis tool. 
Retrieved from [repository URL]
```

**Attribution of AI Contributions:**
```
Tool developed through cross-model collaboration:
- ChatGPT (OpenAI): Foundation architecture
- Claude (Anthropic): Epistemic enhancements
- Kimi (Moonshot AI): Cognitive-social expansion
- DeepSeek (DeepSeek AI): Systematic organization
- Gemini (Google DeepMind): Relational dynamics
Human integration: [Regin Rex]
```

### Citing Specific Metrics

When using particular metric families:

**Epistemic metrics:** "Epistemic analysis using Claude-contributed enhancements to ChatGpt-DialogueMetrics tool..."
**Cognitive metrics:** "Cognitive load patterns measured via Kimi-contributed metrics in ChatGpt-DialogueMetrics..."
**Coupling metrics:** "Interaction dynamics assessed through Gemini-contributed coupling metrics..."

---

## License

**MIT License**

The tool is completely open-source and free to use, modify, and distribute.

**Note on Sample Data:**
The tool code is MIT licensed (unrestricted use).
Sample data has separate usage terms (see DATA_README.md).

---

## Acknowledgments

### AI System Contributions

- **ChatGPT** (OpenAI): Foundation and architecture
- **Claude** (Anthropic): Epistemic depth
- **Kimi** (Moonshot AI): Holistic expansion
- **DeepSeek** (DeepSeek AI): Systematic organization
- **Gemini** (Google DeepMind): Relational dynamics

### Theoretical Foundations

Metrics based on established research in:
- Cognitive psychology (cognitive load theory)
- Epistemology (knowledge construction)
- Discourse analysis (conversation patterns)
- Argumentation theory (structured reasoning)
- Affective science (emotion in cognition)

### Development Model

This tool demonstrates a novel development paradigm:
- Cross-model AI collaboration
- Human as integration bridge
- Distributed expertise contribution
- Transparent role attribution
- Open-source result

---

## Support and Contact

### Documentation

- `README.md` - This overview
- `INSTALLATION.md` - Setup instructions
- `DATA_README.md` - Sample data and usage terms
- `METRICS.md` - Detailed metric definitions (if available)

### Getting Help

**Technical Issues:**
- Check INSTALLATION.md for troubleshooting
- Review error messages carefully
- Try in fresh virtual environment
- Create GitHub issue with details

**Usage Questions:**
- See documentation files
- Review sample outputs
- Test on small conversation first
- Ask in GitHub discussions

**Research Collaboration:**
- Create issue for research proposals
- Discuss methodology applications
- Share findings and insights

### Contributing Back

Found this useful? Consider:
- ⭐ Star the repository
- 📢 Share with others
- 📝 Cite in your work
- 🐛 Report bugs
- 💡 Suggest improvements
- 🤝 Collaborate on research

---

## Project Status

**Current Version:** 3.2

**Status:** Stable, actively maintained

**Tested On:**
- Multiple extended dialogues (500-2500 messages)
- Various conversation types (research, learning, creative)
- Different hardware configurations (2GB-16GB RAM)
- Multiple operating systems (Windows, macOS, Linux)

**Roadmap:**
- Additional AI platform support (Claude, Gemini JSON formats)
- Enhanced visualization options
- Web interface (potential future)
- Community-contributed metrics
- Multi-language support

---

## Philosophy

### Why This Tool Exists

**Problem:** Researchers lack accessible tools for analyzing extended AI dialogues

**Solution:** Free, comprehensive, hardware-accessible analysis tool

**Approach:** Multi-AI collaboration brings diverse perspectives without requiring human expertise in each domain

**Goal:** Enable anyone to understand their AI collaboration patterns through quantitative measurement

### Design Principles

1. **Accessibility:** Runs on basic hardware, costs nothing
2. **Transparency:** Open source, documented processes, clear attributions
3. **Modularity:** Users control what they measure
4. **Comprehensiveness:** 86+ metrics across multiple dimensions
5. **Practicality:** Real-world tested, actually useful output

### Ethical Commitments

- **Privacy:** Sample data stripped, usage terms clear
- **Attribution:** AI contributions explicitly credited
- **Openness:** Tool freely available, encourage derivatives
- **Honesty:** Limitations acknowledged, no overclaiming
- **Respect:** Existing research properly foundational

---

**ChatGpt-DialogueMetrics: Making dialogue patterns visible through collaborative AI measurement**

*"Understanding how we think with AI, one conversation at a time."*

---

*Last updated: February 16, 2026*
*Version: 3.2*
*Repository: *
