# # Условные операторы 
# # a = int(input("Введите число: "))
# # знаки в условных операторах 
# '''
# >,<,== - интуитивно понятно
# <= , >= - меньше или равно больше или равно 
# and --- if a == 0 and b == 0 and c == 0 ... 
# or --- if a == 0 or b == 0 or c == 0 ....
# not -  if a not in list (list = [1,2,3,4,5,6 или че угодно ])

# if ,  elif, else 
# '''
# # list_shit = [1,2,3,4,5,6,7]
# # if a not in list_shit:
# #     print("gsf")

# '''if a == 0:
#     a +=1
#     print(1)
# elif a == 1:
#     print("work")
# else:
#     print("shit")'''
    


# # a = int(input())

# # if a == 12 or a == 1 or a == 2:
# #     print("Зима")
    
# # elif a == 3 or a == 4 or a == 5:
# #     print("Весна")
    
# # elif a == 6 or a == 7 or a == 8:
# #     print("Лето")

# # elif a == 9 or a == 10 or a == 11:
# #     print("Осень")
    
# # else:
# #     print("Ошбика")

# # sum = int(input())
# # card =input()

# # if card == "нет":
# #     print(sum)
# # else:
# #     if sum >= 5000:
# #         sum = sum / 100 * 90
# #         print(sum)

# #     elif sum >= 1000:
# #         sum = sum / 100 * 95
# #         print(sum)
    
# #     else:
# #         print(sum)

# # num = int(input())

# # if num > 0:
# #     print("Положительное")
# # elif num < 0:
# #     print("Отрицательное")
# # else:
# #     print("Ноль")

# # if num %2 == 0:
# #     print("Чётное")
# # else:
# #     print("Нечётное") 
# # sum = int(input())
# # rust = int(input())

# # delivery = 200

# # if sum > 5000:
# #     print(sum)

# # elif sum >= 3000:
# #     if rust > 30:
# #         delivery = delivery + 100 / 100 * 50
# #         sum = sum + delivery
# #         print(sum)
        
# #     else:
# #         if rust < 30:
# #             delivery = delivery / 100 * 50
# #             sum = sum + delivery
# #             print(sum)
# # elif sum < 3000:
# #     if rust > 30: 
# #         delivery = delivery + 100
# #         sum = sum + delivery
# #         print(sum)
# #     else:
# #         if rust < 30:
# #             sum = sum + delivery
# #             print(sum)  





# a = [1,2,3,]
# b =  3 in a
# if b ==True:
#     print("yes")


# a = [2,9,5,3,3,8,7,5,3,21,9,6]
# print(a[0],'-',a[4])
# print(a[1:5])
# b = ['pop', 'tup', 'cup', 'dup', 'snupm', 'plup', 'clup', 'nup']
# print(b[0],'-',b[5])
# print(b[0:4])
# c = [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,8.7,2.5,7.8756,5.64,13.45,534.45,]
# print(c[0:4])
# print(c[-2])
# d = [1, 'trup', 4.3, 5, 5, 'osrup', 93.32, 5, 2, 'off', 44.22, 5, 9, 'klass', 89.4, 5.84, 'zlup', 54.3, 999, 1000]
# print(d[18:])
# print(d[19],'-',d[1])
# l = [False,True,True, False, False,True,True,True,False,False,True]
# print(l[:2],'-',l[9:])
# print(l[-2],'-',l[5])
# print(a[0],a[4],b[0],'-',b[5],c[-2],d[19],'-',d[1],l[-2],'-',l[5], '/n')
# a = a[0], a[1]
# b = b[6], b[7]
# list_per = [a+b] * 3
# print(4 in list_per)

# a = [2,4]
# a.append(6)
# print(a)

# a = [4,5]
# i = 1
# a.insert(i, 6)
# print(a)

# a = [9,3,2,5]
# a.remove(3)
# print(a)


# a = [5,3,2,5]
# i = 2
# a.pop(i)
# print(a) ????

# a = [3,5,6,2,3]
# i = 2
# a.index(i)
# print()???


# a = [4,5,1,7,9,56,3,2]
# a.sort()
# print(a)


# a = [1, 2, 3, 4, 5, 7, 9, 56]
# a.reverse()
# print(a)


