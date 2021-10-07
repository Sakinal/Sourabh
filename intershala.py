import json
n=input("Enter the number:")
flag=False
f=open("internshala.json")
data=json.load(f)
for i,k in data.items():
    if i==n:
        print(k)
        flag=True
if flag==False:
    print('Finding Not Found')
