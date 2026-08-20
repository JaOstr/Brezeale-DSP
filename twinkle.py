import numpy as np
import soundfile as sf # pip install pysoundfile

fs = 8000
t = np.arange(0, 0.5, 1/fs)

notes = np.array([52, 52, 59, 59 ,61, 61, 59, 59, 57, 57, 56, 56,
                  54, 54, 56, 52, 59, 59, 57, 57, 56, 56, 54, 54])

output = np.array([])

for n in notes:
    f = 440 * (2 **((n - 49) / 12))
    print(f"number = {n}, frequency = {f:.3f}")
    x = np.cos(2 * np.pi * f * t)
    output = np.concatenate((output, x))

sf.write("twinkle.wav", output, fs)

