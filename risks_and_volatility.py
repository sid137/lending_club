from decimal import Decimal

loan_grades = [
  'A1', 'A2', 'A3', 'A4', 'A5', 
  'B1', 'B2', 'B3', 'B4', 'B5', 
  'C1', 'C2', 'C3', 'C4', 'C5', 
  'D1', 'D2', 'D3', 'D4', 'D5', 
  'E1', 'E2', 'E3', 'E4', 'E5', 
  'F1', 'F2', 'F3', 'F4', 'F5', 
  'G1', 'G2', 'G3', 'G4', 'G5'
]

#  Why does their risk adjustment level off in G3??
risk_and_volatility_table_2013 = {
    'A1': Decimal("0.0098"),
    'A2': Decimal("0.0157"),
    'A3': Decimal("0.0257"),
    'A4': Decimal("0.0285"),
    'A5': Decimal("0.0385"),
    'B1': Decimal("0.0511"),
    'B2': Decimal("0.0609"),
    'B3': Decimal("0.0707"),
    'B4': Decimal("0.0806"),
    'B5': Decimal("0.0904"),
    'C1': Decimal("0.0928"),
    'C2': Decimal("0.1026"),
    'C3': Decimal("0.1075"),
    'C4': Decimal("0.1124"),
    'C5': Decimal("0.1222"),
    'D1': Decimal("0.1272"),
    'D2': Decimal("0.1344"),
    'D3': Decimal("0.1370"),
    'D4': Decimal("0.1400"),
    'D5': Decimal("0.1467"),
    'E1': Decimal("0.1544"),
    'E2': Decimal("0.1595"),
    'E3': Decimal("0.1644"),
    'E4': Decimal("0.1693"),
    'E5': Decimal("0.1742"),
    'F1': Decimal("0.1790"),
    'F2': Decimal("0.1823"),
    'F3': Decimal("0.1858"),
    'F4': Decimal("0.1871"),
    'F5': Decimal("0.1878"),
    'G1': Decimal("0.1965"),
    'G2': Decimal("0.1978"),
    'G3': Decimal("0.1984"),
    'G4': Decimal("0.1984"),
    'G5': Decimal("0.1984"),
}

