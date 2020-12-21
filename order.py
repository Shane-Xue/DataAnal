#represents the customer's order; a class

class Order():
    def __init__(self,str):
    """
    The string should contain, respectively:
    0. The number of the order;
       orders that come from the same costomer at the same time may have the same number for convenience
    1. The date of the order, in format yyyymmdd
    2. The day of the week (to analyse data by day of week and work/vac days)
    (If possible whether the day is a workday or holiday should be present too;
       inferences from the day of week might be imprecise)
    3. The time of the order, in format hh:mm:ss or hhmmss
    4. Name of the product (in form of string but most conveniently in the form of a integral)
    (The price of the product can be checked from another file that holds the prices)
    5. The remaining of the line will be seen as comments on the order
    """
    if not assert(type(str)=string):
        raise TypeError(f"input data has wrong type (expected string, got {type(str)} )")
    self.number=None
    self.date=None
    self.day=None
    self.time=None
    self.name=None
    self.comments=None
