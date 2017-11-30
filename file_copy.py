
old_file_name = input("请输入你想要拷贝的文件的文件名：")
f_read = open(old_file_name,"rb")
content = f_read.read()
index = old_file_name.rfind(".")#rfind()函数可以找到参数对应的下标，并且加r表示从右往左
new_file_name = old_file_name[:index]+"-副本"+old_file_name[index:]#找到下标以后，根据这个下标对原文件名进行切片，
#插入"-副本"后，再次进行切片即可
f_write = open(new_file_name,"wb")
f_write.write(content)
f_read.close()
f_write.close()




 