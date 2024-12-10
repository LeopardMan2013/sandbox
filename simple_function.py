def merge(output_l, input_l1, input_l2):
    for i in range(len(input_l1)):
        input_l1[i] = str(input_l1[i])
    output_l = input_l1 + input_l2
    output_l.sort()
    return output_l

l1 = [9,8,7,6,5]
l2 = ['Hamish','Jack']

o_list = []

o_list = merge(o_list,l1,l2)
print(o_list)
