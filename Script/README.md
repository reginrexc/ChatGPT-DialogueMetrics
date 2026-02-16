# How to Use ChatGPT-DialogueMetrics: Complete Beginner's Guide

**A step-by-step tutorial for researchers with no programming experience**

---

## What You'll Learn

This guide will walk you through:
1. Getting your ChatGPT conversation data
2. Preparing your files
3. Running the analysis
4. Understanding your results

**No programming knowledge required!** Just follow each step carefully.

---

## Before You Start

### What You Need

✓ A computer (Windows, Mac, or Linux)
✓ ChatGPT conversations you want to analyze
✓ About 30 minutes for first-time setup
✓ Internet connection (for setup only)

### What You DON'T Need

✗ Programming experience
✗ Expensive computer (4GB RAM is enough)
✗ Special software (everything is free)
✗ Technical background

---

# Part 1: Getting Your ChatGPT Data

## Step 1.1: Export Your Conversations from ChatGPT

### On ChatGPT Website (chatgpt.com)

1. **Log in to ChatGPT**
   - Go to chatgpt.com
   - Sign in with your account

2. **Open Settings**
   - Look for your profile picture/name in the bottom-left corner
   - Click on it
   - Select **"Settings"**

3. **Navigate to Data Controls**
   - In the settings menu, find **"Data controls"**
   - Click on it

4. **Request Export**
   - Find the **"Export data"** button
   - Click **"Export"**
   - ChatGPT will say: *"We'll email you when your data is ready"*

5. **Wait for Email**
   - Check your email (the one you used for ChatGPT)
   - This usually takes **a few minutes to a few hours**
   - You'll receive an email from OpenAI

6. **Download Your Data**
   - Open the email from OpenAI
   - Click the **"Download data export"** link
   - This downloads a ZIP file to your computer

7. **Extract the ZIP File**
   
   **On Windows:**
   - Right-click the downloaded ZIP file
   - Select **"Extract All..."**
   - Choose where to save it (Desktop is fine)
   - Click **"Extract"**

   **On Mac:**
   - Double-click the ZIP file
   - It automatically extracts to the same folder

   **On Linux:**
   - Right-click the ZIP file
   - Select **"Extract Here"**

8. **Find the conversations.json File**
   - Open the extracted folder
   - You'll see several files
   - Look for **`conversations.json`** (this is what you need!)

**Important:** This file contains ALL your ChatGPT conversations. Keep a backup copy somewhere safe!

---

## Step 1.2: Rename Your File

### Why Rename?

The script looks for a file called **`chat.json`** (not `conversations.json`). We need to rename your file so the script can find it.

### How to Rename

**On Windows:**

1. Right-click on **`conversations.json`**
2. Select **"Rename"**
3. Delete the current name
4. Type: **`chat.json`**
5. Press **Enter**

**On Mac:**

1. Click once on **`conversations.json`** to select it
2. Press **Enter** (this lets you rename)
3. Delete the current name
4. Type: **`chat.json`**
5. Press **Enter** again

**On Linux:**

1. Right-click on **`conversations.json`**
2. Select **"Rename"**
3. Type: **`chat.json`**
4. Press **Enter**

**After renaming, the file should be called:** `chat.json`

---

# Part 2: Setting Up the Analysis Tool

## Step 2.1: Download the Analysis Tool

1. **Get the tool from GitHub** (or wherever you received it)
2. **Extract the files** if it's in a ZIP
3. **Note where you saved it** (remember this location!)

You should now have a folder containing:
- `ChatGPT-DialogueMetrics.py` (the main script)
- `install_dependencies.sh` or `install_dependencies.bat` or `install_dependencies.py` (installation scripts)
- `requirements.txt`
- Several README files

---

## Step 2.2: Install Required Software

You only need to do this once!

### Option A: Using the Automatic Installer (Easiest)

**On Windows:**

