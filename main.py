#Определяем классы
class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        result = f'Name: {self.name}\nSurname: {self.surname}\nAverage grade for homeworks: {self.average_grade()}\nCourses in progress: {", ".join(self.courses_in_progress)}\nCourses finished: {", ".join(self.finished_courses)}\n'
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Error! This is not student.')
            return
        return self.average_grade < other.average_grade

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_course(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.course_grades.keys():
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Error! Lecturer does not teach at course.'
    
    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        result = sum(all_grades) / len(all_grades)
        return result

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def __str__(self):
        result = f'Name: {self.name}\nSurname: {self.surname}\nAverage grade of lectures: {self.average_grade()}\n'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Error! This is not lecturer.')
            return
        return self.average_grade < other.average_grade

    def average_grade(self):
        all_grades = [grade for grades in self.course_grades.values() for grade in grades]
        result = sum(all_grades) / len(all_grades)
        return result

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error! The student did not finished this course yet.'

    def __str__(self):
        result = f'Name: {self.name}\nSurname: {self.surname}\n'
        return result

#Реализуем две функции из четвертого задания
def average_course_grade_by_student(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades.keys():
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
            # print(f'Course {course}, grades {student.grades[course]}')
    result = total_grades / total_count
    return result

def average_course_grade_by_lecturer(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.course_grades.keys():
            total_grades += sum(lecturer.course_grades[course])
            total_count += len(lecturer.course_grades[course])
            # print(f'Course {course}, grades {lecturer.course_grades[course]}')
    result = total_grades / total_count
    return result

#Создаем по два экземпляра студента, лектора и проверяющего и предварительно наполняем
first_student = Student('Harry', 'Potter', 'Male')
first_student.courses_in_progress += ['Defence against the dark arts']
first_student.courses_in_progress += ['Potion-making']
first_student.finished_courses += ['Flying']
first_student.finished_courses += ['Transfiguration']
first_student.grades['Flying'] = [6, 9, 8 ,8, 7]

second_student = Student('Hermione', 'Granger', 'Female')
second_student.courses_in_progress += ['Defence against the dark arts']
second_student.courses_in_progress += ['Potion-making']
second_student.finished_courses += ['Herbology']
second_student.finished_courses += ['History of Magic']
second_student.grades['Herbology'] = [10, 10, 9, 8]
 
first_lecturer = Lecturer('Severus', 'Snape')
first_lecturer.courses_attached += ['Defence against the dark arts']
first_lecturer.courses_attached += ['Flying']
first_lecturer.courses_attached += ['Transfiguration']

second_lecturer = Lecturer('Horace', 'Slughorn')
second_lecturer.courses_attached += ['Potion-making']
second_lecturer.courses_attached += ['Herbology']
second_lecturer.courses_attached += ['History of Magic']

first_reviewer = Reviewer('Dolores', 'Umbridge')
first_reviewer.courses_attached += ['Defence against the dark arts']
first_reviewer.courses_attached += ['Flying']

second_reviewer = Reviewer('Gilderoy', 'Lokhart')
second_reviewer.courses_attached += ['Potion-making']
second_reviewer.courses_attached += ['Herbology']

#Ставим оценки лекторам
first_student.rate_course(first_lecturer, 'Flying', 9)
first_student.rate_course(first_lecturer, 'Flying', 6)
first_student.rate_course(first_lecturer, 'Defence against the dark arts', 7)
first_student.rate_course(first_lecturer, 'Transfiguration', 8)
first_student.rate_course(first_lecturer, 'Herbology', 9)

second_student.rate_course(second_lecturer, 'Potion-making', 9)
second_student.rate_course(second_lecturer, 'Herbology', 7)
second_student.rate_course(second_lecturer, 'Defence against the dark arts', 8)
second_student.rate_course(second_lecturer, 'History of Magic', 3)


#Проверяем работы по предметам
first_reviewer.rate_hw(first_student, 'Flying', 10)
first_reviewer.rate_hw(first_student, 'Herbology', 4)

second_reviewer.rate_hw(second_student, 'Herbology', 9)
second_reviewer.rate_hw(second_student, 'Flying', 1)



print(first_student)
print(second_student)

print(first_lecturer)
# print(first_lecturer.course_grades)
print(second_lecturer)
# print(second_lecturer.course_grades)

print(first_reviewer)
print(second_reviewer)

#Проверяем работу функций
st_list = [first_student, second_student]
course = 'Flying'
print(f'Average students grade of the {course} course is {average_course_grade_by_student(st_list, course)}')

lc_list = [first_lecturer, second_lecturer]
course = 'Flying'
print(f'Average lecturers grade of the {course} course is {average_course_grade_by_lecturer(lc_list, course)}')

