#定义一个列表，这个列表存储着字典形式的所有名片
card_list = []
#定义一个函数，打印主界面菜单
def print_meun():

	print("="*50)
	print("名片关系系统V1.1")
	print("1.添加一张新名片")
	print("2.查询一张新名片")
	print("3.修改一张新名片")
	print("4.删除一张新名片")
	print("5.显示当前所有名片")
	print("6.退出系统")
	print("="*50)
	
#定义一个函数，实现名片的添加功能
def card_add():
 
	#定义一个空字典，以键值对的方式存储用户键入的信息
	card_dict = {}
	
	card_name = input("请输入姓名:")
	card_addr = input("请输入地址:")
	card_age = input("请输入年龄:")
	card_job = input("请输入工作:")
	
	#将用户键入的信息储存到空字典中
	card_dict["dict_name"] = card_name
	card_dict["dict_addr"] = card_addr
	card_dict["dict_age"] = card_age
	card_dict["dict_job"] = card_job
	
	#将字典作为元素加入到列表中
	card_list.append(card_dict)
	
	#作为测试，打印这个列表
	print(card_list)
	
#定义一个函数，实现名片的显示功能
def card_showall():

	line_num = 1

	print("%s\t%s\t%s\t%s\t%s"%("行号","姓名","地址","年龄","工作"))
	
	for temp in card_list:
		print("%d\t%s\t%s\t%s\t%s"%(line_num,temp["dict_name"],temp["dict_addr"],
		temp["dict_age"],temp["dict_job"]))
		line_num+=1
	
#定义一个函数，实现名片的删除功能
def card_del():

	card_index = int(input("请输入想要删除的名片的下标："))
	
	for temp in card_list:
		if card_list.index(temp) == card_index-1:
			del card_list[card_index-1]
	else:
		print("输入有误。。。")
#定义一个函数，实现名片的修改功能
def card_update():
	line_num = int(input("请输入想要修改的行号"))
	for temp in card_list:
		if card_list.index(temp) == line_num-1:
			update_before = input("请输入想要修改的内容：")
			if update_before == "姓名":
				update_after = input("请输入修改后的名字：")
				temp["dict_name"] = update_after
			elif update_before == "地址":
				update_after = input("请输入修改后的地址：")
				temp["dict_addr"] = update_after
			elif update_before == "年龄":
				update_after = input("请输入修改后的年龄：")
				temp["dict_age"] = update_after
			elif update_before == "工作":
				update_after = input("请输入修改后的工作：")
				temp["dict_job"] = update_after
			else:
				print("你的输入有误。。。")
	else:
		print("行号不存在。。。")
	
#定义一个函数，实现名片的修改功能
def card_query():
	
	query_content = input("请输入想要查询的内容：")
	for temp in card_list:
		if temp["dict_name"] == query_content or temp["dict_addr"] == query_content or temp["dict_age"] == query_content or temp["dict_job"] == query_content:
			print("%s\t%s\t%s\t%s"%(temp["dict_name"],temp["dict_addr"],
			temp["dict_age"],temp["dict_job"]))
	
	
	
#定义一个主函数，在这个函数中实现对程序的控制
def main():
	
	while True:
	
		print_meun()
		meun_num = int(input("请输入想要的执行的功能："))
		
		if meun_num == 1:
			#在这里执行添加新名片的函数card_add
			card_add()
		elif meun_num == 2:
		    #在这里执行查询新名片的函数card_query
			card_query()
		elif meun_num == 3:
			#在这里执行修改新名片的函数card_update
			card_update()
		elif meun_num == 4:
			#在这里执行删除新名片的函数card_del
			card_del()
		elif meun_num == 5:
			#在这里执行显示所有名片的函数card_showall
			card_showall()
		elif meun_num == 6:
			#在这里退出并且结束程序
			print("谢谢使用")
			break
		else:
			print("输入有误，请重新输入")
		
main()			
			
			
			
			
			
			
			
			
			
			