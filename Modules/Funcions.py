from pathlib import Path

directory = Path("./Files")
def listFile():
    for file_path in directory.iterdir():
        if file_path.is_file():
            print(file_path.name)

def init():
    if not directory.exists():
        directory.mkdir(parents=True)

def crea_file(filename):
    file_path = directory / f"{filename}.txt"
    file_path.touch(exist_ok=True)
    print(f"File creato: {file_path}")