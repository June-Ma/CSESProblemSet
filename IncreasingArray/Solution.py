def main(n, A):
    steps = 0
    for i in range(1, n):
        if i == 0:
            continue
        else:
            if A[i] - A[i-1] < 0:
                steps += A[i-1] - A[i]
    print(steps)

if __name__ == "__main__":
    n = int(input("Enter the number for n: "))
    if n<1 or n>2*10**5:
        print("n is out of range")
        exit()
        
    A = list(map(int, input("Enter the numbers for A: ").split(",")))
    main(n, A)