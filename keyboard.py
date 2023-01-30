from item import Item

class Keyboard(Item):
  pay_rate = 0.7
  def __init__(self, name: str, price: float, quantity: int=0):
    # Call to super function to access all attb/methods
    super().__init__(
      name, price, quantity
    )