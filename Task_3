import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_directory_structure(directory: Path, indent: str = ""):
    try:
        items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        for item in items:
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}")
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}🔒 Доступ заборонено")
    except Exception as e:
        print(f"{indent}{Fore.RED}❌ Помилка: {e}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Не вказано шлях до директорії.")
        return

    path_str = sys.argv[1]
    path = Path(path_str)

    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path_str}' не знайдено.")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path_str}' не є директорією.")
        return

    print(f"{Fore.YELLOW}📦 {path.name}")
    print_directory_structure(path)

if __name__ == "__main__":
    main()
