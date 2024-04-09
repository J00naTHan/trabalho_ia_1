while True:
	try:
		file = input('Informe o nome do arquivo: ')
		if not file.endswith('.txt'):
			file += '.txt'

		with open(file) as f:
			lines = f.readlines()
			nodes = []
			edges = []
			count = 0

			nmrNodes = None
			nmrEdges = None

			for line in lines:
				line = line.strip().split(' ')
				if len(line) == 1 and count == 0:
					nmrNodes = line[0]
					count += 1
				elif len(line) == 1 and count == 1:
					nmrEdges = line[0]
					count += 1
				else:
					if count == 1:
						nodes.append(line)
					elif count == 2:
						edges.append(line)
			f.close()
	except:
		continue
