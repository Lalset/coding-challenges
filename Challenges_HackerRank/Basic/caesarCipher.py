import os

# HackerRank Mode:

def caesarCipher(s, k):
    encryp_text = ""

    for char in s:
        if char.isalpha():  
            shift = k % 26  
            if char.islower():
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encryp_text += new_char
        else:
            encryp_text += char  

    return encryp_text
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
