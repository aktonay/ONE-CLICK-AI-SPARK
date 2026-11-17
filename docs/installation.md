# Installation Guide

This guide will walk you through installing One Click AI Spark on your system, step by step.

## Table of Contents

- [Windows Installation](#windows-installation)
- [Ubuntu/Linux Installation](#ubuntulinux-installation)
- [macOS Installation](#macos-installation)
- [Verify Installation](#verify-installation)
- [Troubleshooting](#troubleshooting-installation)

---

## Windows Installation

### Step 1: Ensure Python is Installed

1. **Open PowerShell**
   - Press `Win + X`
   - Select "Windows PowerShell" or "Windows Terminal"

2. **Check Python version:**
   ```powershell
   python --version
   ```
   
   **Expected output:** `Python 3.11.0` or higher

3. **If Python is not installed or version is too old:**
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - Run the installer
   - ✅ **IMPORTANT:** Check "Add Python to PATH"
   - Click "Install Now"
   - Restart your computer

### Step 2: Install One Click AI Spark

In PowerShell, run:

```powershell
pip install one-click-ai-spark
```

**What's happening?**
- `pip` is Python's package installer
- It downloads and installs One Click AI Spark from PyPI (Python Package Index)

**Expected output:**
```
Collecting one-click-ai-spark
  Downloading one_click_ai_spark-3.0.2-py3-none-any.whl
Installing collected packages: one-click-ai-spark
Successfully installed one-click-ai-spark-3.0.2
```

### Step 3: Verify Installation

```powershell
one-click-ai --version
```

**Expected output:** `One Click AI Spark version 3.0.2`

---

## Ubuntu/Linux Installation

### Step 1: Update System Packages

Open Terminal (`Ctrl + Alt + T`) and run:

```bash
sudo apt update
```

**What this does:** Updates the list of available packages

### Step 2: Install Python 3.11+

```bash
# Check if Python 3.11+ is already installed
python3 --version

# If not, install Python 3.11
sudo apt install python3.11 python3-pip python3.11-venv
```

**Package breakdown:**
- `python3.11` - Python interpreter
- `python3-pip` - Package installer
- `python3.11-venv` - Virtual environment support (recommended)

### Step 3: Install One Click AI Spark

```bash
pip3 install one-click-ai-spark
```

**If you get "command not found":**

```bash
python3 -m pip install one-click-ai-spark
```

### Step 4: Add to PATH (if needed)

If `one-click-ai` command is not found after installation:

```bash
# Add to your PATH
export PATH="$HOME/.local/bin:$PATH"

# Make it permanent by adding to ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Step 5: Verify Installation

```bash
one-click-ai --version
```

**Expected output:** `One Click AI Spark version 3.0.2`

---

## macOS Installation

### Step 1: Install Homebrew (if not installed)

Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Python 3.11+

```bash
# Install Python
brew install python@3.11

# Verify installation
python3 --version
```

### Step 3: Install One Click AI Spark

```bash
pip3 install one-click-ai-spark
```

### Step 4: Verify Installation

```bash
one-click-ai --version
```

**Expected output:** `One Click AI Spark version 3.0.2`

---

## Verify Installation

After installation, run these commands to ensure everything works:

### Check Version

```bash
one-click-ai --version
```

### View Help

```bash
one-click-ai --help
```

**Expected output:**
```
Usage: one-click-ai [OPTIONS] COMMAND [ARGS]...

  🚀 One Click AI Spark - Generate production-ready AI backends instantly

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  generate  Generate a new AI project
  list      List available features
```

### List Available Features

```bash
one-click-ai list
```

You should see a list of all available AI features (LLM, RAG, Voice AI, etc.)

---

## Troubleshooting Installation

### "python: command not found"

**Windows:**
- Reinstall Python from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH"
- Restart your computer

**Ubuntu:**
```bash
sudo apt install python3.11
```

**macOS:**
```bash
brew install python@3.11
```

---

### "pip: command not found"

**Windows:**
```powershell
python -m ensurepip --upgrade
```

**Ubuntu:**
```bash
sudo apt install python3-pip
```

**macOS:**
```bash
python3 -m ensurepip --upgrade
```

---

### "one-click-ai: command not found" (after successful pip install)

This means the installation directory is not in your PATH.

**Windows:**
1. Find Python Scripts directory:
   ```powershell
   python -c "import sys; print(sys.prefix + '\\Scripts')"
   ```
2. Add to PATH:
   - Search "Environment Variables" in Start Menu
   - Click "Environment Variables"
   - Under "User variables", select "Path"
   - Click "Edit" → "New"
   - Paste the Scripts directory path
   - Click "OK" on all windows
   - **Restart PowerShell**

**Ubuntu/macOS:**
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

### "Permission denied" errors

**Ubuntu/macOS:**

Use `pip3 install --user` instead:

```bash
pip3 install --user one-click-ai-spark
```

Or use a virtual environment (recommended):

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install one-click-ai-spark
```

---

### "No module named 'pip'"

**All systems:**
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

---

### SSL Certificate Errors

**Windows:**

Install/update certificates:
```powershell
pip install --upgrade certifi
```

**Ubuntu:**
```bash
sudo apt install ca-certificates
sudo update-ca-certificates
```

---

### Installing Specific Version

If you need a specific version:

```bash
# Install specific version
pip install one-click-ai-spark==3.0.2

# Upgrade to latest
pip install --upgrade one-click-ai-spark
```

---

### Behind a Proxy

If you're behind a corporate proxy:

```bash
pip install --proxy http://user:password@proxy-server:port one-click-ai-spark
```

Or set environment variables:

**Windows:**
```powershell
$env:HTTP_PROXY="http://proxy-server:port"
$env:HTTPS_PROXY="http://proxy-server:port"
pip install one-click-ai-spark
```

**Ubuntu/macOS:**
```bash
export HTTP_PROXY="http://proxy-server:port"
export HTTPS_PROXY="http://proxy-server:port"
pip install one-click-ai-spark
```

---

## Using Virtual Environments (Recommended)

Virtual environments keep your projects isolated and avoid dependency conflicts.

### Windows

```powershell
# Create virtual environment
python -m venv ai-env

# Activate it
.\ai-env\Scripts\activate

# Your prompt should now show (ai-env)

# Install One Click AI Spark
pip install one-click-ai-spark

# When done, deactivate
deactivate
```

### Ubuntu/macOS

```bash
# Create virtual environment
python3 -m venv ai-env

# Activate it
source ai-env/bin/activate

# Your prompt should now show (ai-env)

# Install One Click AI Spark
pip install one-click-ai-spark

# When done, deactivate
deactivate
```

---

## Uninstalling

If you need to uninstall:

```bash
pip uninstall one-click-ai-spark
```

To remove all dependencies too:

```bash
pip uninstall one-click-ai-spark jinja2 rich typer pyyaml
```

---

## Next Steps

✅ Installation complete! Now you're ready to:

1. **[Quick Start Guide](quick-start.md)** - Build your first AI project
2. **[Features Overview](features.md)** - Explore all available features
3. **[Examples](examples.md)** - See real-world use cases

---

## Still Having Issues?

- Check the **[Troubleshooting Guide](troubleshooting.md)**
- Search **[GitHub Issues](https://github.com/aktonay/ONE-CLICK-AI-SPARK/issues)**
- Ask for help in **[Discussions](https://github.com/aktonay/ONE-CLICK-AI-SPARK/discussions)**

