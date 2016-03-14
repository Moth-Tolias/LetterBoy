GOTNUMB = 0

while GOTNUMB <= 0:
    GOTNUMB = ord(input("How corrupted do you want the text to be?"))
    if GOTNUMB <=0:
        print("Must be greater than zero.")
    else:
        break
    
TEXT= input("Put the text to be corrupted here:")

print("")
for char in TEXT:
    for i in GOTNUMB:
        char += "r"
        print(char,end="")
print("")
print("")

print("Corruption complete!")
