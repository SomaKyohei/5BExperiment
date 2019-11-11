import Record as re
import re as matchs
import os

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
		if cp == '':
			print(self.record[self.currentNum].r_name)
			print(self.record[self.currentNum].name)
			print(self.record[self.currentNum].zips)
			print(self.record[self.currentNum].add)
			print(self.record[self.currentNum].phoneno)
			print(self.record[self.currentNum].email)
			print('@')
		else:
			if cp == '#':
				print(self.record[len(self.record) - 1].r_name)
				print(self.record[len(self.record) - 1].name)
				print(self.record[len(self.record) - 1].zips)
				print(self.record[len(self.record) - 1].add)
				print(self.record[len(self.record) - 1].phoneno)
				print(self.record[len(self.record) - 1].email)
				print('@')
			elif cp == '+':
				if self.currentNum >= len(self.record)-1:
					print('error : can not go ahead')
				else:
					self.currentNum += 1
					print(self.record[self.currentNum].r_name)
					print(self.record[self.currentNum].name)
					print(self.record[self.currentNum].zips)
					print(self.record[self.currentNum].add)
					print(self.record[self.currentNum].phoneno)
					print(self.record[self.currentNum].email)
					print('@')
			elif cp == '-':
				if self.currentNum <= 0:
					print('error : can not go back')
				else:
					self.currentNum -= 1
					print(self.record[self.currentNum].r_name)
					print(self.record[self.currentNum].name)
					print(self.record[self.currentNum].zips)
					print(self.record[self.currentNum].add)
					print(self.record[self.currentNum].phoneno)
					print(self.record[self.currentNum].email)
					print('@')
			else:
				while self.currentNum + 1 < int(cp):
					self.currentNum += 1
				while self.currentNum + 1 > int(cp):
					self.currentNum -= 1
				print(self.record[self.currentNum].r_name)
				print(self.record[self.currentNum].name)
				print(self.record[self.currentNum].zips)
				print(self.record[self.currentNum].add)
				print(self.record[self.currentNum].phoneno)
				print(self.record[self.currentNum].email)
				print('@')		

	def deleteData(self):
		self.record.pop(self.currentNum)
		
		
	def saveDataBase(self, cp):
		if self.currentNum != -1:
			
			print('レコードの数',len(self.record))
			
			if cp == '':
				if self.currentFileName == None:
					print('ファイル名を入力してください\n')
					self.currentFileName = input('>> ')
				f = open(self.currentFileName,'w')
			else:
				self.currentFileName = cp
				f = open(cp,'w')
				
			que = input('keyを入力しますか？ y/n >>')
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
		path = cp
		loaddata = ["a"]
		if os.path.isfile(path):
			with open(path) as f:
				loaddata = [s.strip() for s in f.readlines()]

		def split_list(l, n):
			for idx in range(0, len(l), n):
				yield l[idx:idx + n]
	
		result = list(split_list(loaddata, 7))

		temp_record = [re.Record(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])]

		for i in range(len(result)):
			if i != 0:
				record = re.Record(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4], result[i][5])
				temp_record.append(record)
			
		self.record = temp_record
		self.currentNum = len(self.record)
		self.currentFileName = path	
		
		
	def findData(self, cp):
		print()
	
