call ".venv\Scripts\pyinstaller.exe" --specpath "build" --onefile --noconsole --icon "logo.ico" -n "The letter editor" main.py
rd /S /Q "build"