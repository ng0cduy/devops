def append_to_list(val, my_list=[]):
    my_list.append(val)
    return my_list

# print(append_to_list(1))
# print(append_to_list(2))

def square_numbers_gen(nums):
    for i in nums:
        yield i * i # Trả về từng số một


# Create a generator for 10 million numbers
print(square_numbers_gen(range(10000000)))
