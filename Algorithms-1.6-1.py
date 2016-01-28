hash_table = set() #sets are objectless hash tables
file = open('algo1-programming_prob-2sum.txt','r')
line = file.readline().split()
while line:
    hash_table.add(int(line[0]))    
    line = file.readline().split()
    
sum_present = [0]*20001
two_sum_count = 0
iter_no = 0
for elem in hash_table:
    iter_no = iter_no + 1
    if iter_no%1000 == 0:
        print(iter_no)
    for val in range(-10000,10001):
        if sum_present[val+10000] == 0:
            conj_elem = val - elem
            if conj_elem in hash_table and conj_elem != elem:
                two_sum_count = two_sum_count + 1
                sum_present[val+10000] = 1
            
print(two_sum_count)