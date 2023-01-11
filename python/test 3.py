def brackets(expression):
   all_br = ['()', '{}', '[]']
   while any(x in expression for x in all_br):
      for br in all_br:
         expression = expression.replace(br, '')
   return not expression

# calling the function
input_string = input(" enter in: ")
if brackets(input_string):
   print(input_string,"balanced")
else:
   print(input_string,"Not balanced")