# a = [1, 2, 3, 4, 5, 7, 9, 56]
# b = len(a)
# print(b)



#1
# a = ['sus', 'kus', 'mus', 'dus', 'nnd']
# print(a[0],a[-1])
#2
# a = [10, 20, 30, 40, 50]
# print(a[1:4])
#3
# a = []
# a.append(5)
# a.append(10)
# a.append(15)
# a.remove(10)
# print(a)
#4
# a = ['a', 'b', 'c']
# a.insert(1, 'x')
# print(a)
#5
# a = [1, 2, 3, 4, 5, 6, 7]
# long_list = len(a)
# print(long_list)
# #6
# a = [1, 2, 3, 2, 4, 2]
# print(a.index(2))
# #7
# a = [5, 1, 8, 3]
# a.sort()
# a.reverse()
# print(a)
#8
# a = [100, 200, 300, 400]
# st = a[0], a[-1] = a[-1], a[0]
# print(a) *
#9
# a = "Привет-мир"
# b = list("Привет-мир")
# b[6] = " "
# print(b) *
# 10
# a = [0] * 9
# a[4] = 1
# print(a)
#11
# a = [2, 4, 6, 8]
# summ = 
#12
# a = [12, 5, 9, 21, 3]
# mak = a[0]
# for i in a:
#     if i > mak:
#         mak = i
# print(mak)*
#13
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for i in a:
#     if i % 2 == 1:
#         even_numbers.append(i)
# print(even_numbers)
#14
# a = [1, 2, 3]
# #b = a.reverse()
# b = a.copy()
# b.reverse()
# print(a+b)
#15
# a = ['я', 'не учу', 'питон', 'я', 'пинаю' 'хуй']
# allah = ' '.join(a)
# print(allah)



# apples = [0,1,2,3,4,5,6,7,8,9]
# # print(apples[0])
# # print(apples[1])
# # print(apples[2])
# # print(apples[3])
# # print(apples[4])

# for apple in apples:
#     print(apple)

# count = 0
# while count < 5:
#     print(count)
#     count = count+1


# kk = [1,2,3,4]
# ss = []

# for i in kk:
#     ss.append(i*10)

# print(ss)

# a = [1,2,3,4]

# for i in range(len(a)):
#     a[i] = a[i] * 2
# print(a)



#1
# a = ['кот', 'пес', 'хомяк']

# for i in a: 
#     print(i)
#2
# a = [5,10,15,20]
# b = 0
# for i in a:
#     b = b + i
# print(b)
 #3
# a = [1,2,3,4,5]
# b = []
# for i in a:
#     b.append(i*3)
# print(b)
#4
# a = ['a', 'b', 'c', 'd']

# for i, a in  enumerate(['a', 'b', 'c', 'd']):
#     print(i, a)
#5
# a = [2,7,4,9,1]
# min = a[0]
# for i in a:
#     if i < min:
#          min = i
# print(min)
#6
# a = [3, 8, 15, 22, 7, 10]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
# print(b)
#7
# a = ['аликоптор', 'банан', 'арбуз', 'виноград']
# b = []
# for i in a:
#     if i[0] == 'а':
#         b.append(i)
# print(b)
#8
# a = [10, -5, 8, -2, 0, 6]

# for i in range(len(a)):
#     if a[i] < 0:
#         a[i] = 0
# print(a)
#9 
# a = ['маша', 'петя', 'маша', 'коля', 'маша']
# b = 0
# for i in a:
#     if i == 'маша':
#         b = b + 1
# print(b)
#10
a = [1, 2, 3, 4, 5]
chisla = ''

for i in a:
        chisla = chisla + str(i) + ' ' 
print (chisla) 



#7

# a = [5, -2, 0, -8, 3, -1, 7]

# i = len(a)-1
# while i >= 0:
#     if a[i] < 0:
#         a.pop(i)
#     i -= 1
        
# print(a)


#8

# a = [2, 4, 3, 5, 7, 1]
# target = 6
# gotovo = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i < j:
#             if a[i] + a[j] == target:
#                 gotovo.append((a[i], a[j]))
# print(gotovo)
        
        
#9


# cards = [1, 2, 3, 4, 5, 6]

