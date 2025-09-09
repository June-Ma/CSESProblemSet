def main(n, A):
    s1 = n * (n + 1) // 2
    s2 = 0
    for i in range(len(A)):
        s2 += A[i]
    
    m = s1 - s2
    print(m)

if __name__ == "__main__":
    n = int(input("Enter the number for n: "))
    if n<2 or n>2*10**5:
        print("n is out of range")
        exit()
        
    A = list(map(int, input("Enter the numbers for A: ").split()))
    main(n, A)