# Write a class to hold player information, e.g. what room they are in
# currently.
import cmd
import textwrap
import sys
import os
import time
import random

class Player:
    def __init__(self, name, quilter_type, player_location = 'outside', craft_skill = 0, money = 0, color_skill = 0, bargain_skill = 0):
      self.name = name
      self.player_location = player_location
      self.quilter_type = quilter_type
      self.player_location = player_location
      self.craft_skill = craft_skill
      self.money = money
      self.color_skill = color_skill
      self.bargain_skill = bargain_skill
