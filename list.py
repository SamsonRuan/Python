def main():
    list=[]
    while True:
        print("input your words,enter 'N' to quit")
        word = input()
        if word!="N":
            list.append(word)
        else:
            break
    display(list)
def display(list):
    for i in list:
        if list.index(i)==len(list)-1:
            print("and %s"%i)
        else:
            print("%s ,"%i,end='')
main()

