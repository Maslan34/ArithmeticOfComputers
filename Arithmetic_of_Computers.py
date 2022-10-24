
"""
    This functions is implementation of the standars of the IEEE 754-2008

"""


def main():
    while True:
        try:
            choice=int(input("Which arhitecture do you want to work with?\n1-64bit or 32bit?->") )
            if choice == 1:
                ArithmeticOfComputers_64Bit()
            elif choice==2:
                ArithmeticOfComputers_32Bit()
            else:
                raise ValueError
        except ValueError:
            print('Wrong input please try again')
            continue
        

    
def ArithmeticOfComputers_32Bit():
    Array_Bit32=[]

    while True:
        try:
            Bit32=str(input("Please enter a 32-bit binary number: -> "))
            break
        except ValueError:
            print('Wrong input please try again')
            continue

    #01000010101000000000000000000000 = 80 

    for i in Bit32:
        Array_Bit32.append(int(i))

    s=Array_Bit32[0]
    c=Array_Bit32[1:9]
    f=Array_Bit32[9:]

    c_sum=0
    f_sum=0

    for index,i in enumerate(c[::-1]):

        if (i) == 1:
            c_sum+=pow(2,index)
  
    for index2,j in enumerate(f):
    
        if (j) == 1:
            f_sum+=pow(2,-(index2+1))

    formula=pow(-1,s)*pow(2,(c_sum-127))*(1+f_sum)

    print("Result: ",formula)

def ArithmeticOfComputers_64Bit():

    #0100000000111011100100010000000000000000000000000000000000000000 =27,56640625
    Array_Bit64=[]

    while True:
        try:
            Bit64=str(input("Please enter a 64-bit binary number: -> "))
            break
        except ValueError:
            print('Wrong input please try again')
            continue



    for i in Bit64:
        Array_Bit64.append(int(i))

    s=Array_Bit64[0]
    c=Array_Bit64[1:12]
    f=Array_Bit64[12:]


    c_sum=0
    f_sum=0

    for index,i in enumerate(c[::-1]):

        if (i) == 1:
            c_sum+=pow(2,index)
    
    for index2,j in enumerate(f):
    
        if (j) == 1:
            f_sum+=pow(2,-(index2+1))

    formula=pow(-1,s)*pow(2,(c_sum-1023))*(1+f_sum)

    print("Result: ",formula)

main()