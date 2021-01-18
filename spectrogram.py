import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt


music_file = 'output/ew.wav'
ipd.Audio(music_file)

scale, sr = librosa.load(music_file)

filter_banks = librosa.filters.mel(n_fft=2048, sr=22050, n_mels=10)
filter_banks.shape
plt.figure(figsize=(25, 10))
librosa.display.specshow(filter_banks,
                         sr=sr,
                         x_axis='linear')
plt.colorbar(format='%+2.f')
plt.show()

mel_spectrogram = librosa.feature.melspectrogram(scale, sr=sr, n_fft=2048, hop_length=512, n_mels=10)
mel_spectrogram.shape
log_mel_spectrogram = librosa.power_to_db(mel_spectrogram)
plt.figure(figsize=(25, 10))
librosa.display.specshow(log_mel_spectrogram,
                         x_axis='Time',
                         y_axis='mel',
                         sr=sr)
plt.colorbar(format='%+2.f')
plt.show()
