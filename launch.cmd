@echo off
setlocal EnableExtensions

REM Keep window open when double-clicked
if "%~1"=="" (
  cmd /k ""%~f0" __inner"
  exit /b
)

set "COMPOSEDIR=%~dp0"
cd /d "%COMPOSEDIR%" || (
  echo Failed to access project folder.
  pause
  exit /b 1
)

echo.
echo Starting Docker containers...
docker compose up -d
if errorlevel 1 (
  echo.
  echo ERROR: Docker failed to start.
  echo Is Docker Desktop running?
  pause
  exit /b 1
)

REM ---- detect host port mapped to container port 9090 ----
for /f "delims=" %%p in ('docker compose port pytf 8080') do set "PORTLINE=%%p"
for /f "tokens=2 delims=:" %%a in ("%PORTLINE%") do set "HOSTPORT=%%a"
set "URL=http://localhost:%HOSTPORT%/"

echo.
echo Opening code-server in Microsoft Edge: %URL%
echo.
echo ONE-TIME STEP:
echo   In Edge click the three dots (...) 
echo   Click: More Tools
echo   Click: Apps
echo   Click: Install code-server
echo.
echo.

REM Locate Edge
set "EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if not exist "%EDGE%" set "EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"

if exist "%EDGE%" (
  start "" "%EDGE%" "%URL%"
) else (
  start "" "%URL%"
)

pause
