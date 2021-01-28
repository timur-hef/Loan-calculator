
import argparse
import math

parser = argparse.ArgumentParser(description="huipstion")

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

arguments = [float(x) for x in [args.principal, args.payment, args.periods, args.interest] if x is not None]

flag = False
for i in arguments:
    if i < 0:
        flag = True


if (args.type is None) or (len(arguments) < 3) or flag:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
    else:
        p = int(args.principal)
        n = int(args.periods)
        i = float(args.interest) / (100 * 12)
        m = 1
        summa = 0
        while m <= n:
            result = math.ceil(p / n + i * (p - p * (m - 1) / n))
            summa += result
            print(f'Month {m}: payment is {result}')
            m += 1
        print(f'Overpayment = {summa - p}')
elif args.type == "annuity":
    import annuity
