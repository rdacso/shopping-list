ourlist = ['puppies']
item = raw_input('Please enter a thing').lower()

def shoppinglist(item):
    if item in ourlist:
    	return "It already exists"
    else: 
    	ourlist.append(item)
    	ourlist.sort()
    	return ourlist



print shoppinglist(item)
print shoppinglist(item).remove()
