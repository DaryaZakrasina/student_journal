class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades= {}
    
    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def student_grade(self, lecturer, course, grade):
    	if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.student_grades: 
                lecturer.student_grades[course] += [grade]
            else:
                lecturer.student_grades[course] = [grade]
    	else:
    		return "Ошибка"

    def grade_averege(self):
    	from statistics import mean
    	for courses, grade in self.grades.items():
    		avarege_grade = mean(grade)
    		return avarege_grade

    def _str_(self):
    	name_mes = f'Имя: {self.name}'
    	surname_mes = f'Фамилия: {self.surname}'
    	avarege_grade_mes = f'Средняя оценка за домашние задания: {self.grade_averege()}'
    	courses_in_progress_mes = f' Курсы в процессе изучения: {", ".join(self.courses_in_progress)}'
    	finished_course_mes = f' Курсы в процессе изучения: {", ".join(self.finished_courses)}'
    	print(name_mes)
    	print(surname_mes)
    	print(avarege_grade_mes)
    	print(courses_in_progress_mes)
    	print(finished_course_mes)
    
    def _lt_(self, other):
        if not isinstance (other, Student):
        	print("нельзя сравнить")
        elif self.grade_averege() == other.grade_averege():
        	print("успеваемость одинаковая")
        elif self.grade_averege() > other.grade_averege():
            print(f'Успеваемость {self.name} {self.surname} выше')	
        else:
        	print(f'Успеваемость {other.name} {other.surname} выше')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.student_grades = {}
	
	def grade_averege(self):
		from statistics import mean
		for courses, grades in self.student_grades.items():
			avarege_grade = mean(grades)
			return avarege_grade

	def _str_(self):
		name_mes = f'Имя: {self.name}'
		surname_mes = f'Фамилия: {self.surname}'
		avarege_grade_mes = f'Средняя оценка за лекции: {self.grade_averege()}'
		print(name_mes)
		print(surname_mes)
		print(avarege_grade_mes)

	def _lt_(self, other):
		if not isinstance (other, Lecturer):
			print("нельзя сравнить")
		elif self.grade_averege() == other.grade_averege():
			print("оценка одинаковая")
		elif self.grade_averege() > other.grade_averege():
			print(f'{self.name} {self.surname} оценен выше')	
		else:
			print(f'{other.name} {other.surname} оценен выше')			

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'            

    def _str_(self):
    	name_mes = f'Имя: {self.name}'
    	surname_mes = f'Фамилия: {self.surname}'
    	print(name_mes)
    	print(surname_mes)



Peter = Student("Петя", "Кислов", "м")
Peter.courses_in_progress.append("Python")
Peter.courses_in_progress.append("Java")
Ivan = Student("Иван", "Кислый", "м")
Ivan.courses_in_progress.append("Python")

EI = Lecturer("Екатерина Игоревна", "Иванова")
EI.courses_attached.append("Python")
EI.courses_attached.append("Java")
Peter.student_grade(EI, "Python", 10 )
Peter.student_grade(EI, "Java", 10 )
Ivan.student_grade(EI, "Python", 9 )
print(EI.student_grades)


AA = Lecturer("Анна Александровна", "Смирнова")
AA.courses_attached.append("Python")
Peter.student_grade(AA, "Python", 7)
Ivan.student_grade(AA, "Python", 7)
print(AA.name)
print(AA.student_grades)

II = Reviewer("Иван Иванович", "Хороший")
II.courses_attached.append("Python")
II.courses_attached.append("Java")
II.rate_hw(Peter, "Python", 10)
II.rate_hw(Peter, "Java", 9)
II.rate_hw(Ivan, "Python", 9)
II.rate_hw(Ivan, "Python", 9)


VV = Reviewer("Иван Иванович", "Хороший")
VV.courses_attached.append("Python")
VV.rate_hw(Peter, "Python", 10)
VV.rate_hw(Peter, "Python",10)
VV.rate_hw(Ivan, "Python", 10)
VV.rate_hw(Ivan, "Python", 10)

print(Peter.grades)


print(EI.grade_averege())
II._str_()
EI._str_()
print(Peter.grade_averege())
print(Ivan.grade_averege())

Peter._str_()
Peter._lt_(Ivan)
EI._lt_(AA)

student_list = [Peter, Ivan]
lecturer_list = [EI, AA]

def avarege_grades_student(student_list, course_name):
	count = 0
	from statistics import mean
	for student in student_list:
		for course, grades in student.grades.items():
			if course == course_name:
				count += mean(grades)
	avarege = count/len(student_list)
	return avarege

print(avarege_grades_student(student_list, "Python"))

def avarege_grades_lecturer(lecturer_list, course_name):
	count = 0
	from statistics import mean
	for lecturer in lecturer_list:
		for course, grades in lecturer.student_grades.items():
			if course == course_name:
				count += mean(grades)
	avarege = count/len(lecturer_list)
	return avarege

print(avarege_grades_lecturer(lecturer_list, "Python"))	