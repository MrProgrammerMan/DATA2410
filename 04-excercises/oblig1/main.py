def read_students(file_path):
	try:
		f = open(file_path).read()
		return f.split("\n")
	except FileNotFoundError:
		print(f"File {file_path} not found")


print(read_students("input.txt"))
