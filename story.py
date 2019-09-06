from collections import Counter
outfile=open("story.txt",'r')
x=outfile.read()
c=x.split(' ')
counted=Counter(c)
print(counted)
