import argparse

parser = argparse.ArgumentParser(description='Simple calculator')
parser.add_argument('num1', type=float, help='First number')
parser.add_argument('operator', type=str, choices=['+', '-', '*', '/'], help='Operator')
parser.add_argument('num2', type=float, help='Second number')

args = parser.parse_args()

if args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
elif args.operator == '/':
    result = args.num1 / args.num2

print(f"Result: {result}")
