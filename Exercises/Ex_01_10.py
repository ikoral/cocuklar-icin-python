################## Ex01 -Ex10 #######################

# # Ex_01
# print("ilhan koral")
# print("The Amazing Street 01")
# print("FantasticCity", 3511)
# print("Belgium")

# # Ex_02
# your_name = input("Enter your name")
# print("Hello", your_name)


# Ex_03 / Ex_04
length = float(input("Please enter a length in meters: "))
width = float(input("Please enter a width in meters: "))
area = width*length
area_donum = area / 1000
area = ("%.3f" % area)  # here we are limiting decimal points to three numbers
print("The area of room is ", area, "square meters")
print("The area of room is ", area_donum, "donum")
