import os
file_addr = input("请输入文件地址：")
os.chdir(file_addr)
for old_file in os.listdir():
	if " - 副本" in old_file:
		position = old_file.rfind(".")
		new_file = old_file[:position-5]+old_file[position:]
		f_read = open(old_file,"rb")
		f_write = open(new_file,"wb")
		content = f_read.read()
		f_write.write(content)
		f_read.close()
		f_write.close()
			