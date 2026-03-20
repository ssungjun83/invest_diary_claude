@echo off
setlocal
cd /d "%~dp0"

set "PY=python"
where py >nul 2>nul
if %errorlevel%==0 set "PY=py"

echo [1/2] Installing dependencies...
%PY% -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Failed to install dependencies.
  pause
  exit /b 1
)

echo.
echo [2/2] Starting Streamlit app...
%PY% -m streamlit run app.py

if errorlevel 1 (
  echo.
  echo Streamlit exited with an error.
)

pause
