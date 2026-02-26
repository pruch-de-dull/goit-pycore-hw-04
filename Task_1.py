import pathlib


def total_salary(path):
    total_salary_sum = 0
    num_developers = 0

    try:
        path = pathlib.Path(path)
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    # Пропуски після коми для PEP 8
                    name, salary_str = line.split(',')
                    total_salary_sum += float(salary_str)
                    num_developers += 1
                except ValueError:
                    print(f"Попередження: Некоректні дані: '{line}'")
                    continue

        if num_developers == 0:
            return 0, 0

        average_salary = total_salary_sum / num_developers
        return int(total_salary_sum), int(average_salary)

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0


def main():
    total, average = total_salary("salary_file.txt")
    if total > 0:
        print(f"Всього: {total}, Середня: {average}")


if __name__ == "__main__":
    main()
