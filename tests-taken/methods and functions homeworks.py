#Problem 1
def vol(rad):
    import math
    units = input("Enter the unit of the radius measurement: ")
    volume = 4/3 * math.pi * rad**3
    
    output = f"The volume of the sphere is {volume} {units}"
    return output
print(vol(5))

#Homework 2
def ran_check(num,low,high):
    if num in range(low,high+1):
        return f'{num} is within the range {low} to {high}'
    else:
        return f'{num} is not within the range {low} to {high}'
    
#Homework3
def up_low(s):
    up = []
    down = []
    
    for character in s:
        if character.islower():
            up.append(character)
        if character.isupper():
            down.append(character)
    print('The number of upper case character is: ' + str(len(up)))
    print('The number of upper case character is: ' + str(len(down)))
    return f'\nYour input is: {s}'

#Homework4
def unique_list(lst):
    
        return list(set(lst))


#Homework5
def multiply(numbers):
    
    product = 1
    
    for num in numbers:
        product *= num
        
    return product

mylist2 = [1,2,3,-4]
result = multiply(mylist2)

#Homework6
def palindrome(s):
    
    print(f'Here is your input: {s[::]}')
    
    if s[::-1] == s[::]:
        return '\nIt is a palindrome!!'
    else:
        print(f'\nHere is the reverse: {s[::-1]}')
        return '\nIt is not a palindrome!!'
