# --- Saraksti ---

print("--- Saraksti ---")

# Izveido sarakstu ar 5+ skaitļiem
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pievieno elementu
numbers.append(10)

# Dzēš pēdējo elementu
numbers.pop()

# Aprēķina summu ar for ciklu
total = 0
count = 0

for num in numbers:
    total += num
    count += 1

average = total / count

print(f"Summa: {total}, Vidējais: {average}")

# Filtrē pāra skaitļus
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Pāra skaitļi: {even_numbers}")

# Demonstrē slice
print(f"Pirmie 3: {numbers[:3]}")
print(f"Pēdējie 2: {numbers[-2:]}")
print(f"Katrs otrais: {numbers[::2]}")


# --- Vārdnīcas ---

print("\n--- Vārdnīcas ---")

# Izveido vārdnīcu
students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

# Pievieno studentu
students["Pēteris"] = 88

# Izmaina atzīmi
students["Jānis"] = 75

# Izdrukā visus studentus
for name, grade in students.items():
    print(f"{name}: {grade}")

# Atrod studentu ar augstāko atzīmi
best_student = ""
best_grade = 0

for name, grade in students.items():
    if grade > best_grade:
        best_grade = grade
        best_student = name

print(f"Labākais students: {best_student} ({best_grade})")


# --- Kombinācija: saraksts ar vārdnīcām ---

print("\n--- Studenti ar atzīmi >= 80 ---")

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 75},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 88}
]

# Filtrē studentus ar atzīmi >= 80
good_students = []

for student in student_list:
    if student["grade"] >= 80:
        good_students.append(student)

# Izvada ar enumerate
for i, student in enumerate(good_students, start=1):
    print(f"{i}. {student['name']} — {student['grade']}")
    