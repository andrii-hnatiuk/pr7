"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).
with open("students.csv", "rt", encoding = "utf-8") as file:
    students_gpa = {}
    math_list = []
    python_list = []
    english_list = []
    l = 0
    next(file)

    for line in file:
        line = line[:-1]
        split = line.split(",")
        name = split[0]
        math = int(split[1])
        python = int(split[2])
        english = int(split[3])
        math_list.append(math)
        python_list.append(python)
        english_list.append(english)
        l += 1
        marks = [int(x) for x in split[1:-1]]
        gpa = sum(marks) / len(marks)
        students_gpa[name] = gpa

    math_avr = sum(math_list) / len(math_list)
    python_avr = sum(python_list) / len(python_list)
    english_avr = sum(english_list) / len(english_list)
    student = max(students_gpa, key=students_gpa.get)

    print("Середній бал по класу:")
    print(f"math: {round(math_avr, 1)}")
    print(f"python: {round(python_avr, 1)}")
    print(f"english: {round(english_avr, 1)}\n")
    print(f"Найкращий студент: {student} ({students_gpa[student]})")

with open("result.txt", "w", encoding="utf-8") as f:

    f.write("Середній бал по класу:\n")
    f.write(f"math: {round(math_avr, 1)}\n")
    f.write(f"python: {round(python_avr, 1)}\n")
    f.write(f"math: {round(english_avr, 1)}\n\n")
    f.write(f"Найкращий студент: {student} ({students_gpa[student]})" )

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
