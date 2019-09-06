#open file for input
outfile=open("output.txt",'w')
#dummy data
names=["jake","joy","parker","felix","james","ada","benita","scott","jerry","tom"]
password=["good","red","g","a","h","g","l","o","p","r"]
#send data to file
for item in names:
    outfile.write(item+'\n')
for item in password:
    outfile.write(item+'\n')

#get input from user ? username
usersname=input(" hello enter  your username:")
#open file to check for username
outfile=open("output.txt",'r')
x=outfile.read()
c=[]
c=x.split('\n')
code=input("your password:")
if code in c:
    if c[int(c.index(usersname))+10]==code:
        print("hello "+usersname)
    else:
            print("invalid parameter")