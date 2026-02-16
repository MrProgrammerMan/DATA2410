def read_students(file_path):
	try:
		f = open(file_path).read()
		if len(f.strip()) == 0:
			print(f"File {file_path} is empty")
			return
		lines = f.split("\n")
		return lines
	except FileNotFoundError:
		print(f"File {file_path} not found")

def process_students(lines):
	lines_split = list(map(lambda s: s.split(','), lines))

	l_valid = lambda l: len(l) == 3	and l[2].isdigit() # check for correct length and 3rd item number

	lines_invalid = list(filter(lambda l: not l_valid(l) and list_has_non_whitespace(l), lines_split)) # the second check makes the reject output cleaner
	lines_valid = filter(l_valid, lines_split)

	if lines_invalid:
		print(f"Rejected the following invalid line(s): {lines_invalid}")

	return list(map(lambda l: (l[0], l[1], int(l[2])), lines_valid))

def list_has_non_whitespace(list):
	return any(len(s.strip()) > 0 for s in list)

def calculate_grade(marks):
	if marks >= 90:
		return 'A'
	if marks >= 80:
                return 'B'
	if marks >= 60:
                return 'C'
	return 'D'

def write_results(file_path, students):
	students_out = format_student_grades(students)
	with open(file_path, 'w') as file:
		file.write(str(students_out))

def format_student_grades(students):
	return '\n'.join(','.join(map(str, s)) for s in students)

def grade_students(students):
	return list(map(
                lambda s: (s[1], s[2], calculate_grade(s[2])),
                students
        ))

def print_report(results):
	print("*** Students grades report ***")
	print(f"Total Students: {len(results)}")
	marks = [student[1] for student in results]
	print(f"Average Marks: {sum(marks)/len(marks)}")
	for grade in ['A', 'B', 'C', 'D']:
		count = len(list(filter(lambda s: s[2] == grade, results)))
		print(f"Number of {grade} Grades: {count}")
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")

results = grade_students(process_students(read_students(input_file_path)))

print_report(results)

write_results(output_file_path, results)
