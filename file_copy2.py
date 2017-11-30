old_file_name = input("请输入想要复制的文件名：")
#得到新文件名
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position]+"-副本"+old_file_name[position:]
f_read = open(old_file_name,"r")
f_write = open(new_file_name,"w")
#文件过大时，可以使用逐行读写
while True:
	content = f_read.readline()
	#当readline方法读到最后一行，并且再次想要读取时，会返回空字符串
	if content == "":
		break
	f_write.write(content)
	
f_read.close()
f_write.close()

