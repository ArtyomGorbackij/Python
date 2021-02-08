counting_dict = {}
max_int = 0
max_count = 0 
numbers = list(map(int, input().split()))
for i in range(0, len(numbers)):
    if numbers[i] in counting_dict:
	    counting_dict[numbers[i]] +=1
	    if max_count == counting_dict[numbers[i]]:
	        if max_int>numbers[i]:
	    	    max_int = numbers[i]
	    if max_count < counting_dict[numbers[i]]:
	        max_count = counting_dict[numbers[i]]
	        max_int = numbers[i]
    elif len(counting_dict) == 0:
        counting_dict[numbers[i]] = 1
        max_int = numbers[i]
        max_count = 1
    else:
        counting_dict[numbers[i]] = 1
        max_count = 1
        if max_int > numbers[i]:
            max_int = numbers[i]

for i in sorted(counting_dict):
    if counting_dict[i] == max_count:
        if i < max_int:
            max_int = i
print(max_int)