1. Open the folder containing the tool
2. Find **`install_dependencies.bat`**
3. **Double-click** it
4. A black window (Command Prompt) will open
5. Watch the installation happen (5-10 minutes)
6. When you see "Installation Complete!", you're done!
7. Press any key to close the window

**On Mac:**

1. Open the folder containing the tool
2. Find **`install_dependencies.sh`**
3. **Right-click** on it
4. Select **"Open With" → "Terminal"**
5. If asked, type your password and press Enter
6. Watch the installation (5-10 minutes)
7. When you see "Installation Complete!", you're done!

**On Linux:**

1. Open the folder containing the tool
2. **Right-click** in empty space
3. Select **"Open in Terminal"**
4. Type: `chmod +x install_dependencies.sh`
5. Press **Enter**
6. Type: `./install_dependencies.sh`
7. Press **Enter**
8. Watch the installation (5-10 minutes)
9. When you see "Installation Complete!", you're done!

### Option B: Using Python Script (If Option A doesn't work)

**All Platforms:**

1. Open the folder containing the tool
2. Open Terminal (Mac/Linux) or Command Prompt (Windows)
   
   **Windows:** 
   - Press **Windows key + R**
   - Type: `cmd`
   - Press **Enter**
   - Type: `cd ` (with a space after cd)
   - Drag the tool folder into the window
   - Press **Enter**

   **Mac:**
   - Open **Terminal** (search for it in Spotlight)
   - Type: `cd ` (with a space after cd)
   - Drag the tool folder into the Terminal window
   - Press **Enter**

   **Linux:**
   - Right-click in the folder
   - Select **"Open in Terminal"**

3. Type: `python3 install_dependencies.py`
4. Press **Enter**
5. Wait for installation to complete

---

## Step 2.3: Place Your Data File

This is **VERY IMPORTANT**!

### The Golden Rule

**The `chat.json` file and `ChatGPT-DialogueMetrics.py` file must be in the SAME FOLDER!**

### How to Do This

1. **Find your renamed file:** `chat.json`
2. **Find the tool folder** (where `ChatGPT-DialogueMetrics.py` is)
3. **Move** (or copy) `chat.json` into the tool folder

**To move/copy a file:**

**On Windows:**
- Select `chat.json`
- Press **Ctrl + X** (cut) or **Ctrl + C** (copy)
- Open the tool folder
- Press **Ctrl + V** (paste)

**On Mac:**
- Select `chat.json`
- Press **⌘ + X** (cut) or **⌘ + C** (copy)
- Open the tool folder
- Press **⌘ + V** (paste)

**On Linux:**
- Right-click `chat.json`
- Select "Cut" or "Copy"
- Open the tool folder
- Right-click in empty space
- Select "Paste"

### Double-Check!

Open the tool folder. You should see BOTH:
- ✓ `ChatGPT-DialogueMetrics.py`
- ✓ `chat.json`

If you see both files in the same folder, you're ready!

---

# Part 3: Running the Analysis

## Step 3.1: Open Terminal/Command Prompt in the Tool Folder

### Windows

**Method 1 (Easy):**
1. Open the folder containing the tool
2. Click in the address bar at the top (where it shows the folder path)
3. Type: `cmd`
4. Press **Enter**
5. A Command Prompt window opens!

**Method 2:**
1. Press **Windows key + R**
2. Type: `cmd`
3. Press **Enter**
4. Type: `cd ` (with a space)
5. Drag the tool folder into the window
6. Press **Enter**

### Mac

