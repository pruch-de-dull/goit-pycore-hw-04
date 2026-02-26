def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary_str = line.split(',')
                    total_salary += int(salary_str)
                    num_developers += 1
                except ValueError:
                    continue

        if num_developers == 0:
            return 0, 0

        average_salary = total_salary / num_developers
        return total_salary, int(average_salary)

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return 0, 0
