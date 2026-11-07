@echo off
echo [%DATE% %TIME%] Setting up your clean project environment...

:: 1. Create Virtual Environment
python -m venv .venv
echo [+] Virtual environment (.venv) created successfully.

:: 2. Create requirements.txt if not exists
if not exist requirements.txt (
    echo fastapi> requirements.txt
    echo uvicorn>> requirements.txt
    echo requests>> requirements.txt
    echo [+] requirements.txt created with default packages.
)

:: 3. Create a basic main.py template if not exists
if not exist main.py (
    echo from fastapi import FastAPI> main.py
    echo app = FastAPI()>> main.py
    echo.>> main.py
    echo @app.get("/")>> main.py
    echo def read_root():>> main.py
    echo     return {"message": "BEright Automation Agent is Live!"}>> main.py
    echo [+] main.py template created successfully.
)

:: 4. Create .gitignore to ignore virtual environment
if not exist .gitignore (
    echo .venv/> .gitignore
    echo __pycache__/>> .gitignore
    echo [+] .gitignore created.
)

echo.
echo [%DATE% %TIME%] Project setup is 100% complete and ready!
pause