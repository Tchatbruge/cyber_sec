
def nospace(message):
    nospace = " "
    for i in message :
        if i != "" :
            nospace += i 
    
    return nospace

def conversion(text):
    num_message = [ord(char) for char in nospace(text)]
    return num_message

def encrypt( message , k ):
    num_message = conversion(message) 
    num_encrypt_message = [(num+k) for num in num_message ] 
    encrypt_message = ''.join([chr(value) for value in num_encrypt_message])
    return encrypt_message

def decrypt(message , k):
    num_message = conversion(message) 
    num_decrypt_message = [ (num - k) for num in num_message ] 
    decrypt_message = ''.join([chr(value) for value in num_decrypt_message])
    return decrypt_message

message = "WYTF"


encrypte = encrypt( message , 2 )
print("crypted : ", encrypte )

print("decypher :", decrypt(encrypte , 2 ) )









    
    
   