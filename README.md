# SoundShare
*SoundShare* is a simple application to allow audio from one PC to be transmitted over a local network and played on another PC.

:warning: **This repo has no error handling and has only been tested in Windows.**

## Install
The project uses [Python](https://www.python.org/) and requires [PyAudio](https://pypi.org/project/PyAudio/) which can be installed with
```
$ pip install PyAudio
```

## Usage
The host which is sending the audio data is the *transmitter* and the host which is receiving and playing the audio data is the *receiver*.

Firstly, the receiver should execute `receiver.py`
```
$ python receiver.py
```
This will describe the local IP and port number which the transmitter will be asked for upon executing `transmitter.py`
```
$ python transmitter.py
```
Additionally, the transmitter will be asked which audio device to record from. Typically, only input devices such as microphones will be supported.

To allow for recording for 'what you hear', on Windows, go to the *Sound Control Panel*, navigate to the *Recording* tab, and enable 'Stereo Mix'. This device will now appear in the menu given when executing `transmitter.py`. If 'Stereo Mix' does not appear, ensure 'Show Disabled Devices' is checked. If that still does not work, install a [custom loopback](https://vac.muzychenko.net/en/download.htm).
