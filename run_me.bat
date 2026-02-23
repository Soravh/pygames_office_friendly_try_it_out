<<<<<<< HEAD
@echo off
setlocal
title Retro Arcade Installer and Launcher

:: 1. Check if Python is installed
echo Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is NOT installed.
    echo Downloading Python installer...
    
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe' -OutFile 'python_installer.exe'"
    
    echo Installing Python... Please wait.
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    del python_installer.exe
    echo Python installation complete. 
    echo Please RESTART this script to refresh system paths.
    pause
    exit
) else (
    echo [OK] Python is already installed.
)

:: 2. Check for Pygame
echo Checking for Pygame...
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo Pygame NOT found. Installing now...
    python -m pip install pygame
    if %errorlevel% neq 0 (
        echo Failed to install Pygame. Check your internet connection.
        pause
        exit
    )
    echo [OK] Pygame installed successfully.
) else (
    echo [OK] Pygame is already installed.
)

:: 3. Selection Menu
:menu
cls
echo ==========================================
echo           RETRO ARCADE MENU
echo ==========================================
echo.
echo  1) Launch Snake Game
echo  2) Launch Breakout (TNT Edition)
echo  Q) Quit
echo.
echo ==========================================
set /p choice="Select an option (1, 2, or Q): "

if "%choice%"=="1" goto run_snake
if "%choice%"=="2" goto run_breakout
if /i "%choice%"=="Q" exit
echo Invalid selection, please try again.
pause
goto menu

:run_snake
if exist snake_game.py (
    echo Launching Snake...
    python snake_game.py
) else (
    echo Error: snake_game.py not found in this folder!
    pause
)
goto menu

:run_breakout
if exist breakout.py (
    echo Launching Breakout...
    python breakout.py
) else (
    echo Error: breakout.py not found in this folder!
    pause
)
=======
@echo off
setlocal
title Retro Arcade Installer and Launcher

:: 1. Check if Python is installed
echo Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is NOT installed.
    echo Downloading Python installer...
    
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe' -OutFile 'python_installer.exe'"
    
    echo Installing Python... Please wait.
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    del python_installer.exe
    echo Python installation complete. 
    echo Please RESTART this script to refresh system paths.
    pause
    exit
) else (
    echo [OK] Python is already installed.
)

:: 2. Check for Pygame
echo Checking for Pygame...
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo Pygame NOT found. Installing now...
    python -m pip install pygame
    if %errorlevel% neq 0 (
        echo Failed to install Pygame. Check your internet connection.
        pause
        exit
    )
    echo [OK] Pygame installed successfully.
) else (
    echo [OK] Pygame is already installed.
)

:: 3. Selection Menu
:menu
cls
echo ==========================================
echo           RETRO ARCADE MENU
echo ==========================================
echo.
echo  1) Launch Snake Game
echo  2) Launch Breakout (TNT Edition)
echo  3) Launch Highway Car
echo  4) Launch Space Shooter
echo  Q) Quit
echo.
echo ==========================================
set /p choice="Select an option (1, 2, 3, 4, or Q): "

if "%choice%"=="1" goto run_snake
if "%choice%"=="2" goto run_breakout
if "%choice%"=="3" goto run_car
if "%choice%"=="4" goto run_space
if /i "%choice%"=="Q" exit

echo Invalid selection, please try again.
pause
goto menu

:run_snake
if exist snake_game.py (
    echo Launching Snake...
    python snake_game.py
) else (
    echo Error: snake_game.py not found!
    pause
)
goto menu

:run_breakout
if exist breakout.py (
    echo Launching Breakout...
    python breakout.py
) else (
    echo Error: breakout.py not found!
    pause
)
goto menu

:run_car
if exist highway_car.py (
    echo Launching Highway Car...
    python highway_car.py
) else (
    echo Error: highway_car.py not found!
    pause
)
goto menu

:run_space
if exist space_shooter.py (
    echo Launching Space Shooter...
    python space_shooter.py
) else (
    echo Error: space_shooter.py not found!
    pause
)
>>>>>>> 5571346 (Initial commit: Added 4 retro games and arcade launcher)
goto menu