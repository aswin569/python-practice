customer = 5
bag = 1
security_check = True

for customers in range(1,customer+1):
    for bags in range(1,bag+1):

       if security_check == True:
          print("Customer :", customers , "Bag :", bags , "bag cleared")
       else:
          print("Security check uncleared")



