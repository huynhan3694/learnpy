# count = dict()
# line = input("Nhap mot doan van ban:")
# works = line.split()
# print("Value Works:", works)


# Key: value
Line = {"Xuan":1 , "Ha": 4, "Thu": 9, "Dong": 12}
print(list(Line))
print(Line.keys())
print(Line.values())
print(Line.items())
for keyOne, ValueOne in Line.items():
    print(keyOne, ":", ValueOne)