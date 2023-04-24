
from microbit import *
import math

'''
define a function that sends a control change message.
chan is which MIDI channel that send through.
n is to specifying a control change number.
value is the number that send out.
'''

def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

'''
This is a Python function definition
that sets up the Universal Asynchronous Receiver/Transmitter (UART)
communication on a specific pin in MicroPython.

Start(): This is the name of the function being defined.
When called, this function will initialize UART communication
on a specific pin with the specified settings.

baudrate sets the baud rate for the UART communication
which determines the rate at which data is transmitted and received over the UART.
The baud rate is set to 31250.

bits is the data bits per transmission.

parity sets the parity bit for error checking in the UART communication.
None meaning no parity bit is used.

stop sets the number of stop bits per transmission.

tx=pin0: This parameter specifies the GPIO pin
to use as the transmit (TX) pin for the UART.
'''

def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()

'''
Here are the variables that defined to be the initial status of different
changing values below.
'''
lastA = False
lastB = False
last_roll = 0
last_pitch = 0
last_ang = 0
BUTTON_A_STATE = 0
BUTTON_B_STATE = 0

while True:

    # read new values of current status.
    current_ang = pin2.read_analog()
    current_x = accelerometer.get_x()
    current_y = accelerometer.get_y()
    current_z = accelerometer.get_z()
    a = button_a.is_pressed()
    b = button_b.is_pressed()

    # Checks for changes in button state and sends MIDI control change messages
    if a is True and lastA is False:
        if BUTTON_A_STATE == 0:
            BUTTON_A_STATE = 1
        else:
            BUTTON_A_STATE = 0
        midiControlChange(0, 20, BUTTON_A_STATE)
        lastA = a
    if b is True and lastB is False:
        if BUTTON_B_STATE == 0:
            BUTTON_B_STATE = 1
        else:
            BUTTON_B_STATE = 0
        midiControlChange(0, 21, BUTTON_B_STATE)
        lastB = b

# calculate acceleration vector in x and y plane.
    gx = math.sqrt(current_y*current_y + current_z * current_z)
    gy = math.sqrt(current_x*current_x + current_z * current_z)

# use accelerometer to calculate euler angles
    current_roll = math.atan2(current_x, gx) + 3.14
    current_pitch = math.atan2(current_y, gy) + 3.14

# The code block checks if the current roll, pitch, and angle values
# have changed since the last loop iteration.
# If so, it calculates the corresponding MIDI values for each parameter
# and sends a control change message to the specified MIDI channel.

# get the current number of angle of roll.
    if current_roll != last_roll:
        mod_roll = math.floor(current_roll/6.28 * 127)
        midiControlChange(0, 22, mod_roll)
        last_roll = current_roll

# get the current number of angle of pitch.
    if current_pitch != last_pitch:
        mod_pitch = math.floor(current_pitch/6.28 * 127)
        midiControlChange(0, 23, mod_pitch)
        last_pitch = current_pitch

# get the current number of angle of ang.
    if current_ang != last_ang:
        mod_ang = math.floor((current_ang / 8) - 0.875)
        midiControlChange(0, 25, mod_ang)
        last_ang = current_ang

    sleep(100)
