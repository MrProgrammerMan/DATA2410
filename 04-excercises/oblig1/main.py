def read_students(file_path):
	try:
		f = open(file_path).read()
		if not f:
			print(f"File {file_path} is empty")
			return
		lines = f.split("\n")
		return lines
	except FileNotFoundError:
		print(f"File {file_path} not found")

def process_students(lines):
	lines_split = map(lambda s: s.split(','), lines)
	lines_correct_length = filter(lambda l: len(l) == 3, lines_split)
	lines_valid = filter(lambda l: l[2].isdigit(), lines_correct_length)
	lines_tuples = list(map(lambda l: (l[0], l[1], int(l[2])), lines_valid))
	return lines_tuples


print(process_students(read_students("input.txt")))
