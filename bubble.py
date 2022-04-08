def displayList():
    output = "["
    for num in list:
        output += str(num) + ", "
    output += "]"
    print (output)

# Swap indexes 1 and 2
def swap(i1, i2):
    uh = list[i2]
    list[i2] = list[i1]
    list[i1] = uh

list = [7, 13, 6, 4, 27, -58, 11, 29, 12, 21, 11, 10, 8]
displayList()
swap(1, 2)
displayList()