@echo off

echo ===============================
echo Setting up Log Analytics Environment
echo ===============================

echo.
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing dependencies...
pip install -r environment\requirements.txt

echo.
echo ===============================
echo Setup Complete!
echo ===============================

pause
