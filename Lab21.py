import argparse

parser = argparse.ArgumentParser(description='Doing Math')
parser.add_argument('-n1','--num1', type=int, help='This is Integer No 1')
parser.add_argument('-n2','--num2', type=int, help='This is Integer No 2')
parser.add_argument('-n3','--num3', type=int, help='This is Integer No 3')
parser.add_argument('-c',"--calculation", help="This will do the Math operations", choices=["add", "sub", "mult"])
args = parser.parse_args()

print(f'n1 = {args.num1}')
print(f'n2 = {args.num2}')
print(f'n3 = {args.num3}') 


n1 = args.num1
n2 = args.num2
n3 = args.num3

if args.calculation == "add":
    result = n1 + n2 + n3
    print(f'addition result of n1 + n2 + n3 is {result}')
elif args.calculation == "sub":
    result = n1 - n2 - n3
    print(f'substraction result of n1 - n2 - n3 is {result}')
elif args.calculation == "mult":
    result = n1 * n2 * n3
    print(f'multiplication result of n1 * n2 * n3 is {result}')
else:
    print("Incorrect option")
