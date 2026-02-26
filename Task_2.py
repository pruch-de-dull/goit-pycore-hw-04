import pathlib

def get_cats_info(path):
    cats_info = []
    try:
        path = pathlib.Path(path)
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    cat_id, name, age = line.split(',')
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Попередження: Некоректний формат рядка: '{line}'")
                    continue
        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

def main():
    path_to_file = "cats.txt"
    cats = get_cats_info(path_to_file)
    if cats:
        print(f"Знайдено інформацію про {len(cats)} котів:")
        print(cats)

if __name__ == "__main__":
    main()
