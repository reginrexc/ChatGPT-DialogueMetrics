# CONTRIBUTING TO ChatGPT-DialogueMetrics

Thank you for your interest in contributing to this project. This document provides guidelines for contributing code, documentation, and ideas to ChatGPT-DialogueMetrics.

---

## TABLE OF CONTENTS

1. [Before You Contribute](#before-you-contribute)
2. [Code of Conduct](#code-of-conduct)
3. [How to Contribute](#how-to-contribute)
4. [Development Guidelines](#development-guidelines)
5. [Documentation Guidelines](#documentation-guidelines)
6. [Pull Request Process](#pull-request-process)
7. [Licensing and Attribution](#licensing-and-attribution)
8. [Questions and Support](#questions-and-support)

---

## BEFORE YOU CONTRIBUTE

### Understanding the License

This project is licensed under the **Research Commons Non-Monetization License (RCNM) v1.0**.

**What this means for contributors:**

✓ **You MAY:**
- Use the tool for research, analysis, and commercial operations
- Modify and improve the code
- Create derivative tools
- Distribute copies and modified versions
- Contribute improvements back to the project

✗ **You MUST NOT:**
- Sell the software itself as a product
- Place it behind paywalls
- Create proprietary versions that restrict access

✓ **You MUST:**
- Release all modifications publicly under RCNM
- Attribute original authors and AI collaborators
- Register derivative tools with this repository
- Share improvements with the community

**By contributing, you agree that your contributions will be licensed under RCNM v1.0.**

Read the full license: [License/LICENSE.md](License/LICENSE.md)

---

### The Project's Philosophy

This project embodies principles of:

1. **Commons-based creation**: Tools built with AI assistance belong to the commons
2. **Transparent collaboration**: Multi-AI development documented openly
3. **Long-term thinking**: Code that outlives its creators
4. **Epistemic discipline**: Facts labeled, speculation acknowledged, sources cited

**Before contributing, ask yourself:**
- Does my contribution align with commons-preservation values?
- Am I willing to share improvements publicly?
- Can I document my work transparently?

If yes, read on. If no, this may not be the right project for you.

---

## CODE OF CONDUCT

### Core Principles

**Be Respectful**
- Treat all contributors with dignity
- Welcome diverse perspectives
- Disagree constructively

**Be Honest**
- Acknowledge sources (human or AI)
- Label speculation clearly
- Admit when you don't know

**Be Patient**
- This is a volunteer project
- Reviews take time
- Iteration is expected

**Be Constructive**
- Critique work, not people
- Suggest improvements
- Help newcomers learn

### Unacceptable Behavior

- Personal attacks or harassment
- Claiming AI-generated work as solely yours without disclosure
- Dismissing contributions based on tooling used
- Deliberately introducing vulnerabilities
- Violating RCNM license terms

**Violations:** Contact maintainers. Serious or repeated violations may result in ban from contributing.

---

## HOW TO CONTRIBUTE

### Types of Contributions

#### 1. Code Contributions
- Bug fixes
- New features (metrics, parsers, export formats)
- Performance improvements
- Test coverage
- Multi-model support

#### 2. Documentation Contributions
- README improvements
- Tutorial creation
- API documentation
- Use case examples
- Translations

#### 3. Research Contributions
- Academic validation of metrics
- Case studies
- Comparative analyses
- Theoretical frameworks

#### 4. Issue Reporting
- Bug reports
- Feature requests
- Use case descriptions
- Edge case identification

### Getting Started

#### Step 1: Check Existing Issues

Before starting work, check if someone else is already working on it:
- Browse [open issues](../../issues)
- Search [closed issues](../../issues?q=is%3Aissue+is%3Aclosed) for prior discussion
- Check [pull requests](../../pulls) for in-progress work

#### Step 2: Discuss First (For Large Changes)

For significant changes:
1. Open an issue describing your proposal
2. Wait for maintainer feedback
3. Discuss approach and scope
4. Get approval before investing time

**Why?** Prevents duplicate work, ensures alignment with project goals, avoids rejected PRs.

#### Step 3: Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/ChatGPT-DialogueMetrics.git
cd ChatGPT-DialogueMetrics
git remote add upstream https://github.com/reginrexc/ChatGPT-DialogueMetrics.git
```

#### Step 4: Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Naming conventions:**
- `feature/` - New functionality
- `fix/` - Bug fixes
- `docs/` - Documentation only
- `refactor/` - Code restructuring
- `test/` - Test additions

---

## DEVELOPMENT GUIDELINES

### Code Quality Standards

#### Python Code Style

Follow [PEP 8](https://pep8.org/) with these specifics:

```python
# Good: Clear variable names, type hints, docstrings
def calculate_entropy(text: str, normalize: bool = True) -> float:
    """
    Calculate Shannon entropy of text.
    
    Args:
        text: Input text string
        normalize: Whether to normalize by text length
        
    Returns:
        Entropy value as float
        
    Example:
        >>> calculate_entropy("hello world")
        3.1699250014423126
    """
    # Implementation here
    pass

# Bad: Unclear names, no types, no docs
def calc(t, n=True):
    # what does this do?
    pass
```

**Key requirements:**
- Type hints for function signatures
- Docstrings for all public functions
- Descriptive variable names
- Comments for complex logic only (code should be self-documenting)

#### Testing

All new features must include tests:

```python
# tests/test_metrics.py
import pytest
from dialogue_metrics import calculate_entropy

def test_entropy_basic():
    """Test entropy calculation on simple string."""
    text = "aaabbc"
    result = calculate_entropy(text)
    assert result > 0
    assert isinstance(result, float)

def test_entropy_empty():
    """Test entropy with empty string."""
    with pytest.raises(ValueError):
        calculate_entropy("")
```

**Test coverage expectations:**
- All new functions have tests
- Edge cases covered (empty input, invalid input, boundary conditions)
- Run tests before submitting PR: `pytest tests/`

#### Dependencies

**Before adding new dependencies:**
1. Check if functionality exists in current dependencies
2. Evaluate package maintenance status
3. Consider bundle size impact
4. Document in `requirements.txt` with version pin

```txt
# Good: Pinned versions with comments
numpy==1.24.3  # Array operations
pandas==2.0.1  # DataFrame handling

# Bad: Unpinned versions
numpy
pandas
```

### Performance Considerations

**This tool processes large conversation files. Keep performance in mind:**

```python
# Good: Generator for memory efficiency
def process_messages(messages: List[dict]):
    for msg in messages:
        yield calculate_metrics(msg)

# Bad: Loading everything into memory
def process_messages(messages: List[dict]):
    return [calculate_metrics(msg) for msg in messages]
```

**Optimization checklist:**
- Use generators for large datasets
- Cache expensive computations
- Profile before optimizing (don't guess)
- Document performance characteristics

### Backward Compatibility

**Maintain compatibility with existing workflows:**
- Don't break existing APIs without deprecation warnings
- Preserve output format unless major version bump
- Provide migration guides for breaking changes

---

## DOCUMENTATION GUIDELINES

### README Updates

When adding features, update README.md:

```markdown
## New Feature: Sentiment Analysis

Calculate sentiment scores for each message.

### Usage

\`\`\`python
from dialogue_metrics import analyze_sentiment

result = analyze_sentiment(conversation_data)
\`\`\`

### Output

Adds `sentiment` column with values -1.0 (negative) to 1.0 (positive).
```

### Code Comments

**Good comments explain WHY, not WHAT:**

```python
# Good: Explains reasoning
# Using Wilson score for confidence intervals instead of normal approximation
# because it handles small sample sizes better
confidence = wilson_score(successes, trials)

# Bad: Repeats what code says
# Calculate confidence score
confidence = wilson_score(successes, trials)
```

### Docstring Standards

Use Google-style docstrings:

```python
def add_metric(name: str, calculator: Callable, description: str = "") -> None:
    """
    Register a custom metric calculator.
    
    Args:
        name: Metric identifier (e.g., 'custom_entropy')
        calculator: Function that takes message dict, returns numeric value
        description: Optional human-readable description
        
    Raises:
        ValueError: If name already registered or calculator invalid
        
    Example:
        >>> def my_metric(msg):
        ...     return len(msg['content'])
        >>> add_metric('word_count', my_metric, 'Count words in message')
    """
```

### AI Assistance Disclosure

**If you used AI assistance (ChatGPT, Claude, Copilot, etc.) in your contribution:**

**In commit messages:**
```
Add sentiment analysis feature

- Implemented using VADER lexicon
- Added tests for edge cases
- Updated README with usage examples

AI assistance: ChatGPT helped structure the VADER integration
```

**In code comments (for substantial AI-generated sections):**
```python
# Sentiment analysis implementation
# Generated with ChatGPT assistance, reviewed and tested by [Your Name]
def analyze_sentiment(text: str) -> float:
    # ...
```

**Why disclose?**
- Intellectual honesty
- Aligns with project philosophy
- Helps others understand contribution process
- Not a requirement, but appreciated

---

## PULL REQUEST PROCESS

### Before Submitting

**Checklist:**
- [ ] Code follows style guidelines
- [ ] Tests added and passing (`pytest tests/`)
- [ ] Documentation updated (README, docstrings)
- [ ] Commit messages are clear
- [ ] Branch is up-to-date with main
- [ ] No merge conflicts
- [ ] AI assistance disclosed (if applicable)

### PR Title Format

```
Type: Brief description

Examples:
Feature: Add sentiment analysis metric
Fix: Correct entropy calculation for empty strings
Docs: Add tutorial for custom metrics
Refactor: Simplify message parsing logic
```

### PR Description Template

```markdown
## Description
Brief summary of changes and motivation.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (describe)

## Testing
Describe how you tested this:
- [ ] Added new tests
- [ ] All existing tests pass
- [ ] Manually tested on sample conversations

## AI Assistance
- [ ] No AI assistance used
- [ ] AI-assisted (specify tool): [ChatGPT/Claude/Copilot/Other]
- [ ] Assistance description: [Brief description]

## Related Issues
Fixes #123
Relates to #456

## Screenshots (if applicable)
[Add screenshots for UI/output changes]

## Checklist
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] Backward compatible (or migration guide provided)
```

### Review Process

**What to expect:**
1. **Automated checks:** Tests, linting run automatically
2. **Maintainer review:** May take 1-7 days depending on PR size
3. **Feedback:** Changes may be requested
4. **Iteration:** Make requested changes, push to same branch
5. **Approval:** Once approved, maintainer will merge

**Review criteria:**
- Code quality and style
- Test coverage
- Documentation completeness
- Alignment with project philosophy
- Backward compatibility
- Performance impact

### After Merge

- Your contribution will be credited in release notes
- Update CONTRIBUTORS.md will include your name
- Close related issues you opened

---

## LICENSING AND ATTRIBUTION

### Your Rights as Contributor

**By contributing, you:**
- Retain copyright to your contribution
- Grant RCNM license to the project
- Allow others to use, modify, and distribute under RCNM
- Cannot later claim contributions are proprietary

**You do NOT:**
- Transfer copyright to the project
- Lose ability to use your own code
- Give up attribution rights

### Attribution Requirements

**All contributions must include attribution:**

In CONTRIBUTORS.md:
```markdown
- [Your Name] (@your-github) - Feature description
```

In git commits:
```bash
git commit -m "Add feature X" --author="Your Name <your@email.com>"
```

**If using AI assistance:**
Document which AI contributed what (in commit messages or comments).

### Multi-AI Contributions

**If your contribution involved multiple AIs (ChatGPT, Claude, etc.):**

Document in PR description:
```markdown
## AI Collaboration

- ChatGPT: Initial code generation
- Claude: Error handling improvements
- Kimi: Documentation formalization
- User: Integration, testing, refinement
```

This transparency:
- Aligns with project values
- Helps others understand development process
- Provides attribution to AI tools

### Third-Party Code

**If incorporating code from other sources:**
1. Ensure license compatibility (must be RCNM-compatible)
2. Preserve original attribution
3. Document source in code comments
4. Add to THIRD_PARTY_NOTICES.md

```python
# Original code from: https://github.com/example/repo
# Author: Original Author
# License: MIT (compatible with RCNM)
# Modified by: Your Name for ChatGPT-DialogueMetrics
def borrowed_function():
    # ...
```

---

## QUESTIONS AND SUPPORT

### Where to Ask

**For different types of questions:**

| Question Type | Where to Ask |
|--------------|-------------|
| "How do I use this feature?" | [GitHub Discussions - Q&A](../../discussions) |
| "I found a bug" | [GitHub Issues](../../issues) |
| "Can we add this feature?" | [GitHub Discussions - Ideas](../../discussions) |
| "I need help contributing" | [GitHub Discussions - Help](../../discussions) |
| "Is this license compatible?" | [GitHub Issues with 'license' tag](../../issues) |

### Getting Help

**Before asking:**
1. Read relevant documentation (README, License docs)
2. Search existing issues and discussions
3. Try to reproduce the issue with minimal example

**When asking:**
- Provide context (what you're trying to do)
- Include error messages (if applicable)
- Share code snippets (if relevant)
- Specify versions (Python, dependencies)

**Response expectations:**
- Maintainers are volunteers
- Response time: 1-7 days typically
- Complex questions may take longer
- Patience appreciated

### Contributing to Documentation

Documentation improvements are especially welcome:

**High-value docs contributions:**
- Tutorial: "Your First Conversation Analysis"
- How-to guide: "Adding Custom Metrics"
- Use case example: "Analyzing Team Meetings"
- Troubleshooting guide: Common issues
- Translation: README in other languages

**Process same as code contributions:**
1. Fork repository
2. Make changes
3. Submit PR
4. Reference this guide for standards

---

## SPECIAL CONTRIBUTION TYPES

### Academic Contributions

**If you're a researcher validating metrics:**

We especially welcome:
- Peer-reviewed citations for existing metrics
- Validation studies
- Comparative analyses
- Theoretical frameworks

**How to contribute:**
1. Add citations to relevant code comments
2. Update METRICS.md documentation
3. Link to papers in PR description
4. Consider adding case study to `/examples/`

**Example:**
```python
def calculate_coherence(messages: List[str]) -> float:
    """
    Calculate conversation coherence using LSA.
    
    Academic validation:
    - Foltz, P. W. (1996). "Latent Semantic Analysis for text-based research."
      Behavior Research Methods, Instruments, & Computers, 28(2), 197-202.
    - Validated on n=500 conversations, r=0.73 with human ratings
    """
```

### Metric Proposals

**Proposing new metrics:**

1. Open issue with "metric-proposal" label
2. Describe:
   - What it measures
   - Why it's useful
   - Academic support (if any)
   - Computational cost
   - Example interpretation
3. Wait for feedback before implementing
4. If approved, submit PR with:
   - Implementation
   - Tests
   - Documentation
   - Example output

### Parser Extensions

**Supporting new conversation formats (Claude, Gemini, etc.):**

1. Create parser in `parsers/` directory:
   ```python
   # parsers/claude_parser.py
   def parse_claude_export(filepath: str) -> List[dict]:
       """Parse Claude conversation export to standard format."""
   ```

2. Add tests with example file
3. Update README with supported formats
4. Document format quirks

**Standard message format:**
```python
{
    'timestamp': '2024-01-01T12:00:00Z',
    'role': 'user',  # or 'assistant'
    'content': 'Message text',
    'agent': 'Claude',  # or 'ChatGPT', 'Human'
    'metadata': {}  # Optional
}
```

---

## VERSION CONTROL

### Commit Message Guidelines

**Format:**
```
Type: Brief description (50 chars max)

Longer explanation if needed (wrap at 72 chars).
Explain what and why, not how.

- Bullet points okay
- Reference issues: #123

AI assistance: [Tool name] (if applicable)
```

**Types:**
- `Feature:` - New functionality
- `Fix:` - Bug fixes
- `Docs:` - Documentation only
- `Test:` - Adding/updating tests
- `Refactor:` - Code restructuring
- `Style:` - Formatting changes
- `Chore:` - Maintenance tasks

**Examples:**
```
Feature: Add sentiment analysis metric

Implements VADER-based sentiment scoring for each message.
Useful for tracking emotional tone across conversations.

- Added vader_lexicon dependency
- Created sentiment.py module
- Added tests for edge cases

AI assistance: ChatGPT helped structure VADER integration
```

### Branch Strategy

**Main branches:**
- `main` - Stable, released code
- `develop` - Integration branch for next release

**Your branches:**
- `feature/your-feature` - New features
- `fix/bug-description` - Bug fixes

**Workflow:**
1. Branch from `main` for small fixes
2. Branch from `develop` for new features
3. PR targets `develop` (or `main` for hotfixes)
4. Maintainers merge `develop` → `main` for releases

---

## RELEASE PROCESS (Maintainers)

**For maintainers handling releases:**

### Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- `v1.0.0` → `v1.0.1` - Bug fixes
- `v1.0.0` → `v1.1.0` - New features (backward compatible)
- `v1.0.0` → `v2.0.0` - Breaking changes

### Release Checklist

- [ ] Update version in code files
- [ ] Update CHANGELOG.md
- [ ] Update LICENSE-HISTORY.md
- [ ] Create git tag: `git tag v1.1.0`
- [ ] Push tag: `git push origin v1.1.0`
- [ ] Create GitHub release with notes
- [ ] Credit contributors in release notes

### Changelog Format

```markdown
## [1.1.0] - 2026-02-20

### Added
- Sentiment analysis metric (#123) @contributor
- Claude conversation parser (#124) @contributor

### Fixed
- Entropy calculation for empty strings (#125) @contributor

### Changed
- Improved documentation for custom metrics

### Contributors
- @contributor1 - Feature A
- @contributor2 - Fix B
- @contributor3 - Docs improvement
```

---

## RECOGNITION

### Contributor Acknowledgment

**All contributors are credited in:**
1. CONTRIBUTORS.md (permanent record)
2. Release notes (for that version)
3. README.md (major contributors)

**Contribution types recognized:**
- Code
- Documentation
- Research/validation
- Issue reporting (significant bugs/features)
- Design/UX improvements
- Community support

### Special Recognition

**Significant contributions earn:**
- Mention in README "Key Contributors" section
- Invitation to maintainer discussions
- Authorship credit in academic papers (if applicable)

**What counts as significant:**
- Major feature implementation
- Substantial architecture improvements
- Comprehensive documentation
- Long-term maintenance support

---

## FINAL NOTES

### The Spirit of This Project

This project exists because:
- One person thought AI-assisted tools should be commons
- Six AIs contributed different expertise layers
- Cross-AI collaboration produced something no single entity could

**When you contribute, you join this pattern:**
- Human + AI collaboration
- Commons-focused output
- Long-term thinking
- Transparent documentation

### Thank You

**Every contribution matters:**
- Bug report → Improves quality
- Documentation → Helps newcomers
- Code → Adds capability
- Research → Validates approach
- Discussion → Advances thinking

**You're not just contributing code.**
**You're contributing to a commons.**
**That will outlive all of us.**

**Thank you for being part of this.**

---

## DOCUMENT HISTORY

- v1.0.0 - Initial guidelines (February 2026)
- Created through multi-AI collaboration (Claude primary)
- Aligned with RCNM v1.0 principles
- Subject to refinement based on contributor feedback

---

**Questions about contributing?**
Open a [GitHub Discussion](../../discussions) or check existing [Issues](../../issues).

**Ready to contribute?**
Fork the repository and start coding!

---

**Research Commons Non-Monetization License**
**Version 1.0 | February 2026**
