import os
import whisper
from pydub import AudioSegment
from tkinter import filedialog
from tkinter import *

def wrap_by_word(s, n):
    '''returns a string where \\n is inserted between every n words'''
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\\n'

    return ret

# Create a file dialog to select an MP3 file
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


# Load the MP3 file and convert it to a WAV file
try:
    sound = AudioSegment.from_mp3(file_path)
    sound.export("audio.wav", format="wav")

    # Initialize the speech recognizer
    model = whisper.load_model("base")

    # Use speech recognition to generate subtitles
    result = model.transcribe("audio.wav")

    # Format text
    text = wrap_by_word(result['text'], 10)

    # Save the subtitles to a text file
    with open("subtitles.txt", "w", encoding='utf-8') as file:
        file.write(result['text'])
        
    # Remove the temporary audio file
    os.remove("audio.wav")

except:
    print('Error')