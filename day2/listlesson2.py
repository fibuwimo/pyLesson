import pprint
data=[
    [1,2,3],
    [4,5,6],
]
print(data[1][2]) 

data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
pprint.pprint(data)

data=[1,2,3]+[4,5]
print(data)

data=[1,2,3]*3
print(data)

data=[None]*10
for i in range(10):
    data[i]=[0]*10
pprint.pprint(data)

data2=[[0]*10]*10
pprint.pprint(data2)

data2[1][1]=5
pprint.pprint(data2)

data3=[[0]*10 for i in range(10)]
pprint.pprint(data3)

data4=[[i*10+j for j in range(1,11)]for i in range(0,10)]
pprint.pprint(data4)

data5=[i*10+j for j in range(1,11) for i in range(0,10)]
pprint.pprint(data5)

data6=[2 if(i==0) else 2+3**i for i in range(0,5)]
pprint.pprint(data6)
