# Looking inside lists
listNumber = [1,2,4,6,8,10]
listString = ["Hello", "World", "Chao","Chao Xin"]
listNumStr = [1,2,4,6,8,10,"Hello", "World", "Chao","Chao"]
print(listNumber)
print(listString)
print(listNumStr)

for listNumbers in listNumber:
    print(listNumbers)
print("Ending")
# List and Mutable
lotto = [1,2,5,6,12,10]
lotto[3] = 99
print(lotto)
# How long is a List? (using len())
# using range()

# Working with lists
# Concatenating lists using +
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)