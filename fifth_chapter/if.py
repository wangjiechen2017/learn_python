name = 'wangjiEchen'
name2 = 'wAngJieChen'
print(name == name2.lower())


age = 12

if age<4:
	print('<4')
elif age<18:
	print('<18')
else:
	print('>=18')


list1 = [1,2,3,5,7,9]
list2 = [1,3,5,7,9]
for element in list1:
	if element in list2:
		print(str(element)+' is in the list2')
	else:
		print(str(element)+' is not in the list2')
 
