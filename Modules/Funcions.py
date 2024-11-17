from pathlib import Path

directory = Path("./Files")
def listFile():
    for index, file_path in enumerate(directory.iterdir()):
        if file_path.is_file() and file_path.suffix == ".txt":
            print(str(index + 1) + ") - " +file_path.name)

def cancella(indice):
    lista_file = [file.name for file in directory.iterdir() if file.is_file()]
    try:
        file_path = directory / f"{lista_file[indice-1]}"
        if file_path.exists():
            file_path.unlink()
            print(f"File '{file_path}' cancellato.")
        else:
            print(f"File '{file_path}' non esiste.")
        input()
    except IndexError:
        print("-" * 31)
        print("L'elemento non esiste")
        input()


def init():
    if not directory.exists():
        directory.mkdir(parents=True)

def crea_file(filename):
    file_path = directory / f"{filename}.txt"
    file_path.touch(exist_ok=True)
    print(f"File creato: {file_path}")