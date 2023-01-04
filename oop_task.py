class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def marking_grade_for_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.list_grades:
                lecturer.list_grades[course] += [grade]
            else:
                lecturer.list_grades[course] = [grade]
        else:
            return 'Ошибка'

    def mean_grade(self):
        mean = sum(sum(self.grades.values(), [])) / \
               len(sum(self.grades.values(), []))
        return mean

    def __eq__(self, other):
        return self.mean_grade() == other.mean_grade()

    def __ne__(self, other):
        return self.mean_grade() != other.mean_grade()

    def __lt__(self, other):
        return self.mean_grade() < other.mean_grade()

    def __gt__(self, other):
        return self.mean_grade() > other.mean_grade()

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: " \
               f"{round(self.mean_grade(), 1)}" \
               f"\nКурсы в процессе изучения:  " \
               f"{', '.join(self.courses_in_progress)}" \
               f"\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.list_grades = {}
        self.list_lecturer = {}

    def average_grade(self):
        average = sum(sum(self.list_grades.values(), [])) / \
                  len(sum(self.list_grades.values(), []))
        return average

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def half_value(self):
        pass

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за лекции: " \
               f"{round(self.average_grade(), 1)} \n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hm(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname} \n"


student_1 = Student('Lydia', 'Martin', 'female')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.courses_in_progress += ['C++']
student_1.courses_in_progress += ['C']
student_1.finished_courses += ['Russian language']
student_1.finished_courses += ['Physical']

student_2 = Student('Scott', 'McCall', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Pascal']
student_2.finished_courses += ['English language']
student_2.finished_courses += ['Mathematic']

lecturer_1 = Lecturer('Derek', 'Hale')
lecturer_1.courses_attached += ['C++']
lecturer_1.courses_attached += ['C']
lecturer_2 = Lecturer('Jackson', 'Whittemore')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Stiles', 'Stilinski')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['C++']
reviewer_2 = Reviewer('Chris', 'Argent')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['Pascal']

student_1.marking_grade_for_lecturer(lecturer_2, 'Python', 8)
student_1.marking_grade_for_lecturer(lecturer_2, 'Git', 10)
student_1.marking_grade_for_lecturer(lecturer_1, 'C++', 7)
student_1.marking_grade_for_lecturer(lecturer_1, 'C', 6)

student_2.marking_grade_for_lecturer(lecturer_1, 'C++', 9)
student_2.marking_grade_for_lecturer(lecturer_2, 'Python', 9)
student_2.marking_grade_for_lecturer(lecturer_2, 'Git', 9)

reviewer_1.rate_hm(student_2, 'Python', 7)
reviewer_1.rate_hm(student_2, 'C++', 9)
reviewer_1.rate_hm(student_1, 'Python', 10)
reviewer_1.rate_hm(student_1, 'C++', 9)

reviewer_2.rate_hm(student_1, 'Git', 8)
reviewer_2.rate_hm(student_2, 'Git', 7)
reviewer_2.rate_hm(student_2, 'Pascal', 10)

list_students = [student_1, student_2]
list_lecturer = [lecturer_1, lecturer_2]


def half_value_grade_student(list_student, course):
    entirety = 0
    length = 0
    for student in list_student:
        if course in student.grades:
            entirety += sum(student.grades[course])
            length += len(student.grades[course])
        else:
            return 'Error!'
    return f'Средняя оценка студентов за курс: {course}: {entirety / length} '


def half_value_grade_lecturer(list_lec, course):
    entirety = 0
    length = 0
    for lecturer in list_lec:
        if course in lecturer.list_grades:
            entirety += sum(lecturer.list_grades[course])
            length += len(lecturer.list_grades[course])
    return f'Средняя оценка лекторов за курс: {course}: {entirety / length}'


print(student_1.grades)
print(student_2.grades)
print()
print(lecturer_1.list_grades)
print(lecturer_2.list_grades)
print()
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(student_1 == student_2)
print(student_1 != student_2)
print(student_2 != student_1)
print(student_1 > student_2)
print(student_2 > student_1)
print(student_1 < student_2)
print(student_2 < student_1)

print(lecturer_1 == lecturer_2)
print(lecturer_2 != lecturer_1)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_2 > lecturer_1)
print(lecturer_2 < lecturer_1)
print()
print(half_value_grade_student(list_students, 'Python'))
print(half_value_grade_student(list_students, 'C++'))
print()
print(half_value_grade_lecturer(list_lecturer, 'C++'))
print(half_value_grade_lecturer(list_lecturer, 'Python'))
