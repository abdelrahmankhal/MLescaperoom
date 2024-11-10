data = { 'homework_score': [40, 60, 80], 'exam_score': [70, 85, 90] }
performance_index = [hw * exam for hw, exam in zip(data['homework_score'], data['exam_score'])]
print(f"Performance Index (Homework * Exam): {performance_index}")
