class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
      self.total = 0
      self.employee_discount = emp_discount
      self.items = []

    def add_item(self, name, price, quantity=1):
       for q in range(0,quantity):
          self.items.append({'item_name': name, 'unit_price': price})
          self.total += price
          
       return self.total

    def mean_item_price(self):
       return self.total/len(self.items)

    def median_item_price(self):
        prices = [item['unit_price'] for item in self.items]
        l = len(prices)
        if l%2 != 0:
           return prices[l//2]
        else: 
           return sum(prices[l/2-1:l/2+1])/2

    def apply_discount(self):
       if self.employee_discount is not None:
          return round(self.total*(1-self.employee_discount/100), 2)
       else:
          return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items is []:
           return "There are no items in your cart!"
        else:
           self.total -= self.items[-1]['unit_price']
           self.items.pop()