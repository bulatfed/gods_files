#1.0

# a = [1, 2, 3, 4, 5, 6]
# chet = []
# gotovo = []

# for i in a:
#     if i % 2 == 0: 
#         chet.append(i)
# for i in chet:
#     gotovo.append(i*10)

# print(gotovo)
    

#1.1

# a = [1, 2, 3, 4, 5, 6]
# gotovo = []

# for i in a:
#     if i % 2 == 0:
#         gotovo.append(i*10)
        
# print(gotovo)

#2 

# a = [1, 2, 3]
# gotovo = a.copy()
# gotovo.reverse()
# print(gotovo)

#3

# a = [5, 1, 9, 9, 3]
# #a = [7, 7, 7]
# unic = []

# for i in a:
#     if i not in unic:
#         unic.append(i)
        
# if len(unic) < 2:
#     print('none')
# else:
#     unic.sort(reverse=True)
#     print(unic[1])
 

#4

# a = [1, 2, 1, 3, 2, 4]
# unic = []

# for i in a:
#     if i not in unic:
#         unic.append(i)
# print(unic) 

#5


# a = [1,2,3,4]
# b = [3,4,5,6,]
# povtor = []
# for i in range(len(a)):
#     if a[i] in b:
#         if a[i] not in povtor:
#             povtor.append(a[i])
# print(povtor)
  