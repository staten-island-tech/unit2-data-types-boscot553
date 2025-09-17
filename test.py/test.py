# Auto detect text files and perform LF normalization
# x = 3
# y = float(3)
# print(x,y)

# values = [1,2.23,5,7,2,30,15]
# print(values[0])
# print(values[6])
# for i in values:
#     print(i)

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)


# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')



# x = input("Gimme a number ")
# x = int(x)
# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

# bill = input("How much was your bill? ")
# tip = input("Select a tip amount: 0, 15, 20, or 25")
# bill = int(bill)
# tip = int(tip)
# if tip == 0:
#     print(bill)
# elif tip == 15:
#     bill = bill * 1.15
#     print(bill)
    
# elif tip == 20:
#     bill = bill * 1.20
#     print(bill)
# elif tip == 25:
#     bill = bill * 1.25
# else:
#     print("Pick a valid tip amount")

x = input("Gimme a number ")
x = int(x)
y = 1
for i in range(x):
    if x % y == 0:
        print(y)
        y += 1
    else:
        y += 1

  