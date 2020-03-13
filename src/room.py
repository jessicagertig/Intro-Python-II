# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
  def __init__(self, name, description):
      self.name = name
      self.description = description
      self.n_to = None
      self.s_to = None
      self.e_to = None
      self.w_to = None
      self.things_list = []
  def __str__(self):
      return_string = "---------"
      return_string += "\n\n"
      return_string += self.name
      return_string += "\n\n"
      return_string += self.description
      return_string += "\n\n"
      return_string += f"{self.get_exits_string()}"
      return return_string
  def get_exits_string(self):
      exits = []
      if self.n_to:
          exits.append("[n]orth")
      if self.s_to:
          exits.append("[s]outh")
      if self.e_to:
          exits.append("[e]ast")
      if self.w_to:
          exits.append("[w]est")
      return exits
  # def print_things(self):
  #     if len(self.things_list) > 0: 
  #       print("The room contains: ")
  #       for i in self.things_list:
  #         print(self.things_list[i])
  #     elif len(self.things_list) == 0:
  #       print("The room contains nothing.")
