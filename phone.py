from item import Item

class Phone(Item):
  pay_rate = 0.5
  def __init__(self, name: str, price: float, quantity: int=0, broken_phones: int=0):
    # Call to super function to access all attb/methods
    super().__init__(
      name, price, quantity
    )

    # Run validations on the received arguments
    assert broken_phones >= 0, f'Broken phones {broken_phones} is not greater than or equal to zero!'

    # Assign to self object
    self.broken_phones = broken_phones