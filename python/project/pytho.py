import datetime
import os
with open( 'daily.csv' , 'a' ) as f:

    name=input("enter your name: ")
    phone=input("enter your num: ")
    email=input("enter your email: ")
    address=input("enter your address: ")
    list_contact=[name,phone,email,address]
    date_created = datetime.datetime.now().isoformat()
    
    
    f.writelines([",".join([str(i) for i in [name,email,phone,address,date_created] ]) ])
    
    


    


#print(list_contact)

#with open( 'daily.txt' , 'w') as f:
    #for i in list_contact:
        #print(i)
        
        























#class Contact:
    #def __init__ (self, name, contact_number, email, address, date_created=None, date_updated=None):
     #   self.name = name
     #   self.contact_number = contact_number
     #   self.email = email
     #   self.address= address
     #   self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
     #   self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()
     #   print(name,contact_number,email,address)
#ans=Contact("ali" , 12345 , "ahmed@gmail" , "alex")
#l_ans=[].append
#ans=l_ans
#with open( 'daily.txt' , 'w') as f:
#    f.write(ans)
#    print('daily.txt')





#l_ans=[].append
#ans=l_ans





