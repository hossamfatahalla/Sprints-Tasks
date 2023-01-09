#Replace using regex module
import re
string = 'abracadabra'
new_string= re.sub('abracadabra','abrackdabra',string)
print(new_string)


#Replace using slicing method

str = 'abracadabra'
index = 5
new_character = 'k'
str = str[:index] + new_character + str[index+1:]
print(str)
 
  
  
#replac using fun  
def test(string,position,character):
    north=list(string)
    north[position]=character
    string= ''.join(north)
    print(string)

x=input("enter your test: ")
y=int(input("enter num: "))
z=input("enter ur tw: ")
test(x,y,z)

