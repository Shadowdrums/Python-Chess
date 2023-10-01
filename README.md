# Python Chess Installation Guide 🛡️

Welcome to the Python Chess Installation guide. Here, we'll walk you through the steps to get the `python-chess` library up and running on both Windows and Linux systems.

## 🌐 Prerequisites

- A functional operating system: Windows or Linux.
- A Python version (preferably 3.x) installed.

## 📚 Installation Steps

### 🪟 Windows:

#### 1. **Ensure Python and pip are Installed**:
   
Verify the installation by typing the following in your PowerShell or Command Prompt:
   
python --version
pip --version


If both commands display version numbers, you're set. If `pip` isn't recognized, continue below.

#### 2. **Reinstall Python**:

Sometimes a fresh start does the trick.

- Head to the [official Python website](https://www.python.org/downloads/windows/) to download Python.
- During installation:
  - Ensure you ✔️ "Add Python to PATH"
  - Check "Install pip" (if the option is visible).
- After the installation, open a new PowerShell or Command Prompt window and retry the `pip` command.

#### 3. **Manual pip Installation**:

If you wish to skip the reinstallation, install `pip` manually.

1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a location on your computer.
2. Open PowerShell or Command Prompt and move to the directory containing `get-pip.py`.
3. Then, execute:

python get-pip.py


#### 4. **Check your PATH**:

Maybe `pip` is installed but isn't part of your PATH. Peer into the Python installation directory (for instance `C:\Python311\Scripts`) and look for `pip.exe`. If it's there, append that directory to your PATH.

#### 5. **Install python-chess**:

Once `pip` is in your arsenal, install the `python-chess` library:

pip install python-chess


### 🐧 Linux:

#### 1. **Ensure Python and pip are Installed**:

Pop open the terminal and check if you have Python and pip:

sudo apt update
sudo apt install python3 python3-pip


#### 3. **Install python-chess**:

With `pip3` installed, proceed to get the `python-chess` library:

pip3 install python-chess


## ✅ Verifying Installation

Post-installation, confirm that `python-chess` is properly installed:

- **Windows**:

python -c "import chess; print(chess.version)"


- **Linux**:

python3 -c "import chess; print(chess.version)"


If all is well, this should output the version number of the `python-chess` library you just installed.

---

**Happy coding and enjoy your chess games!** 🎉
