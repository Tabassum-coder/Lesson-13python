print("Floyd's Triangle")
rows=int(input("Enter no of rows"))
num=1
for i in range(num,rows+1):
    for j in range(1,i+1):
        print(num,end="")
        num=num+1
    print()