# Encrypt or decrypt a message using Caesar cipher.
    
#     Encryption and decryption is determined by the Boolean value in decrypt. Key determines the number of 
#     places a character is shifted. When encrypting, use the positive value of key to shift the characters forward; 
#     when decrypting, use the negative key to shift the characters backward. 
    
#     The function should maintain characters that are not letters without change; for example, spaces, punctuations, 
#     and numbers should not be encrypted or decrypted. Additionally, the case of the letters should be preserved, 
#     small letters are transformed to other small letters and capital letters are transformed to capital letters.
    
#     Use the function `shift` (provided later) to shift each character in message by the number in key.
    
#     args:
#         message: string to be encrypted or decrypted
#         key: number of places to shift the characters (always positive)
#         decrypt: Boolean; when False the message is encrypted,  when True the message is decrypted
        
#     returns:
#         transformed_message: encrypted (or decrypted) message
        
#     examples:
#         Encryption
#         ==  transform("deal", 1, False) returns:
#             "efbm"
        
#         ==  transform("deal", 2, False) returns:
#             "fgcn"
        
#         ==  transform("deal", 30, False) is equivalent to transform(message, 4, False)
#             "hiep"
        
#         Decryption
#         ==  transform("efbm", 1, True) returns:
#             "deal"
            
#         ==  transform("fgcn", 2, True) returns:
#             "deal"
            
#         ==  transform("hiep", 30, True) returns:
#             "deal"    

message = 'hello world'

def transform(message, key, decrypt):

    nw_message = ''
    if decrypt:
        for i in message:
            try:
                nw_message = nw_message + shift(i, -(key))
            except TypeError:
                nw_message = nw_message + ' '
        
        return nw_message
    
    else:
        for i in message:
            try:
                nw_message = nw_message + shift(i, key)
            except TypeError:
                nw_message = nw_message + ' '
        
        return nw_message
    
        


def shift(char, key):    
   
    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    for i in range(len(alphabet)):
        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]
 
    if char.isalpha():
        char_index = alphabet.index(char.lower())
        shifted_char = shifted_alphabet[char_index]
    
        # keep char's case (upper or lower)
        if char.isupper():
            return shifted_char.upper()
        else:
            return shifted_char


x = transform(message, 1, False)

print(x)