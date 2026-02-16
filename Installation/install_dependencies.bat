@echo off
REM Installation Script for ECHOS Dialogue Analysis Tool (Windows)
REM ================================================================
REM
REM This script installs all required Python packages and dependencies
REM needed to run the dialogue analysis tool on Windows.
REM
REM Usage:
REM   Double-click this file, or
REM   Run from Command Prompt: install_dependencies.bat
REM
REM Author: Multi-AI Collaborative Development
REM Version: 1.0
REM License: MIT
REM

setlocal enabledelayedexpansion

echo ========================================================================
echo ECHOS Dialogue Analysis Tool - Dependency Installation (Windows)
echo ========================================================================
echo.

REM Check if Python is installed
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo [ERROR] Please install Python 3.8 or higher from https://www.python.org/
    echo [ERROR] Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

python --version
echo.

REM Check if pip is available
echo [INFO] Checking pip installation...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available!
    echo [INFO] Installing pip...
    python -m ensurepip --upgrade
)

python -m pip --version
echo.

REM Upgrade pip
echo [INFO] Upgrading pip to latest version...
python -m pip install --upgrade pip
echo.

echo ========================================================================
echo Installing Required Python Packages
echo ========================================================================
echo.

REM Core dependencies
echo [INFO] Installing core scientific computing libraries...
python -m pip install numpy pandas
if errorlevel 1 (
    echo [ERROR] Failed to install numpy and pandas
    pause
    exit /b 1
)

REM Excel support
echo [INFO] Installing Excel file support...
python -m pip install openpyxl xlsxwriter
if errorlevel 1 (
    echo [ERROR] Failed to install Excel libraries
    pause
    exit /b 1
)

REM NLP libraries
echo [INFO] Installing Natural Language Processing libraries...
python -m pip install textblob nltk
if errorlevel 1 (
    echo [ERROR] Failed to install NLP libraries
    pause
    exit /b 1
)

REM ROUGE scorer
echo [INFO] Installing ROUGE evaluation metrics...
python -m pip install rouge-score
if errorlevel 1 (
    echo [ERROR] Failed to install rouge-score
    pause
    exit /b 1
)

REM OpenAI tiktoken
echo [INFO] Installing OpenAI tiktoken tokenizer...
python -m pip install tiktoken
if errorlevel 1 (
    echo [ERROR] Failed to install tiktoken
    pause
    exit /b 1
)

echo.
echo [INFO] Downloading required NLTK data...
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('wordnet', quiet=True); nltk.download('omw-1.4', quiet=True); nltk.download('averaged_perceptron_tagger', quiet=True); nltk.download('brown', quiet=True); print('NLTK data download complete!')"

echo.
echo [INFO] Downloading TextBlob corpora...
python -m textblob.download_corpora

echo.
echo ========================================================================
echo Verifying Installation
echo ========================================================================
echo.

python -c "import sys; import importlib.util; packages = ['json', 're', 'datetime', 'collections', 'math', 'itertools', 'difflib', 'warnings', 'numpy', 'pandas', 'openpyxl', 'xlsxwriter', 'textblob', 'nltk', 'rouge_score', 'tiktoken']; all_ok = True; print('Checking required packages:'); print('-' * 50); [print(f'✓ {pkg:30s} OK') if importlib.util.find_spec(pkg.replace('rouge_score', 'rouge-score')) else (print(f'✗ {pkg:30s} FAILED'), setattr(sys, 'exit_code', 1)) for pkg in packages]; print(); print('✓ All packages installed successfully!' if getattr(sys, 'exit_code', 0) == 0 else '✗ Some packages failed to install'); sys.exit(getattr(sys, 'exit_code', 0))"

if errorlevel 1 (
    echo.
    echo ========================================================================
    echo [ERROR] Installation Failed!
    echo ========================================================================
    echo.
    echo [ERROR] Some dependencies could not be installed.
    echo [ERROR] Please check the error messages above.
    echo.
    echo [INFO] Common issues:
    echo   - Python not in PATH: Reinstall Python and check "Add to PATH"
    echo   - Permission issues: Run as Administrator
    echo   - Network issues: Check your internet connection
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo [SUCCESS] Installation Complete!
echo ========================================================================
echo.
echo [INFO] All dependencies have been installed successfully.
echo [INFO] You can now run the dialogue analysis tool.
echo.
echo [INFO] Next steps:
echo   1. Place your ChatGPT JSON export file in this directory
echo   2. Run: python chat_analysis.py
echo.
echo [INFO] For help, see README.md
echo.
pause
