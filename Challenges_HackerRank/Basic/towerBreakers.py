# HackerRank Mode:
def towerBreakers(n, m):
    if m == 1:
        return 2
    if n % 2 == 0:
        return 2
    return 1

#LocalMode:

# t = int(input("Enter the number of test cases: ").strip())

# for _ in range(t):
#     n, m = map(int, input("Enter the number of towers and the height of towers:").split())
#     print("Winner:", towerBreakers(n, m))