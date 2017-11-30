#这是一个学生管理系统
#2017/10/20
#功能选项模块
print("="*50)
print("功能选项：")
print("1.创建一张名片")
print("2.查询一张名片")
print("3.修改一张名片")
print("4.删除一张名片")
print("5.查看所有名片")
print("6.退出系统")
print("="*50)
#定义一个列表，在这个列表中存储用户的名片信息
infor_list = []

#功能选项实现
while True:
	choice_num = int(input("请输入需要执行的功能："))
	
	if choice_num==1:
		card_name = input("请输入姓名：")
		card_addr = input("请输入地址：")
		card_phone = input("请输入电话：")
		card_job = input("请输入职位：")
		#定义一个字典，在这个字典中，用来存储输入的名片信息
		infor_dict = {}
		#向这个字典中添加信息
		infor_dict["name"]=card_name
		infor_dict["addr"]=card_addr
		infor_dict["phone"]=card_phone
		infor_dict["job"]=card_job
		#将字典存储到上面定义的列表中
		infor_list.append(infor_dict)
		#为了对结果进行测试，将这个列表打印
		print(infor_list)
		
	elif choice_num==2:
	
		print("1.按照姓名查询")
		print("2.按照地址查询")
		print("3.按照电话号码查询")
		print("4.按照工作查询")
		print("5.退出查询")
		
		while True:
		
			query_choice = int(input("想按照什么查询？"))
			if query_choice==1:
				query_name = input("请输入姓名：")
				#设立一个标记，当没有找打人时记为0，找到则记为1.
				flag = 0
				for i in infor_list:
					if i["name"]==query_name:
						print("%s\t%s\t%s\t%s"%("姓名","地址","电话","工作"))
						print("%s\t%s\t%s\t%s"%(i["name"],i["addr"],i["phone"],i["job"]))
						flag=1
				if flag==0:
					print("查无此人...")
			elif query_choice==2:
				query_addr= input("请输入地址：")
				flag = 0
				for i in infor_list:
					if i["addr"]==query_addr:
						print("%s\t%s\t%s\t%s"%("姓名","地址","电话","工作"))
						print("%s\t%s\t%s\t%s"%(i["name"],i["addr"],i["phone"],i["job"]))
						flag=1
				if flag==0:
					print("查无此人...")
			elif query_choice==3:
				query_phone= input("请输入电话：")
				flag = 0
				for i in infor_list:
					if i["addr"]==query_phone:
						print("%s\t%s\t%s\t%s"%("姓名","地址","电话","工作"))
						print("%s\t%s\t%s\t%s"%(i["name"],i["addr"],i["phone"],i["job"]))
						flag=1
				if flag==0:
					print("查无此人...")
			elif query_choice==4:
				query_job= input("请输入工作：")
				flag = 0
				for i in infor_list:
					if i["addr"]==query_job:
						print("%s\t%s\t%s\t%s"%("姓名","地址","电话","工作"))
						print("%s\t%s\t%s\t%s"%(i["name"],i["addr"],i["phone"],i["job"]))
						flag=1
				if flag==0:
					print("查无此人...")
			elif query_choice==5:
				break
			else:
				print("数据有误，别瞎搞...")
	elif choice_num==3:
		
		update_line_num = int(input("请输入想要修改的行号"))
		
		for i in infor_list:
			if update_line_num == infor_list.index(i)+1:
				update_new_name=input("请输入你想要的新名字，不修改请按直接按回车：")
				update_new_addr=input("请输入你想要的新地址，不修改请按直接按回车：")
				update_new_phone=input("请输入你想要的新电话，不修改请按直接按回车：")
				update_new_job=input("请输入你想要的新工作，不修改请按直接按回车：")
				if update_new_name!="":
					i["name"]=update_new_name
				if update_new_addr!="":
					i["addr"]=update_new_addr
				if update_new_phone!="":
					i["phone"]=update_new_phone
				if update_new_job!="":
					i["job"]=update_new_job
		
	elif choice_num==4:
		delete_line_num = int(input("请输入想要删除的行号"))
		for i in infor_list:
			if delete_line_num == infor_list.index(i)+1:
				infor_list.remove(i)
	elif choice_num==5:
		print("%s\t%s\t%s\t%s\t%s"%("行号","姓名","地址","电话","工作"))
		#定义一个计数器count，用以计算名片的数量，并在界面中显示
		count=1
		for i in infor_list:
			print("%d\t%s\t%s\t%s\t%s"%(count,i["name"],i["addr"],i["phone"],i["job"]))
			count+=1
	elif choice_num==6:
	
		exit_choice = input("确定退出？y/n:")
		if exit_choice=="yes":
			print("感谢使用，再见")
			break
		elif exit_choice=="no":
			continue
		else:
			print("输入的数据有误，请重新输入")
			continue
	else:
		print("输入的数字有误，请重新输入")