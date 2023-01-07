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
 