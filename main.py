from microbit import *
from milestone1_lib import *

# Example: display symbol "R" (for number 2)
display_symbol(2)
sleep(1000)

# Example: drive forward about 1 cm
drive_forward_1cm()
sleep(1000)

# Example: turn until it finds a line
turn_until_on_line()
sleep(1000)

# Example: back up until 20 cm from an object
drive_backward_until_20cm()
sleep(1000)

# Example: follow the line 2 sec → spin until line → repeat 5 times
loop_follow_and_find()
