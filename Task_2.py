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
                    cats_info.append({
                        "id": cat_id, 
                        "name": name, 
                        "age": age
                    })
                except ValueError:
                    continue
        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []


def main():
    cats = get_cats_info("cats.txt")
    print(cats)


if __name__ == "__main__":
    main()
