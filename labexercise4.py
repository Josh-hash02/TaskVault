course_catalog = [
    ("CS101", "Intro to Python", 4),
    ("MATH201", "Calculus I", 3),
    ("CS102", "Data Structures", 4)
]
student_roster = {
    "S101": {
        "name": "Josh Gabriel Aguila",
        "major": "Cybersecurity",
        "enrolled_courses": ["CS101", "MATH201"]
    },
    "S102": {
        "name": "Chen Jing Ying",
        "major": "Multimedia Arts",
        "enrolled_courses": ["CS101", "CS102"]
    }
}
student1_courses = set(student_roster["S101"]["enrolled_courses"])
student2_courses = set(student_roster["S102"]["enrolled_courses"])

all_unique_courses = student1_courses.union(student2_courses)

common_courses = student1_courses.intersection(student2_courses)

grade_submissions = [
    ("S101", "CS101", "A"),
    ("S101", "MATH201", "B"),
    ("S102", "CS101", "B"),
    ("S102", "CS102", "A")
]


def get_student_gpa(student_id):
    grade_scale = {"A": 4.0, "B": 3.0, "C": 2.0}
    total_points = 0.0
    course_count = 0

    for s_id, course, grade in grade_submissions:
        if s_id == student_id:
            total_points += grade_scale[grade]
            course_count += 1

    if course_count == 0:
        return 0.0

    return total_points / course_count

print("--- Course Catalog ---")
for code, title, credits in course_catalog:
    print(f"{code}: {title} ({credits} credits)")

print("\n--- Enrollment Analytics ---")
print(f"All unique courses being taken: {all_unique_courses}")
print(f"Common courses taken by all students: {common_courses}")

print("\n--- Grade Report ---")
s101_gpa = get_student_gpa("S101")
print(f"Student S101 Final GPA: {s101_gpa:.1f}")