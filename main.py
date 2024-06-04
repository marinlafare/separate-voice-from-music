import os
import ffmpeg
import string
from spleeter.separator import Separator

AUDIOS_URL = 'audio_files'

        
def separate_voice(audio_file, encoder, stems = 2):
    separator = Separator(f"spleeter:{stems}stems")
    separator.separate_to_file(audio_file,
                           'data/temp',
                           codec=encoder,
                           filename_format='{filename}/{instrument}.{codec}')
    
def clean_folders(audio_file, encoder):
    voice = f'data/temp/{audio_file[:-4]}/vocals.{encoder}'
    music = f'data/temp/{audio_file[:-4]}/accompaniment.{encoder}'
    os.rename(voice, f'data/voices/{audio_file[:-4]}_vocals.{encoder}')
    os.rename(music, f'data/music/{audio_file[:-4]}_music.{encoder}')
    os.rmdir(f'data/temp/{audio_file[:-4]}')
    
def clean_audio_files():
    for file in os.listdir(AUDIOS_URL):
            os.remove(os.path.join(AUDIOS_URL,file))

if __name__ == '__main__':
    
    encoder = input("1 for wav 2 for mp3 ::: ")
    if encoder == "1":
        encoder = "wav"
    elif encoder == "2":
        encoder = "mp3"
    songs = os.listdir(AUDIOS_URL)
    print('############')
    print('############')
    print('############')
    print('Songs to separate: ')
    print('############')
    for song in songs:
        print(song)
    print('############')
    print('############')
    print('############')
    
    
    for song in songs:
        song_dir = os.path.join(AUDIOS_URL,song)
        separate_voice(song_dir, encoder)
        clean_folders(song, encoder)
    clean_audio_files()
    print('############')
    print('Files ready')
    print('############')








