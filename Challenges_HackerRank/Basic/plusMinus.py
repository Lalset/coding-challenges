def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
            
    total = len(arr)
    positive_ratio = positive_count / total
    negative_ratio = negative_count / total
    zero_ratio = zero_count / total
    
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    # HackerRank mode
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    # Local mode (for local testing)
    """
    n = int(input("Enter the size of the array: ").strip())
    print(f"Enter the {n} elements of the array (separated by space):")
    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
    """