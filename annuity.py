import math


def number_month(p, a, i):
    result = math.log(a / (a - i * p), 1 + i)
    return math.ceil(result)


def monthly_payment(p, n, i):
    result = p * i * ((1 + i) ** n) / ((1 + i) ** n - 1)
    return math.ceil(result)


def loan_principal(a, n, i):
    result = a / (i * (1 + i) ** n / ((1 + i) ** n - 1))
    return round(result)


from creditcalc import args

if args.periods is None:
    p = int(args.principal)
    a = int(args.payment)
    i = float(args.interest) / (100 * 12)
    result = number_month(p, a, i)
    year = result // 12
    months = result % 12
    if year == 0 and months > 1:
        print(f'It will take {months} months to repay this loan!')
    elif year == 0 and months == 1:
        print(f'It will take 1 month to repay this loan!')
    elif year == 1 and months == 0:
        print(f'It will take 1 year to repay this loan!')
    elif year > 1 and months == 0:
        print(f'It will take {year} years to repay this loan!')
    else:
        print(f"It will take {year} years and {months} months to repay this loan!")
    print(f'Overpayment = {a * result - p}')
elif args.payment is None:
    p = int(args.principal)
    n = int(args.periods)
    i = float(args.interest) / (100 * 12)
    result = monthly_payment(p, n, i)
    print(f'Your monthly payment = {result}!')
    print(f'Overpayment = {n * result - p}')
else:
    n = int(args.periods)
    i = float(args.interest) / (100 * 12)
    a = int(args.payment)
    result = loan_principal(a, n, i)
    print(f'Your loan principal = {result}!')
    print(f'Overpayment = {n * a - result}')