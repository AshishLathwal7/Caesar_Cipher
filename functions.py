
def shift( msg ,key):
    encrypted_msg = ''
    for i in range(len(msg)):
        encrypted_msg += chr(chk_shift(char= ord(msg[i]), key= key) - key)

    return encrypted_msg

def chk_shift(char ,key):
    if char - key < ord('a'):
        char += 26
    elif char - key > ord('z'):
        char -= 26

    return char
    
