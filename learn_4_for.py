# Print lagre value in for
n = -1
for intervalNew in [12, 13, 14, 20, 90, 10, 15, 20]:
    if intervalNew > n:
        n = intervalNew
    print("Value :", n, intervalNew)
print("Large Value :", n)
print("================================================")
# Test 2 loop
zork = 0
print("Before", zork)
for ithink in [14, 22, 25, 76, 92, 12, 100,29, 34]:
    zork = zork + 1
    print(zork, ithink)
print("After", zork)
print("================================================")
# Summing in a loop
zork_1 = 0
print("Before", zork_1)
for ithink_1 in [12, 13, 14, 20, 90, 10, 15, 20ll]:
    zork_1 = zork_1 + ithink_1
    print(zork_1, ithink_1)
print("after", zork_1)
print("================================================")
# Finding the Average Value in a loop
averageloop = 0
total = 0
for ithink_2 in [12, 13, 14, 20, 90, 10, 15]:
    averageloop = averageloop + ithink_2
    total = total + 1
    print(averageloop, ithink_2, total)
print("Total:", averageloop/total)
print("After all:", averageloop,total, averageloop/total)
print("================================================")    
# Filtering in a loop
print("Start")
for filt in [54,12,34, 20, 90, 10, 15]:
    if filt > 30:
        print("Value large 30 : ", filt)
print("end")
print("================================================")
#Searching Using a Boolean  Variable
foundFile = False
for boolean_valuestring in [54,12,34, 20, 90, 10, 15]:
    if boolean_valuestring == 90:
        foundFile = True
    print("Value true", boolean_valuestring)
print("After:", foundFile)
print("================================================")
# Find the smallest value
smallestValue = -1
print("Before:", smallestValue)
for smalletV in [54,12,34, 20, 90, 10, 15]:
    if smalletV < smallestValue:
        smallestValue == smalletV
    print("Value:",smallestValue, smalletV)
print("After:", smallestValue)
print("================================================")
# Finding the smallest value
smallestValue1 = None
for smalletValue11 in [54,12,34, 20, 90, 10, 15]:
    if smallestValue1 is None:
        smallestValue1 = smalletValue11
    elif smalletValue11 < smallestValue1 :
        smallestValue1 = smalletValue11
    print("Value:",smallestValue1, smalletValue11)
print("Final:", smallestValue1)
