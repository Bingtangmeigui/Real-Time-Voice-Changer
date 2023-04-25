# Real-Time Voice Changer
This is an interesting product for changing the tone of human voices. It consists of two main parts, micro-bit as controller and purr-data as digital signal processing engine.
## Features

Real-time control and modulate your voice. Controlling the constant change of the tone, which can be applied in the future in the field of game live broadcasting or gaming to improve entertainment.
## File description

* [real-time voice changer.py](./real-time voice changer.py) is for the microbit to transmit gesture and button pressed information and potentiometer information.

* [IAM20230228_final2.pd](./IAM20230228_final2.pd) contains the main audio processing module, which includes pitch changes and ring modulator processing of the sound.

* [dw.pd](dw.pd) is a subfile of the [IAM20230228_final2.pd](./IAM20230228_final2.pd). Contains the signal path that adjusts the ratio of the two audio paths to the output.
