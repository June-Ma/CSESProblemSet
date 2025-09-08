def main(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 1:
        return main(n * 3 + 1)
    else:
        return main(int(n / 2))

if __name__ == "__main__":
    n = int(input("Put down a number: "))
    main(n)
