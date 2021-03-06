import time
import os

class Rpi_ScreenSaver:
  rpi_display = "/sys/class/backlight/rpi_backlight/bl_power"
  
  running_on_rpi = False

  display_state = True

  def __init__(self):
    if os.path.exists(self.rpi_display) is True:
      self.running_on_rpi = True

      self.display_on()
  
  def display_on(self):
    if self.running_on_rpi is True:
      f = open(self.rpi_display, "w")
      f.write("0")
      f.close()
    self.display_state = True

  def display_off(self):
    if self.running_on_rpi is True:
      f = open(self.rpi_display, "w")
      f.write("1")
      f.close()
    self.display_state = False


