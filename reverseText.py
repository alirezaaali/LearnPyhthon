

#First Method

text="learnPython"
reverseText=""
number=-1*(len(text)+1)
for i in range(-1,number,-1):
    reverseText=reverseText+text[i]
print(reverseText)


#Secound Method

text="learnPython"
reverseText=text[::-1]
print(reverseText)



#Third Method

def reverseFunction(text):
    reverseText = text[::-1]
    return reverseText

newText=reverseFunction('learnPython')
print(newText)




