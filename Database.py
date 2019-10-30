import Record as re
import re as matchs

class Database:
	def __init__(self,record = re.Record(),currentNum = -1,currentFileName = None):
		self.record = [record]
		self.currentNum = currentNum
		self.currentFileName = currentFileName

	def insertData(self):
		while True:
			recordInp = re.Record()
			if self.putRecord(recordInp): break
			else : 
				if self.currentNum < 0:
					self.currentNum = 0
					self.record[0] = recordInp
				else:
					self.record.append(recordInp)
					self.currentNum += 1
	
	
	def putRecord(self,recordInp):
		print('Enter Following Informations: ')
		print('\tEnglish/Japanese Name, Zip, Address, Tel and E-mail')
		while True:
			r_name=input('English Name (Family & First name) >>> ')
			if not r_name:
				exit=input('End? (y/n) :: ')
				if exit=='y': return True
			break;
		recordInp.setRname(r_name)
		self.strGets('Japanese Name >>> ',recordInp.setName)
		self.strGets('Zip code >>> ',recordInp.setZips)
		self.strGets('Address >>> ',recordInp.setAdd)
		self.strGets('Telephone No. >>> ',recordInp.setPhoneno)
		self.strGets('E-mail >>> ',recordInp.setEmail)
		return False
		

	def strGets(self, string, func):
		x = input(string)
		func(x)
		
	def printData(self, cp):
		print()
		
	def deleteData(self):
		print()
		
		
	def saveDataBase(self, cp):
		if self.currentNum != -1:
			
			print('レコードの数',len(self.record))
			
			if cp == '':
				if currentFileName == None:
					print('ファイル名を入力してください\n')
					currentFileName = input('>> ')
				f = open(currentFileName,'w')
			else:
				currentFileName = cp
				f = open(cp,'w')
				
			que = input('keyを入力しますか？>>> y/n')
			if que == 'y':
				key = input('>> ')
				for i in range(len(self.record)):
					recordall = self.record[i].r_name+self.record[i].name+self.record[i].zips+self.record[i].add+self.record[i].phoneno+self.record[i].email
					match = matchs.search(key,recordall)
					if match:
						f.write(self.record[i].r_name)
						f.write('\n')
						f.write(self.record[i].name)
						f.write('\n')
						f.write(self.record[i].zips)
						f.write('\n')
						f.write(self.record[i].add)
						f.write('\n')
						f.write(self.record[i].phoneno)
						f.write('\n')
						f.write(self.record[i].email)
						f.write('\n@\n')
			else:
				for i in range(len(self.record)):
					f.write(self.record[i].r_name)
					f.write('\n')
					f.write(self.record[i].name)
					f.write('\n')
					f.write(self.record[i].zips)
					f.write('\n')
					f.write(self.record[i].add)
					f.write('\n')
					f.write(self.record[i].phoneno)
					f.write('\n')
					f.write(self.record[i].email)
					f.write('\n@\n')

						
			f.close

		
		
	def loadDataBase(self, cp):
		return 0
		
	def findData(self, cp):
		print()
	
