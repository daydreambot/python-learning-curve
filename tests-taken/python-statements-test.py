#TEST1

st = 'Print only the words that start with s in this sentence'

#seperating them to various strings
sub_st = st.split()

#printing out only strings starting with s
for i in sub_st:
    if i[0] == 's':
        print(i)
