class Record:
	def __init__(self,r_name = 'rn',name = 'na',zips = 'zi',add = 'ad',phoneno = 'ph',email = 'em'):
		self.r_name = r_name
		self.name = name
		self.zips = zips
		self.add = add
		self.phoneno = phoneno
		self.email = email

	def setRname(self,r_name):
		self.r_name = r_name

	def getRname(self):
		return r_name

	def setName(self,name):
		self.name = name

	def getName(self):
		return name

	def setZips(self,zips):
		self.zips = zips

	def getZips(self):
		return zips

	def setAdd(self,add):
		self.add = add

	def getAdd(self):
		return add

	def setPhoneno(self,phoneno):
		self.phoneno = phoneno

	def getPhoneno(self):
		return phoneno

	def setEmail(self,email):
		self.email = email

	def getEmail(self):
		return email

