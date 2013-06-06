#!/usr/bin/env python
from decimal import Decimal


loan_grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
sub_grades = [1, 2, 3, 4, 5]
lending_club_base_interest_rate = Decimal("0.0505")

def initial_scoring(application):
  score = 600
  return score

def proprietary_scoring(score, fico_score, application):
    """docstring for proprietary_scoring"""

    model_rank = 16 # 1 - 25
    return model_rank

base_risk_sub_grade_table = {
    1: 'A1',
    2: 'A2',
    3: 'A3',
    4: 'A4',
    5: 'A5',
    6: 'B1',
    7: 'B2',
    8: 'B3',
    9: 'B4',
    10: 'B5',
    11: 'C1',
    12: 'C2',
    13: 'C3',
    14: 'C4',
    15: 'C5',
    16: 'D1',
    17: 'D2',
    18: 'D3',
    19: 'D4',
    20: 'D5',
    21: 'E1',
    22: 'E2',
    23: 'E3',
    24: 'E4',
    25: 'E5'
}

def base_risk_sub_grade(model_rank):
    """docstring for base_risk_sub_grade"""
    return base_risk_sub_grade_table[model_rank]

def final_sub_grade(base_risk_sub_grade, loan_amount, term):


def risk_and_volatility_adjustment(loan_grade):
    """ Function of loan grade, assigned by LC
    https://www.lendingclub.com/account/rateDetail.action
    """
    return risk_and_volatility_table[loan_grade]

def interest_rate(loan_grade):
    """ https://www.lendingclub.com/account/rateDetail.action
    interest_rate = Lending Club Base Rate + Adjustment for Risk & Volatility
    """
    return lending_club_base_interest_rate + risk_and_volatility_adjustment(loan_grade)


def apr(interest_rate, something):
    """docstring for apr"""
    return interest_rate + something




class Note(object):
  lending_club_base_interest_rate = Decimal("0.0505")

  def interest_rate(self):
      """ 
      https://www.lendingclub.com/account/rateDetail.action
      interest_rate = Lending Club Base Rate + Adjustment for Risk & Volatility
      """
      self.interest_rate = self.lending_club_base_interest_rate + self.risk_and_volatility_adjustment()



