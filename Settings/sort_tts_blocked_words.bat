@echo off
setlocal EnableExtensions

cd /d "%~dp0"

if not exist "TTS-Blocked-Words.txt" (
  echo File not found: "%~dp0TTS-Blocked-Words.txt"
  pause
  exit /b 1
)

if not exist "sort_tts_blocked_words.py" (
  echo File not found: "%~dp0sort_tts_blocked_words.py"
  pause
  exit /b 1
)

py -3 "sort_tts_blocked_words.py"
if errorlevel 1 (
  echo.
  echo Failed. Make sure Python is installed and the "py" launcher works.
  pause
  exit /b 1
)

pause
endlocal
