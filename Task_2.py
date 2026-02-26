
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    cat_id, name, age = line.split(',')
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    continue

        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []
