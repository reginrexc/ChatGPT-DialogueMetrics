#!/bin/bash
#
# Installation Script for ECHOS Dialogue Analysis Tool
# =====================================================
#
# This script installs all required Python packages and dependencies
# needed to run the dialogue analysis tool.
#
# Usage:
#   chmod +x install_dependencies.sh
#   ./install_dependencies.sh
#
# Or:
#   bash install_dependencies.sh
#
# Author: Multi-AI Collaborative Development
# Version: 1.0
# License: MIT
#

set -e  # Exit on error

echo "========================================================================"
echo "ECHOS Dialogue Analysis Tool - Dependency Installation"
echo "========================================================================"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python 3 is installed
print_info "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    print_info "Found: $PYTHON_VERSION"
else
    print_error "Python 3 is not installed!"
    print_error "Please install Python 3.8 or higher from https://www.python.org/"
    exit 1
fi

# Check Python version
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
if [ "$PYTHON_MINOR" -lt 8 ]; then
    print_error "Python 3.8 or higher is required. You have Python 3.$PYTHON_MINOR"
    exit 1
fi

# Check if pip is installed
print_info "Checking pip installation..."
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version)
    print_info "Found: $PIP_VERSION"
else
    print_error "pip3 is not installed!"
    print_error "Installing pip..."
    python3 -m ensurepip --upgrade
fi

# Upgrade pip to latest version
print_info "Upgrading pip to latest version..."
python3 -m pip install --upgrade pip

echo ""
echo "========================================================================"
echo "Installing Required Python Packages"
echo "========================================================================"
echo ""

# Core dependencies
print_info "Installing core scientific computing libraries..."
pip3 install numpy pandas --break-system-packages 2>/dev/null || pip3 install numpy pandas

# Excel support
print_info "Installing Excel file support..."
pip3 install openpyxl xlsxwriter --break-system-packages 2>/dev/null || pip3 install openpyxl xlsxwriter

# NLP libraries
print_info "Installing Natural Language Processing libraries..."
pip3 install textblob nltk --break-system-packages 2>/dev/null || pip3 install textblob nltk

# ROUGE scorer
print_info "Installing ROUGE evaluation metrics..."
pip3 install rouge-score --break-system-packages 2>/dev/null || pip3 install rouge-score

# OpenAI tiktoken for tokenization
print_info "Installing OpenAI tiktoken tokenizer..."
pip3 install tiktoken --break-system-packages 2>/dev/null || pip3 install tiktoken

echo ""
print_info "Downloading required NLTK data..."
python3 << 'NLTK_DOWNLOAD'
import nltk
import ssl

# Handle SSL certificate issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

print("Downloading NLTK punkt tokenizer...")
nltk.download('punkt', quiet=True)

print("Downloading NLTK wordnet...")
nltk.download('wordnet', quiet=True)

print("Downloading NLTK omw-1.4...")
nltk.download('omw-1.4', quiet=True)

print("Downloading NLTK averaged_perceptron_tagger...")
nltk.download('averaged_perceptron_tagger', quiet=True)

print("Downloading NLTK brown corpus...")
nltk.download('brown', quiet=True)

print("NLTK data download complete!")
NLTK_DOWNLOAD

echo ""
print_info "Downloading TextBlob corpora..."
python3 -m textblob.download_corpora

echo ""
echo "========================================================================"
echo "Verifying Installation"
echo "========================================================================"
echo ""

# Verification script
python3 << 'VERIFY'
import sys

def check_import(module_name, package_name=None):
    """Check if a module can be imported"""
    if package_name is None:
        package_name = module_name
    try:
        __import__(module_name)
        print(f"✓ {package_name:30s} OK")
        return True
    except ImportError as e:
        print(f"✗ {package_name:30s} FAILED: {e}")
        return False

print("Checking required packages:")
print("-" * 50)

all_ok = True
all_ok &= check_import('json', 'json (built-in)')
all_ok &= check_import('re', 're (built-in)')
all_ok &= check_import('datetime', 'datetime (built-in)')
all_ok &= check_import('collections', 'collections (built-in)')
all_ok &= check_import('math', 'math (built-in)')
all_ok &= check_import('itertools', 'itertools (built-in)')
all_ok &= check_import('difflib', 'difflib (built-in)')
all_ok &= check_import('warnings', 'warnings (built-in)')

print()
all_ok &= check_import('numpy', 'numpy')
all_ok &= check_import('pandas', 'pandas')
all_ok &= check_import('openpyxl', 'openpyxl')
all_ok &= check_import('xlsxwriter', 'xlsxwriter')
all_ok &= check_import('textblob', 'textblob')
all_ok &= check_import('nltk', 'nltk')
all_ok &= check_import('rouge_score', 'rouge-score')
all_ok &= check_import('tiktoken', 'tiktoken')

print()
if all_ok:
    print("✓ All packages installed successfully!")
    sys.exit(0)
else:
    print("✗ Some packages failed to install. Please check errors above.")
    sys.exit(1)
VERIFY

VERIFY_STATUS=$?

echo ""
echo "========================================================================"
if [ $VERIFY_STATUS -eq 0 ]; then
    echo -e "${GREEN}Installation Complete!${NC}"
    echo "========================================================================"
    echo ""
    print_info "All dependencies have been installed successfully."
    print_info "You can now run the dialogue analysis tool."
    echo ""
    print_info "Next steps:"
    echo "  1. Place your ChatGPT JSON export file in this directory"
    echo "  2. Run: python3 chat_analysis.py"
    echo ""
    print_info "For help, see README.md"
else
    echo -e "${RED}Installation Failed!${NC}"
    echo "========================================================================"
    echo ""
    print_error "Some dependencies could not be installed."
    print_error "Please check the error messages above."
    echo ""
    print_info "Common issues:"
    echo "  - Insufficient permissions: Try using sudo or virtual environment"
    echo "  - Network issues: Check your internet connection"
    echo "  - Python version: Ensure Python 3.8 or higher is installed"
    echo ""
    print_info "For support, see documentation or create an issue on GitHub"
    exit 1
fi
