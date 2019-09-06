outfile=open("output.txt",'w')
names=["jake","joy","parker","felix","james","ada","benita","scott","jerry","tom"]
password=["good","red","g","a","h","g","l","o","p","r"]
for item in names:
    outfile.write(item+'\n')
for item in password:
    outfile.write(item+'\n')
d=input("Hello choose between register or login :")
chard=input()
print(chard)
chard=""
while True:
    chard=input("> ").lower()
    def register():
        if chard=="register":
            print("enter username :")
            print("enter password :")
    def login():
        if chard=="login":
            usersname=input(
" hello enter  your username:")
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
    