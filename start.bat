@echo off
:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python.
    pause
    exit /b
)

:: Check if pyautogui is installed
python -c "import pyautogui" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pyautogui is not installed. Installing it now...
    python -m pip install pyautogui
)

:: Run the Python script
echo Running your Python script...
python main.py

pause
