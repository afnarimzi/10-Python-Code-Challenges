def filter_integer(user_input):
    integer_list=[]
    for n in user_input:
        if n.isdigit():
            integer_list.append(int(n))
    return integer_list
user_input=(input("Enter a list with non_integers and string: "))
result=filter_integer(user_input)
print("New list with only the integer={}".format(result))        