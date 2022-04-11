import wave
import struct
import math

def generate_audio(f, duration, sample_rate, freq, volume):
  try:
    #duration is in ms
    if volume is None: volume = 10
    if sample_rate is None: sample_rate = 44100.0
    if duration is None: duration = 1000
    if int(duration) > 10000: duration = 10000
    if freq is None: freq = 440

    volume, sample_rate, duration, freq = int(volume), int(sample_rate), int(duration), int(freq)

    audio = []
    num_samples = duration * (sample_rate/1000.0)
    for x in range(int(num_samples)):
      audio.append((volume/10) * math.sin(2*math.pi*freq* (x/sample_rate)))
    print("audio appended")

    wav_file = wave.open(f, "w")
    num_channels = 1
    sample_width = 2

    num_frames = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((num_channels, sample_width, sample_rate, num_frames, comptype, compname))

    for sample in audio:
      wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))
    
    return
  except Exception as e:
    print(e)
    generate_audio(f, 1000, 44100, 440, 10)

if __name__ == "__main__":
  pass