1. Open **Finder**
2. Navigate to the tool folder
3. Right-click on the folder
4. Hold **Option key** (you'll see new menu items appear)
5. Select **"Open in Terminal"**

OR:

1. Open **Terminal** (search in Spotlight)
2. Type: `cd ` (with a space)
3. Drag the tool folder into Terminal
4. Press **Enter**

### Linux

1. Open the tool folder in your file manager
2. Right-click in empty space
3. Select **"Open in Terminal"**

---

## Step 3.2: Run the Script

### The Command

In the Terminal/Command Prompt window, type:

```bash
python3 ChatGPT-DialogueMetrics.py chat.json
```

**On Windows, you might need to type:**
```cmd
python ChatGPT-DialogueMetrics.py chat.json
```

Then press **Enter**!

### What Happens Next

You'll see text scrolling by. This is the script working! It will:

1. **Reading your conversations...** (a few seconds)
2. **Analyzing messages...** (2-5 minutes for typical files)
3. **Computing metrics...** (processing all 86+ measurements)
4. **Generating Excel file...** (creating your results)
5. **Done!** (you'll see a completion message)

**Be patient!** For a typical conversation file (8MB), this takes 2-5 minutes.

**Don't close the window** while it's running!

### Progress Indicators

You'll see messages like:
```
Processing message 100 of 2557...
Processing message 200 of 2557...
```

This shows it's working correctly.

### When It's Done

You'll see a message like:
```
Analysis complete!
Output saved to: chat_analysis_20240315_143022.xlsx
```

The script has finished! 🎉

---

## Step 3.3: Find Your Results

### Locate the Output File

1. Go to the tool folder (where `ChatGPT-DialogueMetrics.py` is)
2. Look for a new file with a name like:
   - `chat_analysis_20240315_143022.xlsx`
   - (The numbers are the date and time)

This is your results file!

### Open the Results

**Simply double-click the Excel file**

It will open in:
- Microsoft Excel (if you have it)
- Google Sheets (upload it to Google Drive)
- LibreOffice Calc (free alternative)
- Apple Numbers (on Mac)

---

# Part 4: Understanding Your Results

## Step 4.1: Navigate the Excel File

### What You'll See

The Excel file has **multiple sheets** (tabs at the bottom):

1. **Message Analysis** - Every message with all metrics
2. **Summary Statistics** - Overall patterns
3. **Correlation Matrix** - How metrics relate to each other
4. **User vs Assistant** - Comparison between you and AI
5. **Trajectory Analysis** - How things changed over time

### Basic Navigation

**Switch between sheets:**
- Click the tabs at the bottom of the Excel window
- Each tab shows different analysis

**Frozen headers:**
- The first row stays visible when you scroll down
- This helps you remember what each column means

**Hyperlinks:**
- Some cells are clickable
- They take you to related sheets

---

## Step 4.2: What the Metrics Mean

### Main Metrics You'll See

**Basic Measurements:**
- **Word Count** - How many words in each message
- **Sentence Count** - How many sentences
- **Sentiment Score** - How positive/negative the tone was
  - Positive number = positive tone
  - Negative number = negative tone
  - Close to 0 = neutral

**Cognitive Metrics:**
- **Cognitive Load** - How mentally demanding the message was
  - Higher numbers = more complex thinking
  - Typical range: 2-6
- **Abstraction Markers** - How abstract vs concrete
- **Metacognition** - Thinking about thinking

**Epistemic Metrics:**
- **Contradictions** - Times you or AI challenged/corrected
- **Elaborations** - Times you or AI explained further
- **Hedges** - Uncertainty words ("maybe", "possibly")
- **Confidence** - Certainty words ("definitely", "clearly")

**Emotional Metrics:**
- **Curiosity Score** - How much you were seeking to learn
- **Frustration Score** - Signs of frustration
- **Satisfaction Score** - Signs of satisfaction

**Social Metrics:**
- **Rapport Index** - How warm/friendly the conversation was
- **Social Presence** - How engaged both parties were

### Don't Worry!

You don't need to understand every metric right away. Start with the **Summary Statistics** sheet—it gives you the big picture.

---

## Step 4.3: Reading Summary Statistics

### Open the "Summary Statistics" Sheet

1. Click the **"Summary Statistics"** tab at the bottom
2. You'll see a table with overall numbers

### Key Numbers to Look At

**Total Messages:** How many messages in the conversation

**Average Sentiment:** 
- Positive = friendly, constructive conversation
- Negative = conflict or frustration

**Contradiction/Elaboration Ratio:**
- Higher than 1.0 = More challenging than explaining
- Lower than 1.0 = More explaining than challenging

**Average Cognitive Load:**
- 2-3 = Light, casual conversation
- 4-5 = Moderate intellectual engagement
- 6+ = Intense, complex thinking

**Positive Sentiment %:**
- Above 80% = Very positive conversation
- 60-80% = Balanced conversation
- Below 60% = Consider whether dialogue was productive

---

# Part 5: Common Problems and Solutions

## Problem 1: "Python is not recognized" or "command not found"

**This means:** Python isn't installed or not in your system PATH

**Solution:**

1. **Install Python:**
   - Go to [python.org](https://www.python.org/)
   - Download Python 3.8 or higher
   - **Important:** During installation, check the box "Add Python to PATH"
   - Restart your computer
   - Try again

## Problem 2: "No module named..."

**This means:** A required package isn't installed

**Solution:**

1. Run the installation script again:
   ```bash
   python3 install_dependencies.py
   ```
2. Wait for it to complete
3. Try running the analysis again

## Problem 3: "Cannot find chat.json"

**This means:** The script can't find your data file

**Solution:**

1. Make sure your file is named exactly: `chat.json` (not `conversations.json`)
2. Make sure it's in the SAME folder as `ChatGPT-DialogueMetrics.py`
3. Check for typos in the filename
4. Make sure the file extension is `.json` (not `.json.txt`)

**To see file extensions on Windows:**
- Open File Explorer
- Click "View" menu
- Check "File name extensions"

## Problem 4: Script runs but no output file appears

**Solution:**

1. Check the tool folder carefully
2. Look for ANY `.xlsx` files
3. The filename has a timestamp, so it won't be exactly `chat_analysis.xlsx`
4. Look for files like: `chat_analysis_20240315_143022.xlsx`

## Problem 5: "Permission denied" or "Access is denied"

**This means:** Your user account doesn't have permission

**Solution:**

**Windows:** Right-click Command Prompt, select "Run as Administrator"

**Mac/Linux:** 
- You might need administrator access
- Try: `sudo python3 ChatGPT-DialogueMetrics.py`
- Enter your password when asked

## Problem 6: Script is very slow or freezes

**This means:** Your file might be very large

**Solution:**

1. Check your JSON file size:
   - Right-click → Properties (Windows)
   - Right-click → Get Info (Mac)
   
2. If it's **larger than 50MB**:
   - This is normal! Large files take longer
   - Wait patiently (could take 10-30 minutes)
   - Don't close the window

3. For **very large files** (100MB+):
   - Consider using the chunking tool (if available)
   - Or analyze only specific conversations

## Problem 7: Excel file won't open

**Solution:**

1. **Install a spreadsheet program:**
   - **Free option:** LibreOffice ([libreoffice.org](https://www.libreoffice.org/))
   - **Free option:** Upload to Google Sheets
   - **Paid option:** Microsoft Excel

2. **To open in Google Sheets:**
   - Go to [sheets.google.com](https://sheets.google.com)
   - Click "Blank" to create a new sheet
   - File → Import → Upload
   - Select your `.xlsx` file

---

# Part 6: Tips for First-Time Users

## Start Small

If you have many conversations, test on a smaller one first:
1. Open your `chat.json` in a text editor
2. Copy just one conversation
3. Save as `chat_small.json`
4. Rename to `chat.json` for testing

## Keep Your Original File Safe

**Always keep a backup of your original `conversations.json`!**

1. Copy it to a safe location
2. Maybe upload to cloud storage
3. This way you can always start over if needed

## Check the Sample Output

Look at the sample files included in the repository to see what your results should look like.

## Take Your Time

Don't rush! Each step is simple if you follow carefully.

## Ask for Help

If you're stuck:
1. Read the error message carefully
2. Check this guide's troubleshooting section
3. Search for the error online
4. Ask in the repository's Issues section

---

# Quick Reference Card

## The Five Essential Steps

```
1. Export from ChatGPT → Get conversations.json
   ↓
2. Rename to chat.json
   ↓
3. Put chat.json in tool folder (same as ChatGPT-DialogueMetrics.py)
   ↓
4. Open Terminal/Command Prompt in that folder
   ↓
5. Type: python3 ChatGPT-DialogueMetrics.py
   ↓
   Results appear as .xlsx file!
```

## Essential Commands

**Install dependencies:**
```bash
python3 install_dependencies.py
```

**Run analysis:**
```bash
python3 ChatGPT-DialogueMetrics.py
```

**Check Python version:**
```bash
python3 --version
```

---

# Appendix: Platform-Specific Details

## For Windows Users

### Opening Command Prompt in a Folder (Detailed)

1. Open File Explorer
2. Navigate to your tool folder
3. Click in the address bar (where it shows: `C:\Users\YourName\Documents\ChatGPT-DialogueMetrics-tool`)
4. The text becomes highlighted/blue
5. Type: `cmd`
6. Press Enter
7. Command Prompt opens in that folder!

### Viewing File Extensions

By default, Windows hides file extensions. To see them:

1. Open File Explorer
2. Click the "View" tab at the top
3. Check the box "File name extensions"

Now you can see if a file is `chat.json` or `chat.json.txt`

### If Python Opens Microsoft Store

If typing `python` opens the Microsoft Store instead:

1. Search for "Manage app execution aliases" in Windows search
2. Turn OFF the Python toggles
3. Try again

---

## For Mac Users

### Opening Terminal from Finder

**Method 1:**
1. Open Finder
2. Go to your tool folder
3. Right-click the folder (or Ctrl+click)
4. Hold the **Option** key
5. Select "Open in Terminal"

**Method 2:**
1. Open Terminal (Command + Space, type "Terminal")
2. Type: `cd ` (with a space)
3. Drag your tool folder into the Terminal window
4. Press Enter

### If Permission Denied

Mac may ask for permission:

1. System Preferences → Security & Privacy
2. Click the lock to make changes
3. Allow Terminal or Python

---

## For Linux Users

### Opening Terminal in Folder

**Ubuntu/Debian/Most Distributions:**
1. Open file manager
2. Navigate to tool folder
3. Right-click in empty space
4. Select "Open in Terminal"

**Alternative:**
1. Open Terminal
2. Type: `cd ~/path/to/tool/folder`
3. Press Enter

### Installing Python (if needed)

Most Linux distributions include Python. If not:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

**Arch:**
```bash
sudo pacman -S python python-pip
```

---

# Still Confused?

## Visual Checklist

Before running, verify:

□ Python is installed (run `python3 --version`)
□ Dependencies are installed (ran installation script)
□ You have `chat.json` file (renamed from conversations.json)
□ `chat.json` is in the same folder as `ChatGPT-DialogueMetrics.py`
□ You opened Terminal/Command Prompt in that folder
□ You typed the command correctly: `python3 ChatGPT-DialogueMetrics.py`

If all boxes are checked, it should work!

## Getting Help

**GitHub Issues:**
- Go to the repository
- Click "Issues"
- Click "New Issue"
- Describe your problem with:
  - Your operating system
  - What step you're on
  - The exact error message (copy and paste it)
  - What you've tried

**Be specific!** "It doesn't work" is hard to help with. "I get error: 'Python not found' when typing python3" is much better!

---

# Congratulations! 🎉

If you've made it through this guide and successfully analyzed your conversation, you've just:

✓ Learned to use command-line tools
✓ Worked with Python scripts
✓ Analyzed data scientifically
✓ Generated quantitative research metrics

**You're now equipped to:**
- Analyze all your ChatGPT conversations
- Understand your dialogue patterns
- Use this data for research
- Share your findings

**Welcome to computational research!**

---

*Last updated: [Date]*
*Questions? Create an issue on GitHub or check the FAQ*
