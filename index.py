print("new patient")
name="john smith"
age=20
print(name,age) 
sentence="i love python"
print("python" in sentence)
#for exponential fuctions like 2^10 we use **
print(2**3)
txt="my name is {},i like {}"
print(txt.format("naveen","apple"))
thislist=["apple","banana","greap","eat"]
for x in thislist:
    print(x)
thislist.sort()
print(thislist)
x=(1,2,3,4)
print(x)
y=list(x)
y[1]=5
x=tuple(y)
print(x)
#dictionaries
thisdicti={"name":"ravi","age":14,"address":"nuzvid","gender":"male"}
print(thisdicti["age"])
y=thisdicti.get("address")
print(y)
print(thisdicti.items())
print(thisdicti.keys())
print(thisdicti.values())
thisdicti["age"]=18
print(thisdicti)
thisdicti.update({"address":"vijayavada"})
print(thisdicti)
thisdicti["color"]="brown"
print(thisdicti)
thisdicti.pop("color")
print(thisdicti)
thisdicti.popitem()
print(thisdicti)
del thisdicti["name"]
print(thisdicti)
thisdicti.clear()
print(thisdicti)
thisdicti = {"name": "ravi", "age": 14, "address": "nuzvid", "gender": "male"}
for x in thisdicti.items():
    print(x)
#if else condition short form
a=55
b=58
c=1
print("lesser") if a<b else print("greater")
print("lesser") if a < b else print("equal") if a==b else print("greater")
if a>b and a>c:
    print("a is the largest")
elif a==b or (c<a and c<b):
    print("a and b is equal")
else:
    print("a is not largest")
#while loop
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)
#while loop with else condition
i = 0
while i < 9:
  i += 1
  print(i)
else:
    print("i is no longer lessthan 9")
#functions


def mufunn(*name):
      print("my name is "+name[0]+" and i am 21")


mufunn("naveen", "21")
#special kind of if statement
x = 'hello'
if not type(x) is int:
    print("only integers are allowed")
