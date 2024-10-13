#sort a list in the provided order
def order_list(numbers,order):
    if order=="asc":
        return sorted(numbers)
    elif order=="desc":
        return sorted(numbers,reverse=True) 
    else:
        return numbers
 # example:          
n = order_list([1,2,3],"desc")
print(n)