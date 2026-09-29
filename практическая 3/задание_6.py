name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую, без пробелов между словами): ")
age = int(age_str)
subjects = subjects_str.split(",")
student = {
    "name": name,
    "age": age,
    "subjects": subjects
}
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")
print("=" * 30)