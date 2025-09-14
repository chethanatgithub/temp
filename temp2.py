def generate_odd_numbers_between_range(start,end):
    
 
    odd_list=[]
    for num in range(start,end+1):
        if num%2!=0:
            odd_list.append(num)
    return odd_list
print(generate_odd_numbers_between_range(1,100))


