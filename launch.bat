@echo off
cd /d "%~dp0"
start "" pythonw "%~dp0app.py"
if %errorlevel% neq 0 (
    python "%~dp0app.py"
)
