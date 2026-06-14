from microbit import *
from Freenove_Micro_Rover import *

Rover = Micro_Rover()

def display_symbol(number):
    symbols = {
        1: "L",
        2: "R",
        3: "S",
        4: "U",
        5: "E",
        6: "*"
    }
    if number in symbols:
        display.show(symbols[number])
    else:
        display.show("?")

def drive_forward_1cm():
    Rover.motor(60, 60)
    sleep(150)  # adjust this experimentally to be ~1 cm
    Rover.motor(0, 0)

def turn_until_on_line():
    Rover.motor(60, -60)
    while (
        pin14.read_digital() == 0 and
        pin15.read_digital() == 0 and
        pin16.read_digital() == 0
    ):
        Rover.motor(60, -60)
    Rover.motor(0, 0)

def drive_backward_until_20cm():
    while Rover.get_distance() > 20:
        Rover.motor(-60, -60)
    Rover.motor(0, 0)

def loop_follow_and_find():
    for _ in range(5):
        start_time = running_time()
        while running_time() - start_time < 2000:
            sensor_value = (
                pin14.read_digital() << 2 |
                pin15.read_digital() << 1 |
                pin16.read_digital()
            )
            if sensor_value == 7:
                Rover.motor(60, 60)
            elif sensor_value in [2, 5]:
                Rover.motor(60, 60)
            elif sensor_value in [4, 6]:
                Rover.motor(30, 70)
            elif sensor_value in [1, 3]:
                Rover.motor(70, 30)
            elif sensor_value == 0:
                Rover.motor(0, 0)
        Rover.motor(0, 0)
        Rover.motor(60, -60)
        while (
            pin14.read_digital() == 0 and
            pin15.read_digital() == 0 and
            pin16.read_digital() == 0
        ):
            Rover.motor(60, -60)
        Rover.motor(0, 0)
