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
#     print(d.setdefault(a, "неизвестно"))
#     print(d)

