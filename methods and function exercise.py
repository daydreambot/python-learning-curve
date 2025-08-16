#Warmup 1
def less_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
    

#Warmup 2 Animal-Cracker
def animal_cracker(text):
    wordlist = text.split()
    
    first = wordlist[0]
    second = wordlist[1]
    
    return first[0] == second[0]


#WarmUp3
def makes_twenty(a,b):
    if a+b ==20:
        return True
    elif a ==20:
        return True
    elif b == 20:
        return  True
    else:
        return False
    
#LEVEL1
#Problem1
def old_mac(name):
    string1 = (name[:3])
    string2 = (name[3:])
    cap1 = string1.capitalize()
    cap2 = string2.capitalize()
    
    return cap1 + cap2

print(old_mac('macdonald'))

#Problem2
def master_yoda(text):
    text_list = text.split()
    reverse = reversed(text_list)
    
    return ' '.join(reverse)

#Problem3
def almost_there(n):
    if n in range(90,111):
        return True
    elif n in  range(190,211):
        return True
    else:
        return False


#LEVEL2
#Problem1
def has_33(nums):
    for i in range(len(nums) -1):
        
        if nums[i] == 3 and nums[i+1] ==3:
            return True
    else:
        return False

#Problem 2
def paper_doll(text):
    final_text =''
    for i in text:
        final_text += i * 3
    return final_text


#Problem3
def blackjack(a,b,c):
    if not all(num >= 1 and num <= 11 for num in [a,b,c]):
        return 'One or all numbers exceed 11!'
    if a + b + c > 21 and 11 in [a,b,c]:
        total = a + b + c - 10
        print(total)
    if a + b + c > 21:
        return 'BUST'
    else:
        return a + b + c

#Problem4
def summer_69(arr):
    total = 0
    add = True
    
    for num in arr:
        if num ==6:
            add = False
        elif num == 9:
            add = True
        elif add:
            total += num
    return total


#CHALLENGE
#Problem1
def spy_game(nums):
    final_list = []
    
    for i in nums:
        if i == 0 or i == 7:
            final_list.append(i)
          
    if final_list[:3] == [0,0,7]:
        return True
    else:
        return False

# PROBLEM2
def count_primes(num):
    import math
    primes = [2]
    if num < 2:
        return 0
    if num == 2:
        return 1
    if num > 2:
        for n in range(3, num+1, 2):
            is_prime = True
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
    return len(primes)