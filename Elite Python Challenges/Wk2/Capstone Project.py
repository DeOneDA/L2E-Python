records_1 = [
("ST06", "Python"),
("ST06", "Python"),
("ST07", "Python"),
("ST07", "Python"),
("ST05", "Python"),
("ST05", "Python"),
("ST05", "Python"),
("ST05", "Python"),
("ST01", "Python"),
("ST02", "HTML"),
("ST01", "Python"),
("ST03", "CSS"),
("ST02", "HTML"),
("ST01", "JavaScript"),
("ST03", "CSS"),
("ST01", "Python")
]

records_2 = [
("ST06", "Python"),
("ST06", "Python"),
("ST07", "Python"),
("ST07", "Python"),
("ST05", "Python"),
("ST02", "HTML"),
("ST01", "Python"),
("ST03", "CSS"),
("ST02", "HTML"),
("ST01", "JavaScript"),
("ST03", "CSS"),
("ST01", "Python")
]

records_3 = [
("ST06", "Python"),
("ST06", "Python"),
("ST07", "Python"),
("ST05", "Python"),
("ST05", "Python"),
("ST01", "Python"),
("ST02", "HTML"),
("ST01", "Python"),
("ST03", "CSS"),
("ST02", "HTML"),
("ST01", "JavaScript"),
("ST03", "CSS"),
("ST01", "Python")
]

records_4 = []

records_5 = [("ST11", "HTML")]

def track_calls(func):
    count = 0
    def counter(x):
        nonlocal count
        result = func(x)
        count += 1
        if count >3:
            return result
        print(f"Count: {count}")
        return result
    return counter

@track_calls
def analysis_records(records):
    if len(records) == 0:
        return "Records is empty"

    student_counts = {}
    activity_counts = {}

    for student in records:
        student_id, topic = student
        if student_id in student_counts:
            student_counts[student_id] += 1
        else:
            student_counts[student_id] = 1

        if topic in activity_counts:
            activity_counts[topic] += 1
        else:
            activity_counts[topic] = 1

    most_active_students = []
    count = max(student_counts.values())

    for item, value in student_counts.items():
        if value == count:
            most_active_students.append(item)
    
    most = min(most_active_students)

    return f"""Student Count = {student_counts}
Activity Count = {activity_counts}
Most Active Student = '{most}'"""

print(analysis_records(records_1))
print("~" * 30)
print(analysis_records(records_2))
print("~" * 30)
print(analysis_records(records_3))
print("~" * 30)
print(analysis_records(records_4))
print("~" * 30)
print(analysis_records(records_5))
print("~" * 30)

def count_student_records(records, student_id):
    if not records:
        return 0
        
    student, topic = records[0]

    if student_id == student:
        return 1 + count_student_records(records[1:], student_id)
        
    return 0 + count_student_records(records[1:], student_id)

print(count_student_records(records_1, "ST01"))
print("~" * 30)
print(count_student_records(records_1, "ST20"))