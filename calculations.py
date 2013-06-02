#!/usr/bin/env python

class Note(object):
  lending_club_base_interest_rate = 0.0505 # 5.05%

  def interest_rate(self):
      """ 
      https://www.lendingclub.com/account/rateDetail.action
      interest_rate = Lending Club Base Rate + Adjustment for Risk & Volatility
      """
      self.interest_rate = self.lending_club_base_interest_rate + self.risk_and_volatility_adjustment()



