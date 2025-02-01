def miniMaxSum(arr):
    arr.sort()
    
    min_sum = sum(arr[:4])
    
    max_sum = sum(arr[1:])
    
    print(min_sum, max_sum)

if __name__ == '__main__':
    # Local Mode: manual input
    input = input("Digite 5 números separados por espaço: ")
    arr = list(map(int, input.split()))
        
    if len(arr) != 5:
        print("Por favor, insira 5 números.")
    else:
        miniMaxSum(arr)

    #HackerRank Mode: automatic input
    #arr = list(map(int, sys.stdin.readline().rstrip().split()))
    #miniMaxSum(arr)