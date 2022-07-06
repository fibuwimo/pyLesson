import pprint

pprint.pprint([[i*10+j for j in range(9,0,-1)]for i in range(9,-1,-1)])

row=col=5
matrix=[[1 if i==j or 4-i==j else 0 for j in range(col)] for i in range(row)]
pprint.pprint(matrix)

pprint.pprint([[i+j for j in range(0,-100,-10)] for i in range(0,100,10)])

row=col=5
matrix2=[[1 if i==j else 2 if i>j else 0 for j in range(col)] for i in range(row)]
pprint.pprint(matrix2)

row=col=4
matrix3=[[i if i==j else 0 for j in range(col)] for i in range(row)]
pprint.pprint(matrix3)

print([[i*10+j for j in range(0,9)]for i in range(6,10)])

pprint.pprint([[i*j for j in range(1,10)]for i in range(1,10)])

pprint.pprint([[i*j for j in range(1,10)]for i in range(3,10,2)])

pprint.pprint([[i+j for j in range(0,10,2)] for i in range(2,0,-1)])

pprint.pprint([['_' if ((i+1)*j)%2==0 else '*' for j in range(10)]for i in range(10)])

pprint.pprint([[i**2+j for j in range(0,10)]for i in range(0,10)])
