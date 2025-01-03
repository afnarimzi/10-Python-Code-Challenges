def balance():
    string=input("Enter a string :")
    countX=0
    countO=0
    for x in string.lower():
        if x=='x':
            countX=countX+1
        elif x=='o':
            countO=countO+1    
    if countX==countO:
     print(True) 
    else:
      print(False)   
balance() 



