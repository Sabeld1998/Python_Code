phoneNum = input("Enter phone number:")
finalNum = ""
for Num in phoneNum: 
    if (ord (Num) >=47 and ord(Num)<=57):
                finalNum+=Num
    
    Num = Num.upper()
    if (ord(Num) >=65 and ord(Num)<=90):
       
        #A, B, and C = 2
        if (ord(Num) == 41 or ord(Num)==42 or ord(Num) == 46):
            finalNum+= '2'
    # D, E, and F = 3
        if (ord(Num) == 68 or ord(Num)==69 or ord(Num) == 70):
            print(Num)
            finalNum+='3'
    # G, H, and I = 4
        if (ord(Num) == 71 or ord(Num)==72 or ord(Num) == 73):
            print(Num)
            finalNum+='4'
    # J, K, and L = 5
        if (ord(Num) == 74 or ord(Num)==75 or ord(Num) == 76):
            print(Num)
            finalNum+='5'
    # M, N, and O = 6
        if (ord(Num) == 77 or ord(Num)==78 or ord(Num) == 79):
            print(Num)
            finalNum+='6'
    # P, Q, R, and S = 7
        if (ord(Num) == 80 or ord(Num)==81 or ord(Num) == 82 or ord(Num) ==83):
            print(Num)
            finalNum+='7'
    # T, U, and V = 8
        if (ord(Num) == 84 or ord(Num)==85 or ord(Num) == 86):
            print(Num)
            finalNum+='8'

    # W, X, Y, and Z = 9
        if (ord(Num) == 87 or ord(Num)==88 or ord(Num) == 89 or ord(Num) ==90):
            print(Num)
            finalNum+='9'
    
print(finalNum)
