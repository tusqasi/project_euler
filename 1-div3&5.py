'''
##this is problem-1
##read the problems**
##out = 233168
'''
##                  {       }
list_100 = list(range(1,1000))


lst_div_3n5 = []

for i in list_100:
	if (i%3) == 0:
		lst_div_3n5.append(i)
		
	elif(i%5) == 0:
		lst_div_3n5.append(i)

garbage = 0
for i in lst_div_3n5:
	garbage = garbage + i
print (garbage)
print(lst_div_3n5)