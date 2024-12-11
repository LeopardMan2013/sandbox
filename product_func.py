
def prod(lst):
    calc = 1
    for i in lst:
        calc += i
    return calc

l = [1,2,3,4,5,6,7,8,9,10]
result = prod(l)
print(result)
