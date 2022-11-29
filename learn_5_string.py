# 25/11/2022 String
# String Data type
# When a string contains numbers, it is still is string

for i in "banana":
    print(i)

print("==============o0o===============")
# Reading and converting
name = input("Your name:")
age = input("Your age:")


totalAge = int(age) - 5
print("Ten cua toi la:",name,"\n Tuoi cua toi la:",totalAge)
print("==============o0o===============")
# Looking inside Strings
vegatables = input("Nhap Ten rau ban muon an:")
firstStrings = vegatables[0]
print("Rau ban an co ma dau tien la:",firstStrings)