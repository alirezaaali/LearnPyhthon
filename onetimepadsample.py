# import onetimepad

# inputstring = input("Please enter you text:")
# inputKey = input("Please Enter your Key:")
# cipher = onetimepad.encrypt(inputstring, inputKey)
# print("Entered text is: ",inputstring)
# print("Your key is:",inputKey)
# print("Here is Encrypted string:",cipher)
# secoundky = input("Please Enter your Key to decrypt:")
# print("Plain text is: ",onetimepad.decrypt(cipher, secoundky))
# # msg =

# # print(msg)

import onetimepad

inputMsg = input("Please Enter Your Message:")
inputKey = input("Please Enter Your Key:")
cipher = onetimepad.encrypt(inputMsg, inputKey)
print("Here is Encrypted Message:", cipher)
decryptedMsg = onetimepad.decrypt(cipher, inputKey)
print("Message is: ", decryptedMsg)



