import csv

class Item:
  pay_rate = 0.8 # The pay rate after 20 percent discount
  all:list = []
  def __init__(self, name: str, price: float, quantity: int=0):
    # Run validations on the received arguments
    assert price >= 0, f'Price {price} is not greater than or equal to zero!'
    assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

    # Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    self.price = self.price * self.pay_rate

  @classmethod
  def instantiate_from_csv(cls):
    with open('items.csv', 'r') as file:
      reader = csv.DictReader(file)
      items = list(reader)

    for item in items:
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = int(item.get('quantity'))
      )

  @staticmethod
  def check_integer(num):
  # We will count the floats that are point zero i.e 10.0, 20.0
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False

  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"