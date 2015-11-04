import random

ran_num1 = [random.randint(0,10000) for r in xrange(100)] # v1
# ran_num1 = [5,4,3,2,1]
# ran_num2 = [random.choice([i for i in xrange(10000)]) for r in xrange(10)] # v2 
print ("original"), ran_num1
for j in range(0, len(ran_num1)-1):
	for i in range(0, len(ran_num1)-1):
		if ran_num1[i] > ran_num1[i + 1]:
			ran_num1[i], ran_num1[i + 1] = ran_num1[i + 1], ran_num1[i]
print ("finished sort"), ran_num1
