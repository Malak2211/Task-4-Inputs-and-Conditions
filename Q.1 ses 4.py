grade=int(input('please enter your grade:  '))
if grade>=90 and grade<=100 :
    print('A')
elif grade>=80 and grade<=89:
    print('B')
elif grade>=70 and grade<=79:
    print('C')
elif grade>=60 and grade<=69:
    print('D')
elif grade>=0 and grade<=59:
    print ('F')
else: print("invalid degree :(")