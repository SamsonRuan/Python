#exception test
try:
	#f=open("abc.txt","r")
	#print(num)
	print("what?")
except FileNotFoundError:
	print("can not found file")
except (IOError,NameError):
	print("IO,NameError happend")
except Exception:
	print("another error")
else:
	print("nothing happend")
finally:
	#f.close()
	print("hello , print")
