# 25/11/2022 String
# String Data type
# When a string contains numbers, it is still is string

for i in "banana":
    print(i)

print("==============o0o===============")
# Reading and converting
name = "An"
age = "5"


totalAge = int(age) - 5
print("Ten cua toi la:",name,"\n Tuoi cua toi la:",totalAge)
print("==============o0o===============")
# Looking inside Strings
vegatables = "Tao Tau"
firstStrings = vegatables[0]
print("Rau ban an co ma dau tien la:",firstStrings)
print("==============o0o===============")
# Looping through Strings
vagaTables = "Ngu Qua"
index = 0 
while index < len(vagaTables):
  letter = vagaTables[index]
  print(index,letter)
  index = index +1
print("==============o0o===============")  
# Looping and counting
work = "banana"
indeX = 0 
for valueFor in work:
    if valueFor == 'a':
        indeX = indeX + 1
print(indeX)

# String concatenation

a = "Hello"
b = a + "world"
print(b)
c = "Hello"
d = c + " " + "World"
print(d)