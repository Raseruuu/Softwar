init python:
    def increasehexadecimal(digit):
        result = ''
        if digit=='1':
            result = '2'
        elif digit=='2':
            result = '3'
        elif digit=='3':
            result = '4'
        elif digit=='4':
            result = '5'
        elif digit=='5':
            result = '6'
        elif digit=='6':
            result = '7'
        elif digit=='7':
            result = '8'
        elif digit=='8':
            result = '9'
        elif digit=='9':
            result = 'a'
        elif digit=='a':
            result = 'b'
        elif digit=='b':
            result = 'c'
        elif digit=='c':
            result = 'd'
        elif digit=='d':
            result = 'e'
        elif digit=='e':
            result = 'f'
        elif digit=='f':
            result = '0'
        elif digit=='0':
            result = '1'
        return result
    def decreasehexadecimal(digit):
        result = ''
        if digit=='1':
            result = '0'
        elif digit=='2':
            result = '1'
        elif digit=='3':
            result = '2'
        elif digit=='4':
            result = '3'
        elif digit=='5':
            result = '4'
        elif digit=='6':
            result = '5'
        elif digit=='7':
            result = '6'
        elif digit=='9':
            result = '8'
        elif digit=='a':
            result = '9'
        elif digit=='b':
            result = 'a'
        elif digit=='c':
            result = 'b'
        elif digit=='d':
            result = 'c'
        elif digit=='e':
            result = 'd'
        elif digit=='f':
            result = 'e'
        elif digit=='0':
            result = 'f'
        return result  
    def increaseip(address,cursor):
        if cursor ==15:
            digittochange = address[18]
            address.replace(address[18],increasehexadecimal(digittochange))
        if cursor ==14:
            digittochange = address[17]
            address.replace(address[17],increasehexadecimal(digittochange))
        if cursor ==13:
            digittochange = address[16]
            address.replace(address[16],increasehexadecimal(digittochange))
        if cursor ==12:
            digittochange = address[15]
            address.replace(address[15],increasehexadecimal(digittochange))


        if cursor ==11:
            digittochange = address[13]
            address.replace(address[13],increasehexadecimal(digittochange))
        if cursor ==10:
            digittochange = address[12]
            address.replace(address[12],increasehexadecimal(digittochange))
        if cursor ==9:
            digittochange = address[11]
            address.replace(address[11],increasehexadecimal(digittochange))
        if cursor ==8:
            digittochange = address[10]
            address.replace(address[10],increasehexadecimal(digittochange))


        if cursor ==7:
            digittochange = address[8]
            address.replace(address[8],increasehexadecimal(digittochange))
        if cursor ==6:
            digittochange = address[7]
            address.replace(address[7],increasehexadecimal(digittochange))
        if cursor ==5:
            digittochange = address[6]
            address.replace(address[6],increasehexadecimal(digittochange))
        if cursor ==4:
            digittochange = address[5]
            address.replace(address[5],increasehexadecimal(digittochange))

        if cursor ==3:
            digittochange = address[3]
            address.replace(address[3],increasehexadecimal(digittochange))
        if cursor ==2:
            digittochange = address[2]
            address.replace(address[2],increasehexadecimal(digittochange))
        if cursor ==1:
            digittochange = address[1]
            address.replace(address[1],increasehexadecimal(digittochange))
        if cursor ==0:
            digittochange = address[0]
            address.replace(address[0],increasehexadecimal(digittochange))
        return address
    def decreaseip(address,cursor):
        if cursor ==15:
            digittochange = address[18]
            address.replace(address[18],decreasehexadecimal(digittochange))
        if cursor ==14:
            digittochange = address[17]
            address.replace(address[17],decreasehexadecimal(digittochange))
        if cursor ==13:
            digittochange = address[16]
            address.replace(address[16],decreasehexadecimal(digittochange))
        if cursor ==12:
            digittochange = address[15]
            address.replace(address[15],decreasehexadecimal(digittochange))


        if cursor ==11:
            digittochange = address[13]
            address.replace(address[13],decreasehexadecimal(digittochange))
        if cursor ==10:
            digittochange = address[12]
            address.replace(address[12],decreasehexadecimal(digittochange))
        if cursor ==9:
            digittochange = address[11]
            address.replace(address[11],decreasehexadecimal(digittochange))
        if cursor ==8:
            digittochange = address[10]
            address.replace(address[10],decreasehexadecimal(digittochange))


        if cursor ==7:
            digittochange = address[8]
            address.replace(address[8],decreasehexadecimal(digittochange))
        if cursor ==6:
            digittochange = address[7]
            address.replace(address[7],decreasehexadecimal(digittochange))
        if cursor ==5:
            digittochange = address[6]
            address.replace(address[6],decreasehexadecimal(digittochange))
        if cursor ==4:
            digittochange = address[5]
            address.replace(address[5],decreasehexadecimal(digittochange))

        if cursor ==3:
            digittochange = address[3]
            address.replace(address[3],decreasehexadecimal(digittochange))
        if cursor ==2:
            digittochange = address[2]
            address.replace(address[2],decreasehexadecimal(digittochange))
        if cursor ==1:
            digittochange = address[1]
            address.replace(address[1],decreasehexadecimal(digittochange))
        if cursor ==0:
            digittochange = address[0]
            address.replace(address[0],decreasehexadecimal(digittochange))
        return address

label iptest:
    
    $current = '10F0:0E73:2B61:A52C'
             # 0123 4567 89AB CDEF
    $cursorcurrent = 15
    label cyclemenutest:
    menu:
        "Choose an option."
        "Up":
            $current = increaseip(current,cursorcurrent)
        "Right":
            $cursorcurrent = cursorcurrent+1
        "Left":
            $cursorcurrent = cursorcurrent-1
        "Down":
            $current = decreaseip(current,cursorcurrent)
    "current ip = [current], cursor is at [cursorcurrent]"
    jump cyclemenutest
        

