def doubled(user_input):
    string=''
    for n in user_input:
        string=string+2*n
    return string    
        
user_input=input("Enter a string : ") 
print(doubled(user_input)) 