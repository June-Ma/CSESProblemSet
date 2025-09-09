def main(n, A):
    A.sort()
    for i in range(n):
        if A[i] == i + 1:
            continue
        else:
            print(i + 1)
            break

if __name__ == "__main__":
    n = int(input("Enter the number for n: "))
    if n<2 or n>2*10**5:
        print("n is out of range")
        exit()
        
    A = list(map(int, input("Enter the numbers for A: ").split()))
    main(n, A)