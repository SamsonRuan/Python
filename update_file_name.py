import os
file_addr = input("请输入文件地址：")
os.chdir(file_addr)
for temp in os.listdir(".\\"):
	if " - 副本" in temp:
		position = temp.rfind(".")
		new_file_name = temp[:position-5]+temp[position:]
		os.rename(temp,new_file_name)

		