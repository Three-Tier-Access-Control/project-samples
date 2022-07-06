import I2C_LCD_driver as I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Three Tier", 1)
mylcd.lcd_display_string("Security System", 2)
