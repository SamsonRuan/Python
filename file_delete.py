import os
addr = input("请输入文件地址:")
os.chdir(addr)
for file in os.listdir():
	if ".mp3" not in file:
		os.remove(file)