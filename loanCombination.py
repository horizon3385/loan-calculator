#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
    
    import sys
    import csv
    import argparse
    from loanCalculator import LoanCalculator

    parser = argparse.ArgumentParser()
    parser.add_argument('--apr', type=float, nargs='+',
        help="APRs for a loan, like 0.07 for 7%%")
    parser.add_argument('--amount', type=float, nargs='+',
        help='Amounts of a loan')
    parser.add_argument('--month', type=int, nargs='+',
        help='Month of a loan')
    args = parser.parse_args()

    def loan(amount, apr, month):
        output = {
            'amount': amount,
            'apr': apr,
            'month': month
        }

        loan = LoanCalculator(amount=amount, apr=apr, month=month)
        total = loan.total_amount()
        payment = loan.month_payment()

        output.update({
            'total': total,
            'payment': payment
            })
        return output

    headers = ['amount', 'apr', 'month', 'total', 'payment']
    writer = csv.DictWriter(sys.stdout, fieldnames=headers)
    writer.writeheader()
    
    for a in args.amount:
        for r in args.apr:
            for m in args.month:
                writer.writerow(loan(a, r, m))


if __name__ == '__main__':
    main()