slicingString = "Become to Senior Python"

print(slicingString[:4])
print(slicingString[-4:])
print(slicingString[4:-4])
print(slicingString[2:5])

# String Library
inValue = "Hello Python"
lowercaseString = inValue.lower()
print(lowercaseString)

# Value dir
stuff = "Hello world"
type(stuff)
dir(stuff)

# Using find("value"), upper(), lower(), replace("Value will replace", "Value replace")
valueInput = "Hello Python, My Name is Python"
valueUpper = valueInput.upper()
valueLower = valueInput.lower()
valueFind = valueInput.find("Py")
valueReplace = valueInput.replace("Python", "Golang")
print(valueUpper,"\n" ,valueLower,"\n", valueFind,"\n", valueReplace)

# Stripping Whitespace
# Sometime we want to take a string and remove whitespace at the beginning and/or end
#lstrip and rstrip : remove whitespace lef and right
#strip: remove whitespace both beginning and ending whitespace

createWhiteSpace = ' Hello Python '
lWhiteSpace = createWhiteSpace.lstrip()
rWhiteSpace = createWhiteSpace.rstrip()
allWhiteSpace = createWhiteSpace.strip()

print("left whitespace:",lWhiteSpace,"right whitespace:",rWhiteSpace,"all white space:",allWhiteSpace)

# Prefixes
line = "Please have a nice day"
valueTrue = line.startswith("Please")
valueFalse = line.startswith("p")
print(valueTrue, valueFalse )
# Parsing and Extracting

data = "Hello include world@aboutParsing and Extracting"
atpos = data.find("@")
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1: sppos]
print(host)
