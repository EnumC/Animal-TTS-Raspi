# Copyright 2020 Eric Qian.
# GNU GPLv3 License. See LICENSE

import RPi.GPIO as GPIO

import time

from typing import Optional, List

btnDef = {
    # assign board pin to word/phrase
    29: "water",
    31: "food",
    33: "outside",
    35: "poop"
}

stringBuffer: str = ""


def intrHandler(pin) -> None:
    global stringBuffer
    stringBuffer = stringBuffer + btnDef[pin] + " "


def initGPIO(inputs: List[Optional[int]],
             outputs: List[Optional[int]]) -> None:
    GPIO.setmode(GPIO.BOARD)  # use pin numbering

    for button in inputs:
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(button,
                              GPIO.RISING,
                              callback=intrHandler,
                              bouncetime=300)

    for led in outputs:
        GPIO.setup(led, GPIO.OUT)


def main() -> None:
    initGPIO(btnDef.keys(), None)


if __name__ == "__main__":
    main()
