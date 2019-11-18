# -*- coding: utf_8 -*-
import sys
import traceback
import Database as data

#空白までの文字列を削除
def getArg(string):
<<<<<<< HEAD
	if len(string) > 1:
		while not(string.startswith(' ')):
			string = string[1:]
		string = string[1:]
	else: string = ''
=======
	while not(string.startswith(' ')):
		string = string[1:]
	string = string[1:]
>>>>>>> develop
	return string

#ヘルプの表示
def helpCommand():
	print('I:レコードの追加(insert)\nP:レコードの表示(print)\nD:レコードの削除(delete)\n+,N:次のレコードを表示(next)\n-,B:前のレコードを表示(before)\nL:データベース・ファイルのロード(load)\nS:データベース・ファイルのセーブ(save)\nF:データベースの検索(find)\nQ:データベースシステムの終了(quit)\nH:データベースシステムのコマンドの説明(help)')


#main文

db = data.Database()
#コマンド引数があれば該当するデータベースをロード
argv = sys.argv
argc=len(argv)
if argc>1 :
	root = db.loadDataBase(argv[0])
	if root: print('not find')

while True:
	buf = input('AddressBook>')
	if not buf:
		print('Command : I/P/N/B/L/S/F/Q/Help')
		continue
	ini = buf[0]
	ini = ini.upper()
	if ini == 'I':
		db.insertData()
	elif ini == 'P':
		buf = getArg(buf)
		db.printData(buf)
	elif ini == 'D':
<<<<<<< HEAD
=======
		buf = getArg(buf)
>>>>>>> develop
		db.deleteData()
	elif ini == '+' or ini == 'N':
		buf = getArg(buf)
		db.printData('+')
	elif ini == '-' or ini == 'B':
		buf = getArg(buf)
		db.printData('-')
	elif ini == 'L':
		buf = getArg(buf)
		db.loadDataBase(buf)
	elif ini == 'S':
		buf = getArg(buf)
		db.saveDataBase(buf)
	elif ini == 'F':
		buf = getArg(buf)
		db.findData(buf)
	elif ini == 'Q':
		break;
	elif ini == 'H':
		helpCommand()

