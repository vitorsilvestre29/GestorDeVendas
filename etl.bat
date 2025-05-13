@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python etl\extract.py
python etl\transform.py
python etl\load.py
pause
