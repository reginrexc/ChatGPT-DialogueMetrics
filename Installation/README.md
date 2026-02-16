# Installation Guide for ChatGPT-DialogueMetrics

This directory contains installation scripts for setting up all required dependencies to run the ECHOS dialogue analysis tool.

## Quick Start

### Option 1: Automated Installation (Recommended)

#### Linux / macOS
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

#### Windows
Double-click `install_dependencies.bat` or run from Command Prompt:
```cmd
install_dependencies.bat
```

#### Cross-Platform (Python Script)
```bash
python3 install_dependencies.py
```

### Option 2: Manual Installation

Using pip with requirements file:
```bash
pip install -r requirements.txt
```

Or with system package flag (if needed):
```bash
pip install -r requirements.txt --break-system-packages
```

Then download NLTK data:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('averaged_perceptron_tagger'); nltk.download('brown')"
```

And TextBlob corpora:
```bash
python -m textblob.download_corpora
```

## System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Storage**: 500MB for dependencies and data
- **Operating System**: 
  - Linux (Ubuntu 18.04+, Debian 10+, or equivalent)
  - macOS 10.14+
  - Windows 10+

### Recommended Specifications
- **Python**: 3.10 or higher
- **RAM**: 4GB or more
- **Storage**: 1GB free space
- **Internet**: Required for downloading packages and data

## Required Python Packages

The tool requires the following packages:

### Core Dependencies
- `numpy` (≥1.20.0) - Numerical computing
- `pandas` (≥1.3.0) - Data manipulation and analysis

### Excel Support
- `openpyxl` (≥3.0.0) - Reading Excel files
- `xlsxwriter` (≥3.0.0) - Writing Excel files

### Natural Language Processing
- `textblob` (≥0.15.0) - Sentiment analysis
- `nltk` (≥3.6.0) - Natural Language Toolkit

### Evaluation Metrics
- `rouge-score` (≥0.1.0) - ROUGE metrics for text evaluation

### Tokenization
- `tiktoken` (≥0.3.0) - OpenAI's tokenizer

### Built-in Python Modules (No Installation Needed)
- `json` - JSON parsing
- `re` - Regular expressions
- `datetime` - Date and time handling
- `collections` - Container datatypes
- `math` - Mathematical functions
- `itertools` - Iterator functions
- `difflib` - Sequence comparison
- `warnings` - Warning control

## Installation Methods Explained

### Method 1: Shell Script (Linux/macOS)
The `install_dependencies.sh` script:
- Checks Python and pip installation
- Upgrades pip to latest version
- Installs all required packages
- Downloads NLTK data and TextBlob corpora
- Verifies installation
- Provides colored output and error handling

**Advantages:**
- One-command installation
- Automatic error detection
- Installation verification included

**Requirements:**
- Bash shell (standard on Linux/macOS)
- Execute permissions (`chmod +x` may be needed)

### Method 2: Batch Script (Windows)
The `install_dependencies.bat` script:
- Checks Python and pip installation
- Installs all required packages
- Downloads necessary data
- Verifies installation

**Advantages:**
- Native Windows script
- No additional dependencies
- Simple double-click execution

**Requirements:**
- Windows Command Prompt
- Python in system PATH

### Method 3: Python Script (Cross-Platform)
The `install_dependencies.py` script:
- Works on all operating systems
- Handles system-specific issues
- Provides detailed feedback
- Most robust error handling

**Advantages:**
- Works everywhere Python works
- Best error messages
- Most reliable

**Requirements:**
- Python 3.8+
- No other dependencies

### Method 4: Requirements File
The `requirements.txt` file:
- Standard pip format
- Can be used with virtual environments
- Integrates with existing workflows

**Advantages:**
- Industry standard format
- Works with virtualenv/venv
- Can be version-controlled

**Requirements:**
- pip installed
- Manual NLTK/TextBlob data download needed

## Troubleshooting

### Python Not Found
**Error:** `python3: command not found` or `'python' is not recognized`

**Solution:**
1. Install Python from [python.org](https://www.python.org/)
2. During installation, check "Add Python to PATH"
3. Restart terminal/command prompt
4. Verify: `python --version` or `python3 --version`

### Permission Denied
**Error:** `Permission denied` or `Access is denied`

**Solution (Linux/macOS):**
```bash
# Use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# OR use --user flag
pip install -r requirements.txt --user
```

**Solution (Windows):**
- Run Command Prompt as Administrator
- Or use virtual environment (see above)

### SSL Certificate Error
**Error:** `SSL: CERTIFICATE_VERIFY_FAILED`

**Solution:**
The installation scripts handle this automatically for NLTK downloads. If you still encounter issues:

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

### Package Installation Fails
**Error:** Various pip installation errors

**Solution:**
1. Update pip: `python -m pip install --upgrade pip`
2. Try installing packages individually:
   ```bash
   pip install numpy pandas
   pip install openpyxl xlsxwriter
   pip install textblob nltk
   pip install rouge-score tiktoken
   ```
3. Check your internet connection
4. Consider using a virtual environment

### NLTK Data Download Fails
**Error:** Cannot download NLTK data

**Solution:**
1. Try manual download:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('brown')
   ```

2. Or download from [NLTK Data](https://www.nltk.org/data.html) manually

### Low Disk Space
**Error:** Insufficient storage

**Solution:**
- Free up at least 500MB of disk space
- Consider installing in a different location
- Use `pip install --no-cache-dir` to reduce temporary space usage

### Old Python Version
**Error:** Python 3.7 or older

**Solution:**
- Upgrade to Python 3.8 or higher
- Or install a newer Python version alongside (use `python3.8`, `python3.9`, etc.)

## Verifying Installation

After installation, verify all packages are working:

```bash
python3 -c "import numpy, pandas, textblob, nltk, rouge_score, tiktoken, openpyxl, xlsxwriter; print('All packages imported successfully!')"
```

Or run the verification section of any installation script.

## Virtual Environment (Recommended)

For isolated installation:

```bash
# Create virtual environment
python3 -m venv echos-env

# Activate it
# On Linux/macOS:
source echos-env/bin/activate
# On Windows:
echos-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('averaged_perceptron_tagger'); nltk.download('brown')"

# Download TextBlob corpora
python -m textblob.download_corpora

# Deactivate when done
deactivate
```

## Next Steps

After successful installation:

1. **Prepare your data:**
   - Export your ChatGPT conversation as JSON
   - Place the JSON file in the tool directory

2. **Run the analysis:**
   ```bash
   python3 chat_analysis.py
   ```

3. **View results:**
   - Open the generated Excel file
   - Explore the 86+ metrics across multiple sheets

## Getting Help

If you encounter issues not covered here:

1. Check the main README.md for tool documentation
2. Verify your Python version: `python --version`
3. Check pip version: `pip --version`
4. Review error messages carefully
5. Try installation in a fresh virtual environment
6. Create an issue on GitHub with:
   - Your operating system
   - Python version
   - Complete error message
   - Steps you've already tried

## License

MIT License - See LICENSE file for details

## Authors

Multi-AI Collaborative Development:
- ChatGPT (OpenAI) - Foundation
- Claude (Anthropic) - Epistemic enhancements
- Kimi (Moonshot AI) - Cognitive-social expansion
- DeepSeek (DeepSeek AI) - Systematic organization
- Gemini (Google) - Relational dynamics

Human Orchestration: [Regin Rex]
