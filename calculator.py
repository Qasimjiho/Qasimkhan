numb_1 = float(input('enter number 1 :'))
numb_2 = float(input("enter number 2: "))


choice = input('enter your choice + * - / ')

if choice == '+':
    print(f'Addition :{numb_1 + numb_2}')
if choice == '-':
    print(f'Subsctraion :{numb_1 - numb_2}')
if choice =='*':
    print(f"multiply : {numb_1 * numb_2}")
if choice == "/":
    print(f'devide : {numb_1 / numb_2}')
else:
    print('invalid choice')
    print("THANK YOU FOR USING OVER SMALL PROJECT")
print("THIS PROJECT MAKE BY QASIM JIHO")