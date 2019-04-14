#!usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhangshuai time:2019/3/30
from pyfirmata import Arduino, util
import time
board = Arduino("COM3")
# loopTimes = input('How many times would you like the LED to blink:\n ')
# print("Blinking " + loopTimes + " times.")
# for x in range(int(loopTimes)):
#     board.digital[13].write(1)
#     time.sleep(0.2)
#     board.digital[13].write(0)
#     time.sleep(0.2)
def server_run(degree):
    board.servo_config(9, angle=degree)


    # time.sleep(1)
    # board.servo_config(9, angle=500)
    # time.sleep(1)
    # board.servo_config(9, angle=800)
    # time.sleep(1)