from lib2to3.pgen2.token import EQUAL
import honeyHouse as hH
import extraTest as eT

test1 = hH.Honey()
test2 = eT.Extra()

# for a in range(1, 100):
#     # print("test1 :", test1.makeHoney(a))
#     # print("test2 :", test2.makeExtra(a))
#     if test1.makeHoney(a) != test2.makeExtra(a):
#         print(a)
#         break

#     else:
#         continue

# print("test1 Done")

# for a in range(100, 500000):
#     # print("test1 :", test1.makeHoney(a))
#     # print("test2 :", test2.makeExtra(a))
#     if test1.makeHoney(a) != test2.makeExtra(a):
#         print(a)
#         break

#     else:
#         continue

# print("test2 Done")

# for a in range(500000, 1000000):
#     # print("test1 :", test1.makeHoney(a))
#     # print("test2 :", test2.makeExtra(a))
#     if test1.makeHoney(a) != test2.makeExtra(a):
#         print(a)
#         break

#     else:
#         continue

# print("test2+ Done")

for a in range(1000000, 10000000):
    # print("test1 :", test1.makeHoney(a))
    # print("test2 :", test2.makeExtra(a))
    if test1.makeHoney(a) != test2.makeExtra(a):
        print(a)
        break

    else:
        continue

print("test3 Done")

# for a in range(10000000, 100000000):
#     # print("test1 :", test1.makeHoney(a))
#     # print("test2 :", test2.makeExtra(a))
#     if test1.makeHoney(a) != test2.makeExtra(a):
#         print(a)
#         break

#     else:
#         continue

print("test4 Done")

# for a in range(100000000, 1000000001):
#     # print("test1 :", test1.makeHoney(a))
#     # print("test2 :", test2.makeExtra(a))
#     if test1.makeHoney(a) != test2.makeExtra(a):
#         print(a)
#         break

#     else:
#         continue

print("all test Done")