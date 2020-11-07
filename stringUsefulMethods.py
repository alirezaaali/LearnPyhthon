'''
Here is some useful string methods
You can find more information in
https://www.w3schools.com/python/python_ref_string.asp
'''
a = '     This is a simple string to test some methods     '
print('This is type(a): ')
print(type(a))
print('-------------------------')
print('This is len(a): ')
print(len(a))
print('-------------------------')
print('This is a.strip(): ')
print(a.strip())
print('-------------------------')
print('This is a.lower(): ')
print(a.lower())
print('-------------------------')
print('This is a.upper(): ')
print(a.upper())
print('-------------------------')
print('This is a.replace("s","K"): ')
print(a.replace('s', 'K'))
print('-------------------------')
print('This is a.split(" "): ')
print(a.split(' '))
print('-------------------------')
print('We are going to fin ing in a [x = "ing" in a]: ')
print("ing" in a)
print("ing" not in a)
print('-------------------------')
print('this is format()')
sometext = "This is testing method named:{0}, which is great way to format {1} "
print(sometext.format("str_var.format()", sometext))
print('-------------------------')
print('Scape character is backslash \"\\"')
print('We are the so-called \"Vikings\" from the north.')
print('-------------------------')
print('This is new line \n \t which followed by tab and backspace')
