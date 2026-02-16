#!/usr/bin/env python3
"""
Cross-Platform Installation Script for ECHOS Dialogue Analysis Tool
====================================================================

This script installs all required Python packages and dependencies
needed to run the dialogue analysis tool.

Works on:
- Linux
- macOS
- Windows

Usage:
    python3 install_dependencies.py

Author: Multi-AI Collaborative Development
Version: 1.0
License: MIT
"""

import sys
import subprocess
import platform
import os
from typing import List, Tuple

# Color codes for terminal output
class Colors:
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color
    
    @staticmethod
    def strip_if_windows():
        """Remove color codes on Windows if not supported"""
        if platform.system() == 'Windows' and not os.environ.get('ANSICON'):
            Colors.GREEN = ''
            Colors.YELLOW = ''
            Colors.RED = ''
            Colors.BLUE = ''
            Colors.NC = ''

Colors.strip_if_windows()

def print_info(message: str):
    """Print info message"""
    print(f"{Colors.GREEN}[INFO]{Colors.NC} {message}")

def print_warning(message: str):
    """Print warning message"""
    print(f"{Colors.YELLOW}[WARNING]{Colors.NC} {message}")

def print_error(message: str):
    """Print error message"""
    print(f"{Colors.RED}[ERROR]{Colors.NC} {message}")

def print_success(message: str):
    """Print success message"""
    print(f"{Colors.GREEN}[SUCCESS]{Colors.NC} {message}")

def print_header(message: str):
    """Print section header"""
    print()
    print("=" * 72)
    print(message)
    print("=" * 72)
    print()

def check_python_version() -> bool:
    """Check if Python version is 3.8 or higher"""
    print_info("Checking Python version...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8 or higher is required. You have Python {version.major}.{version.minor}.{version.micro}")
        return False
    
    print_info(f"Python {version.major}.{version.minor}.{version.micro} detected ✓")
    return True

def run_command(command: List[str], description: str, capture_output: bool = False) -> Tuple[bool, str]:
    """Run a command and return success status"""
    try:
        if capture_output:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return True, result.stdout
        else:
            subprocess.run(command, check=True)
            return True, ""
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to {description}")
        if capture_output and e.stderr:
            print(e.stderr)
        return False, ""
    except FileNotFoundError:
        print_error(f"Command not found: {command[0]}")
        return False, ""

def install_package(package: str) -> bool:
    """Install a Python package using pip"""
    print_info(f"Installing {package}...")
    
    # Try with --break-system-packages flag first (for newer systems)
    success, _ = run_command(
        [sys.executable, "-m", "pip", "install", package, "--break-system-packages"],
        f"install {package}",
        capture_output=True
    )
    
    if not success:
        # Fall back to regular pip install
        success, _ = run_command(
            [sys.executable, "-m", "pip", "install", package],
            f"install {package}",
            capture_output=True
        )
    
    return success

def download_nltk_data() -> bool:
    """Download required NLTK data"""
    print_info("Downloading NLTK data...")
    
    try:
        import nltk
        import ssl
        
        # Handle SSL certificate issues
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        
        datasets = ['punkt', 'wordnet', 'omw-1.4', 'averaged_perceptron_tagger', 'brown']
        
        for dataset in datasets:
            print(f"  - Downloading {dataset}...")
            nltk.download(dataset, quiet=True)
        
        print_info("NLTK data downloaded ✓")
        return True
        
    except Exception as e:
        print_error(f"Failed to download NLTK data: {e}")
        return False

def download_textblob_corpora() -> bool:
    """Download TextBlob corpora"""
    print_info("Downloading TextBlob corpora...")
    
    success, _ = run_command(
        [sys.executable, "-m", "textblob.download_corpora"],
        "download TextBlob corpora"
    )
    
    if success:
        print_info("TextBlob corpora downloaded ✓")
    
    return success

def verify_installation() -> bool:
    """Verify all required packages are installed"""
    print_header("Verifying Installation")
    
    required_packages = [
        ('json', 'json (built-in)'),
        ('re', 're (built-in)'),
        ('datetime', 'datetime (built-in)'),
        ('collections', 'collections (built-in)'),
        ('math', 'math (built-in)'),
        ('itertools', 'itertools (built-in)'),
        ('difflib', 'difflib (built-in)'),
        ('warnings', 'warnings (built-in)'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('openpyxl', 'openpyxl'),
        ('xlsxwriter', 'xlsxwriter'),
        ('textblob', 'textblob'),
        ('nltk', 'nltk'),
        ('rouge_score', 'rouge-score'),
        ('tiktoken', 'tiktoken'),
    ]
    
    print("Checking required packages:")
    print("-" * 50)
    
    all_ok = True
    for module_name, display_name in required_packages:
        try:
            __import__(module_name)
            print(f"✓ {display_name:30s} OK")
        except ImportError as e:
            print(f"✗ {display_name:30s} FAILED: {e}")
            all_ok = False
    
    print()
    return all_ok

def main():
    """Main installation function"""
    print_header("ECHOS Dialogue Analysis Tool - Dependency Installation")
    
    print_info(f"Platform: {platform.system()} {platform.release()}")
    print_info(f"Python: {sys.version}")
    print()
    
    # Check Python version
    if not check_python_version():
        print_error("Installation cannot continue with unsupported Python version")
        return 1
    
    # Upgrade pip
    print_header("Upgrading pip")
    print_info("Upgrading pip to latest version...")
    run_command(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        "upgrade pip"
    )
    
    # Install packages
    print_header("Installing Required Python Packages")
    
    packages = [
        ("numpy", "Core scientific computing"),
        ("pandas", "Data analysis and manipulation"),
        ("openpyxl", "Excel file reading"),
        ("xlsxwriter", "Excel file writing"),
        ("textblob", "Natural Language Processing"),
        ("nltk", "Natural Language Toolkit"),
        ("rouge-score", "ROUGE evaluation metrics"),
        ("tiktoken", "OpenAI tokenizer"),
    ]
    
    failed_packages = []
    
    for package, description in packages:
        print_info(f"{description}...")
        if not install_package(package):
            failed_packages.append(package)
            print_warning(f"Failed to install {package} - will verify later")
    
    # Download NLTK data
    print()
    if not download_nltk_data():
        print_warning("NLTK data download had issues")
    
    # Download TextBlob corpora
    print()
    if not download_textblob_corpora():
        print_warning("TextBlob corpora download had issues")
    
    # Verify installation
    all_ok = verify_installation()
    
    print()
    if all_ok:
        print_header("✓ Installation Complete!")
        print_success("All dependencies have been installed successfully.")
        print_info("You can now run the dialogue analysis tool.")
        print()
        print_info("Next steps:")
        print("  1. Place your ChatGPT JSON export file in this directory")
        print("  2. Run: python3 chat_analysis.py")
        print()
        print_info("For help, see README.md")
        return 0
    else:
        print_header("✗ Installation Failed!")
        print_error("Some dependencies could not be installed.")
        print_error("Please check the error messages above.")
        print()
        print_info("Common issues:")
        print("  - Insufficient permissions: Try using a virtual environment")
        print("  - Network issues: Check your internet connection")
        print("  - Python version: Ensure Python 3.8 or higher is installed")
        print()
        
        if failed_packages:
            print_error(f"Failed packages: {', '.join(failed_packages)}")
            print()
        
        print_info("For support, see documentation or create an issue on GitHub")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print()
        print_warning("Installation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print()
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
