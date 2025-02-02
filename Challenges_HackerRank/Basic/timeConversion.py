import os

def timeConversion(s):
    
    period = s[-2:]
    hh,mm,ss = map(int, s[:-2].split(":"))
    
    if period == "AM":
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12
    
    return f"{hh:02}:{mm:02}:{ss:02}"

if __name__ == '__main__':
    # Local Mode
    
    #s = input("Enter a time in the format hh:mm:ssAM/PM: ").strip()
    #result = timeConversion(s)
    #print("Converted Time:", result)
    
    
    # HackerRank Mode
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
