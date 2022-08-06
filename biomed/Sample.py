class Sample:
	def __init__(self,entry):
		self.observation = int(entry[0])
		self.id = int(entry[1])
		self.age = int(entry[2])
		self.sample_date = int(entry[3])
		self.m1 = float(entry[4])
		self.m2 = None if entry[5] == '?' else float(entry[5])
		self.m3 = float(entry[6])
		self.m4 = None if entry[7] == '?' else int(entry[7])
		self.class_type = entry[8].strip('\n')

