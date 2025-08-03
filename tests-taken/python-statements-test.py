#TEST1

st = 'Print only the words that start with s in this sentence'

#seperating them to various strings
sub_st = st.split()

#printing out only strings starting with s
for i in sub_st:
    if i[0] == 's':
        print(i)

#TEST2
#Printing even numbers betwen 0 to 10

for i in range(0,11):
    if i%2 == 0:
        print(i)

#TEST3
#Use a List Comprehension to create a list of all numbers
#between 1 and 50 that are divisible by 3
num1 = [i for i in range(51) if i%3 ==0]
print(num1)

#TEST4
#Printing words with an even numbered length
st2 = 'Print every word in this sentence that has an even number of letters'

#List each word in st2 variable
even_st2 = st2.split()

#Check each word length 
for i in even_st2:
    if len(i) % 2 == 0:  #Check the even lengthed words and print
        print(i)

#TEST5
# Write a program that prints the integers from 1 to 100.
#But for multiples of three print "Fizz" instead of the number
#and for the multiples of five print Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    #Check if it is multiples of both 3 and 5 
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0: #Check multiples of 3
        print("Fizz")
    elif i%5 == 0: #Check multiples of 5
        print("Buzz")
    else:
        print(i)

#TEST6
# Create a list of the first letter of every word in the string
st3 = 'Create a list of the first letters of every word in this string'

split_st3 = st3.split()  #Splitting the string
#Putting the first letters of each word in a list
list_st3 = [i[0] for i in split_st3] 
print(list_st3)
