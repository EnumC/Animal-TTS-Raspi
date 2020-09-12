# Animal-TTS-Raspi
More input shenanigans. This time, with dogs!
This project is based on the premise of associative learning, which may allow for concise communications between humans and animals.

### Project Features
Utilizes modified 60mm buttons as input devices, and output the interpreted inputs via a TTS library over audio out.
Inputs can also be used to directly toggle IoT devices. 
The 60mm buttons can eventually be replaced by capacitive touch targets for space optimization and improved aesthetics.

### Getting Started
This project is written in Python and relies on the RPi.GPIO library for input interrupts. Text-To-Speech is powered by Google Cloud's Text-To-Speech API with WaveNet. Additional experimental features relies on libraries such as: python-kasa, Beautiful Soup, and Requests. 

To run the script, first install all dependencies by running:

`pip install -r requirements.txt`

To start, enter: 

`sudo python startTTS.py`

Requires Python >3.0.


### More resources:
https://www.akc.org/expert-advice/training/can-dogs-talk-one-speech-pathologist-says-yes/
