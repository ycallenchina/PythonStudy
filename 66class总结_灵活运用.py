

class list_update(list):


	def print_lines(self): 
		for i in self:
			print(i)


x=list_update([1,2,3])
x.print_lines()



class list_update2(list):


	def __repr__(self): 
		for i in self:
			print(i)
		return ''

y=list_update2([1,2,3])
print(y)

