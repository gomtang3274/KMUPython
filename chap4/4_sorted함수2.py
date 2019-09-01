student = [
    ("허준녕", 20153253, 4.2),
    ("김영재", 20153180, 3.7),
    ("한채연", 20153250, 4.5),
]

print("Before sorted :", student)
sort_by_id = sorted(student, key=lambda x: x[1])
print("Sort by id :", sort_by_id)
sort_by_grade = sorted(student, key=lambda x: x[2], reverse=True)
print("Sort by grade :", sort_by_grade)
