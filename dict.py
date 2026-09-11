#1
# d = {"name": "AdskiiSatana", "age": 666, "city": "AdNahui"}
# print(d["name"])

#2
# d = {"a": 10, "b": 20}

# print(d.get("c", 0))

#3
# d = {"x": 1, "y": 2}
# print("y" in d)

#4
# d = {"Иван": 123, "Оля": 456, "Петя": 789}
# print(d["Оля"])

#5
# d = {"a": 1, "b": 2, "c": 3}

# if "a" not in d:
#     print("Проспись блядота")
# else:
#     print(d["a"])

#6
# d = {"car": "blinchester", "year": 1707}
# if "color" not in d:
#     print("нит")
# else:
#     print(d["color"])

# #7
# d1 = {"x": 10, "y": 20}
# d2 = {"y": 99, "z": 30}

# if "y" in d1 and "y" in d2:
#     print(True)
# else:
#     print(False)

#8
# d = {"name": "Аня", "age": 23}
# a = input()

# if a in d:
#     print(d[a])
# else:
#     print("Нет")

# #9
# d = {}
# print(bool(d))

#10
# d = {"a": 1, "b": 2}
# print(list(d))   

#11
# d = {"a": 1, "b": 2, "c": 3}
# print(list(d.values()))

#12
# d = {"x": 10, "y": 20}
# print(len(d))

#13
# d = {"name": "Аня", "age": 23}
# a = input()
# print(d.get(a, "нет"))

#14
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 99, "c": 3}
# sod = []

# for i in d1:
#     if i in d2:
        
#             sod.append(i)
# print(sod)
    

#15
# d = {"a": 1, "b": 2, "c": 3}

# if "b" in d and "z" in d:
#     print(True)
# else:
#     print(False)

#16
# d1 = {}
# d2 = {"a": 1}


# if d1 == {}:
#     print(True)
# else:
#     print(False)
# if d2 == {}:
#     print(True)
# else:
#     print(False)

#17
# d = {"x": 10, "y": 20, "z": 30}
# print(d["x"] + d["y"] + d["z"])

# 18
# d = {"a": 5, "b": 2, "c": 3}
# print(min(d.values()), max(d.values()))

# #19
# d = {"a": "h", "b": "e", "c": "l"}
# print("e" in d.values())

# 20
# d = {"name": "Иван"}
# a = input()
# if  a in d:
#     print(d[a])
# else:
#     print(d.4default(a, "неизвестно"))
#     print(d)

"----------------------------------------------------"

 #Доступ и проверка
#1
# d = {"a": 1, "b": 2, "c": 3}                  
# if "d" in d:
#     print(True)
# else:
#     print(False)

#2
# d = {"name": "Иван", "age": 25}
# a = input("Введите ключ " " " )

# if a not in d:
#     print("неизвестно")
# else:
#     print(d[a])

#3
# d = {"x": 1, "y": 2}
# print(list(d.values()))

#4
# d = {}

# if d == {}:
#     print(True)
# else:
#     print(False)

#5
# d = {"a": 1, "b": 2, "c": 3}
# print(min(d.values()), max(d.values()))

#Добавление и удаление

#6
# d = {"a": 1, "b": 2}
# d["c"] = 3
# print(d) 

#7
# d = {"name": "Иван", "age": 25}
# d["age"] = 26
# print(d)

#8
# d = {"a": 1, "b": 2, "c": 3}
# del d["b"]
# print(d)

#9
# d = {"name": "Иван"}
# a = input("Введите ключ" " ")
# if a in d:
#     print(d[a])
# else:
#     d.setdefault(a, "неизвестно")
#     print(d)

#10
# d = {"a": 10, "b": 20, "c": 30}
# for i, a in d.items():
#     print(f"{i}: {a}")

#11
# d = {"a": 1, "b": 2, "c": 3}
# print(sum(d.values()))

#12
# d = "helloplkjklkuihuikgolllllllllllllllllo"
# c = {}
# for i in range(len(d)):
#     if d[i] not in c:
#         c[d[i]] = 1
#     else:
#         c[d[i]]+=1
# print(c)

#13
# d = {"a": 5, "b": 12, "c": 7}
# print(max(d.values()))

# #14
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 99, "c": 3}
# # ожидаем {"a": 1, "b": 99, "c": 3}
# df = d1
# df.update(d2)
# print(df)

#15
# a = [1, 3, 2, 3, 1, 3, 2, 1]
# # ожидаем 3

# d1 = {}
# for i in a:
#     if i not in d1:
#         d1[i] = 1
#     else:
#         d1[i]+=1
        
# max = 0
# max_num = None

# for i in d1:
#     if d1[i]>max:
#         max = d1[i]
#         max_num = i
# print(max_num)


#----------------------------------------------------------------------



#1
# a = [1, 2, 2, 3, 3, 3]
# d = {}

# for i in a:
#     d[i] = d.get(i, 0) + 1
# print(d)     

#2
# a = "abracadabra"
# d = {}

# for i in a:
#     d[i] = d.get(i, 0) + 1
# print(d)

# #3
# a = ["кот", "пес", "кот", "кот", "пёс"]
# d = {}
# for i in a:
#     d[i] = d.get(i, 0) + 1
# print(d)

#4
# a = [1, 1, 1, 2, 2, 3]
# d = {}
# for i in a:
#     d[i] = d.get(i, 0) + 1

# for k, v in d.items():
#     if v > 1:
#         print(k)

#5
# d = "hello world"
# a = list(d)
# bukv = {}
# for i in a:
#     if i == " ":
#         continue    
#     bukv[i] = bukv.get(i, 0) + 1 


# print(bukv)

#6
# d = {"a": 3, "b": 7, "c": 5}
# print(max(d, key=d.get)) 

#7
# d = {"a": 3, "b": 7, "c": 5}
# print(min(d, key=d.get)) 

#8
# d = {"a": 3, "b": 7, "c": 5}

# for k, v in d.items():
#     if v > 4:
#         print(k)

#9
# d = {"a": 3, "b": 7, "c": 5}
# print(sum(d.values() ) / 2)

#10
# d = {"Иван": 4, "Оля": 5, "Петя": 3}
# for k, v in d.items():
#     if v >= 4:
#         print(k)

#11
# a = ["кот", "собака", "дом"]
# d = {}

# d = {s: len(s) for s in a}
# print(d)

#12
# a = [1, 2, 3, 4, 5]
# d = {}

# d = {s: s**2 for s in a}
# print(d)

#13
# a = ["apple", "banana", "cherry"]
# d = {s: s[0] for s in a}
# print(d)

#14
# a = [1, 2, 2, 3, 3, 3]
# s = {}
# for i in a:
#     s[i] = s.get(i, 0) + 1
# print(s)

#15
# a = ["a", "b", "a", "c", "b", "a"]
# chas = {}
# for i in a:
#     chas[i] = chas.get(i, 0) + 1
# for i, v in chas.items():
#     if v == 1:
#         print(i)
#     else:
#         continue
            
