@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

python daily_auto_snapshot.py --force
if errorlevel 1 (
  echo [ERROR] 일일 자동 실행 실패
  exit /b 1
)

echo [OK] 일일 자동 실행 완료
exit /b 0
