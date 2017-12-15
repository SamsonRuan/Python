#exception test2
def test1():
	print("----1-----")
	print(11/0)
	print("----2-----")
def test2():
	print("====1=====")
	test1()
	print(num)
	print("====2=====")
def test3():
	try:
		print("-------11-----")
		test2()
		print("-------22-----")
	except (NameError,IOError) as result:
		print("find a error")
		print(result)
	except Exception as result:
		print("another error")
		print(result)
	finally:
		print("hello,i am good")
test3()	
		