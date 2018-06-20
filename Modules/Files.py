try:
    text = "This is what I meant"
    file1 = open("wanyama.pdf", "w")
    file1.write(text)
except IOError:
    print("Can't find file or read data")
else:
    print("Content written successfully")
    file1.close()

try:
    file1 = open("mimi", "w")
    try:
        file1.write("This is the second Meaning")
    finally:
        print("Going to close .;p")
        file1.close()
except IOError:
    print("Error: Can't find the file or read data")


# Try Except in functions
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n", Argument)


temp_convert("xyz")