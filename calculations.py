#!/usr/bin/env python

class Note(object):
  lending_club_base_interest_rate = 0.0505

  def interest_rate(self):
      """docstring for interest_rate"""
      self.interest_rate = self.lending_club_base_interest_rate + self.risk_and_volatility_adjustment()



