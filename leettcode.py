# def two_sum(nums, target):
#     result = list(set([(x,y) for x in nums for y in nums if x+y == target]))
#     return result

# print(two_sum([2,7,11,15], 9))



# x, y, z = 1,1,2
# def func():
#     list_ =[x,y,z]
#     res = list(set([(x,y,z) for x in list_ for y in list_ for z in list_ if x+y+z != 4]))
#     return res
# print (func())


# def p(num):
#     num = str(num)
#     num1 = num[::-1]
#     if num == num1:
#         return True
#     else:
#         return False

# print(p(12))

def say_hello(name, city, state):
    name = ' '.join(name)
    return f'Hello, {name}! Wecome to {city}, {state}!'

print(say_hello(['john', 'sam'], 'new york', 'arizona'))