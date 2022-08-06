class Satellite:
	def __init__(self,entry):
		self.id = entry[0]
		self.operator_country = entry[1]
		self.user = entry[2]
		self.purpose = entry[3]
		self.class_type = entry[4]
		self.type = entry[5]
		self.perigee = None if entry[6] == '' else float(entry[6])
		self.apogee = None if entry[7] == '' else float(entry[7])
		self.eccentricity = None if entry[8] == '' else float(entry[8])
		self.period = None if entry[9] == '' else float(entry[9])
		self.launch_mass = None if entry[10] == '' else float(entry[10])
		self.dry_mass =  None if entry[11] == '' else float(entry[11])
		self.power = None if entry[12] == '' else float(entry[12])
		self.date = None if entry[13] == '' else float(entry[13])
		self.expected_lifetime = None if entry[14] == '' else float(entry[14]) 
		self.contractor_country  = entry[15]
		self.launch_site = entry[16]
		self.launch_vehicle = entry[17]
		self.source = entry[18]
		self.longitude = None if entry[19] == '' else float(entry[19])
		self.inclination = None if entry[20] == '' else float(entry[20])

