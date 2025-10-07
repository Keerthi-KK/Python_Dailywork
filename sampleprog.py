print(5)
d=99
print(d)
print(type(d))
f='Digital'
print(f)
print(type(f))
h=True
print(h)
print(type(h))
s=7.889
print(s)
print(type(s))

#this is a tuple ,immutable,ordered,allow duplicates
d=(1,2,3,3)
print(d)
print(type(d))
print(d[2])
#d[2]=6
#doesnt work 

#this is a list ,mutable,ordered,allow duplicates
f2=[1,4,4,8,7]
print(f2)
print(type(f2))
print(f2[2])
f2[2]=3
print(f2)


#this is a set ,mutable,unordered,no duplicates
he= {1, 2, 3, 4, 2}
print(he)
print(type(he))
he.add(5)
print(he)

#dictionary
dic={ 'class':'PYTHON','student count':'30'}
print(dic)
print(type(dic))
