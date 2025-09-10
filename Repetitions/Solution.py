def main(s):
    maxvalue = 0
    count = 0
    
    for i in range(len(s)):
        if i == 0:
            count = 1
        else:
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
        if count > maxvalue:
            maxvalue = count
    print (maxvalue)


if __name__ == "__main__":
    s = str(input("Enter the string of characters: "))
    main(s)