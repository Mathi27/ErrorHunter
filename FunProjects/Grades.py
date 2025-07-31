class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student, grade):
        if isinstance(grade, (int, float)):
            self.grades[student] = grade
            print(student, "Grade is", self.grades[student])
        else:
            print(f"Invalid grade for {student}. Grade must be a number.")

    def calculate_average(self):
        if not self.grades:
            return 0  # Avoid division by zero
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average

# Example Usage
grades = StudentGrades()
grades.add_grade("John", 85)
grades.add_grade("Sarah", 90)
grades.add_grade("Mike", 78)
print("Average grade:", grades.calculate_average())
