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


print(read_students("input.txt"))
