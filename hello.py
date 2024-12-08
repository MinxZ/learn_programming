"""
simple hello world program
"""

# print("Hello, World twice!")

# a = 2
# if (a) == 2:
#     print("a is 2")

# total = 0
# for i in range(1, 10):
#     if i % 3 == 0:
#         continue
#     # total += i
#     print(i)

# a_list = list('123')
# b_list = list('246')
# for a, b in zip(a_list, b_list):
#     print(a, b)

# a, b = 1, 2

ab_dict = {'a': 1, 'b': 2}
# for key, value in ab_dict.items():
#     print(key, value)

print(list(ab_dict.keys()))
print(list(ab_dict.values()))

exit()
# some expression in python
print(2 + 3)
print(2 * 3)
print(2 ** 3)
print(2 / 3)
print(2 // 3)
print(2 % 3)

apple_price = 2
orange_price = 3

def count_apples_and_oranges(apples, oranges):
    """
    count total number of apples and oranges
    """
    return apples + oranges

print(count_apples_and_oranges(2, 3))


