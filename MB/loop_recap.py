# fruits = ["apple", "banana" , "cherry"]
# for fruit in fruits:
#     print(fruit)



# for i in range(2, 7):
#     print(i)



# for i in range(1, 10, 2):
#     print(i)



# fruits = ["apple", "banana" , "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f'Index: {index}, Fruit: {fruit}')




# count = 1
# while(count <= 5):
#     print(count)
#     count += 1




# i = 0
# while True:
#     print(i)
#     i += 1
#     if i >= 10:
#         break






# i = 0
# while i < 10:
#     i += 1
#     if (i % 2 == 0) :
#         continue
#     print(i)



# for i in range(3):
#     for j in range(2):
#         print(f'i: {i}, j: {j}')




# loop lease clause :

# for i in range(5):
#     print(i)
# else :
#     print("loop finished!")

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else :
#     print('while loop finished!')





# squares = [x ** 2 for x in range(10)] 
# print(squares)


# even = [x for x in range(20) if x % 2 == 0]
# print(even)



squares_generator = (x ** 2 for  x in range(10))
for square in squares_generator:
    print(square)

