#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from math import exp, log1p, pow

class LoanCalculator:
    """A Class to calculate monthly payment for a loan

    amount: the total loan amount
    apr: the apr for a loan
    month: the length of a loan"""
    def __init__(self, amount, apr, month):
        
        assert isinstance(amount, float) or isinstance(amount, int)
        assert 0 <= apr < .1
        assert isinstance(month, int)

        self.amount = amount
        self.apr = apr
        self.mpr = exp(log1p(self.apr) / 12) - 1
        self.month = month

    def total_amount(self):
        """total_amount method: total amount value of a loan"""
        return self.amount * pow((1 + self.mpr), self.month)

    def month_payment(self):
        """month_payment method: monthly payment of a loan"""
        return (self.amount * self.mpr * pow((1 + self.mpr), self.month)) / (pow((1 + self.mpr), self.month) - 1)


def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--apr', type=float,
        help="loan APR, like 0.07 for 7%% APR")
    parser.add_argument('--month', type=int,
        help="the duration in month of a loan")
    parser.add_argument('--amount', type=float,
        help="the total amount of a loan")
    args = parser.parse_args()

    loan = LoanCalculator(args.amount, args.apr, args.month)
    r = loan.mpr
    total = loan.total_amount()
    fee = loan.month_payment()
    print '\nMonth\t%d' % args.month
    print 'APR\t%.2f%%\t\tMPR\t%.2f%%' % (100 * args.apr, 100 * r)
    print 'Amount\t%.2f\tTotal\t%.2f' % (args.amount, total,)
    print '\nMonthly Payment\t%.2f\n' % fee


if __name__ == '__main__':
    main()