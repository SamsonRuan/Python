#guess game
import random
print("hi,wthat is your name?")
name=input()
print("hi,%s,let us play a game,now ,guess a number between 1 and 20"%name)
try:
	guess_num=int(input())
except Exception:
	print("sorry,it is not a num...")
num_count=0
num=random.randint(1,20)
while num_count<5:
	num_count=num_count+1
	try:
		if num>guess_num:
			print("your guess is too low,please guess a new one")
			guess_num=int(input())
		elif num<guess_num:
			print("your guess is too high,please guess a new one")
			guess_num=int(input())
		else:
			print("congratulations,%s!your guess is right!"%name)
			break
	except Exception:
		print("dont have this variable")
if num_count<=6:
	print("you pass the game in %d times!"%num_count)
else:
	print("sry,you fai the game...")
		
	
	
