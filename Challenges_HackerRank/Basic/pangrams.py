# HackerRank Input Mode:

import os 
def pangrams(s):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    return "pangram" if set(s.lower()) >= letters else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

# Local Mode:

# s = input("Enter a sentence: ")
# print(pangrams(s))