import pickle

f2=open("files/MemberRoughCopy.dat",'rb')
mem_rec=pickle.load(f2)

for i in mem_rec:
   print(i)
   
f2.close()


   
