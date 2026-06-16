pyinstaller --onefile --noconsole --icon "logo.ico" -n "The letter editor" main.py
rd /S /Q "build"
del /Q "The letter editor.spec"
