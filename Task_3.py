import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def list_structure(directory_path):
    path = Path(directory_path)
    
    if not path.exists() or not path.is_dir():
        print(Fore.RED + "Помилка: Шлях не існує або не є директорією.")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + f"📁 {item.name}")
        else:
            print(Fore.GREEN + f"📜 {item.name}")


def main():
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Використання: python task3.py <шлях_до_директорії>")
    else:
        list_structure(sys.argv[1])


if __name__ == "__main__":
    main()
