#!/usr/bin/env python
# coding=utf-8
# Author: bostin.wang
# Mail: bostinwangbo@gmail.com
# Created Time: 2017-02-09 11:15:50

import sys
import wave
import pyaudio

RECORD_SECONDS = int(sys.argv[1])

# wave configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print('recording')

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print('done recording')

stream.stop_stream()
stream.close()
p.terminate()

# write down
wf = wave.open('output.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

