class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

class Fabric(Item):
  def __init__(self, name, description, yards):
    super().__init__(name, description)
    self.yards = yards
  def __str__(self):
    return 'You have found {self.yards} yards of {self.name}: {self.description}'.format(self=self)
  
    