# jussy = []
# pussy = []
# for i in range(len(cards)):
#     if i % 2 == 0:
#         jussy.append(i)
#     else:
#         pussy.append(i)
# print(jussy+pussy)    


#10



# nums = [1, 2, 3, 4, 5, 6]
# k = 2
# suck = []

# # for i in nums:
# suck = nums[k:] + nums[:k]
# print(suck)

#or

# nums = [1, 2, 3, 4, 5, 6]
# k = 2

# k %= len(nums)
# nums = nums[k:] + nums[:k]
# print(nums)




#11

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3

# k %= len(nums)
# nums = nums[k:] + nums[:k]
# print(nums)


#12

# nums = [2, 0, 3, 4, 0, 5]
# summ = 1

# for i in range(len(nums)):
#     if nums[i] == 0:
#         nums[i] = 1

#     summ = nums[i] * summ                           
# print(summ)


#13


# nums = [10, 20, 30, 40, 50]
# # Ожидаемый результат: [50, 10, 20, 30, 40]
# k = -1
# k %= len(nums)
# k = k + 1
# # k = len(nums)-1
# a = [nums[k - 1]]
# z = 0



# for i in nums:
#     if z == k - 1:
        
#         break
    
    
#     else:
        
#         a.append(i)
        
        
#     z = z + 1
    
    
    
# print(a)


#14



# nums = [5, 9, 2, 9, 1, 9, 8]
# # Ожидаемый результат: [1, 3, 5]  (максимум = 9, встречается на индексах 1, 3, 5)
# max_num = nums[0]
# for i in nums:
#     if i > max_num:
#         max_num = i
        
# index = []
# for i in range(len(nums)):
#     if nums[i] == max_num:
#         index.append(i)
        
# print(index)


# nums = [1, 2, 3, 4, 5]
# new_list = []


# a = len(nums)-1
# for i in nums:
#     new_list.append(nums[a])
#     a-=1
    
# print(new_list)    











# # while True:
# #     sum = int(input())
# #     rast = int(input())

# #     delivery = 200
        
        
# #     if sum>= 5000:
# #         print(sum)
# #     elif sum >= 3000:
# #         if rast > 30:
# #             print(sum+delivery/2+100)
# #         else:
# #             print(sum+delivery/2)  
# #     else:
# #         if rast > 30:
# #             print(sum+delivery+100)
# #         else:
# #             print(sum+delivery)     








# abon = input()
# month = int(input())

# # # "базовый" = 1500
# # # "Стандарт" = 2500
# # # "Премиум" = 4000

# if abon == "базовый":
#     price = 1500
#     if month >= 12:
#             print(price*month/100*80)
#     elif month >= 6:
#         print(price*month/100*90)
#     else:
#         print(price*month)
# if abon == "стандарт":
#     price = 2500
#     if month >= 12:
#         print(price*month/100*80)
#     elif month >= 6:
#         print(price*month/100*90)
#     else:
#         print(price*month)
# if abon == "премиум":
#     price = 4000
#     if month >= 12:
#         print(price*month/100*80)
#     elif month >= 6:
#         print(price*month/100*90)
#     else:
#         print(price*month)

# while True:
#     abon = input()
#     month = int(input())


#     if abon == "базовый":
#         price = 1500
#     elif abon == "стандарт":
#         price = 2500
#     else:
#         price = 4000
        
    # if month >= 12:
    #     print(price*month/100*80)
    # elif month >= 6:
    #     print(price*month/100*90)
    # else:
    #     print(price*month)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Типы данных в python 
int -  целое число
str - строка 
float - вещественное число 
bool - True/False - логические значения 
list - список ---> [1,2,3,4,5,6, [1,2]]
dict - словарь ---> {1:"лимон", 2:"апельсин", 3:"чайник"}

a = 1 
b = "l"
print(a+b) --  сложение разных типов данных 


операции с типами данных 
+
-
*
/
//
%


a = "1"
a = int(a)

# '''

# #(2, 6), (-4, 0), (0, 3), (5, 5), (-2, -1), (-5, 10)
# s = int(input())
# k = int(input())
# if (s >= 0 and k <= 5) or (s < -3):
#     print("ДА")
# else:
#     print("НЕТ")
    


    
    
    
    