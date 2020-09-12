# Copyright 2020 Eric Qian.
# GNU GPLv3 License. See LICENSE

import RPi.GPIO as GPIO
import time
from typing import Optional, List
from google.cloud import texttospeech as tts
from os import path

btnDef = {
    # assign board pin to word/phrase
    29: "water",
    31: "food",
    33: "outside",
    35: "poop"
}

stringBuffer: str = ""


def text_to_wav(voice_name, text):
    language_code = '-'.join(voice_name.split('-')[:2])

    filename = f'audio/{language_code}_{voice_name}_{text}.wav'
    
    # check if audio already cached
    if path.exists(filename):
        print(filename + " already exists!")
    else:
        text_input = tts.SynthesisInput(text=text)
        voice_params = tts.VoiceSelectionParams(
            language_code=language_code,
            name=voice_name)
        audio_config = tts.AudioConfig(
            audio_encoding=tts.AudioEncoding.LINEAR16)

        client = tts.TextToSpeechClient()
        response = client.synthesize_speech(
            input=text_input,
            voice=voice_params,
            audio_config=audio_config)

        
        with open(filename, 'wb') as out:
            out.write(response.audio_content)
            print(f'Audio content written to "{filename}"')


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
    text_to_wav('en-US-Wavenet-A', "This is a test clip.")


if __name__ == "__main__":
    main()
