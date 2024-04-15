import numpy as np
import json 
from openai import OpenAI
import requests
import os
from yt_dlp import YoutubeDL
import whisper
import tempfile
import time

def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
        'noplaylist': True,
        'outtmpl': tempfile.mktemp(suffix='.%(ext)s')  
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(video_url, download=True)
        return result['requested_downloads'][0]['filepath']  

def save_subtitles(subtitles, filename='subtitles.txt'):
    """Save subtitles to a text file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(subtitles)

def save_word_timings(timings, filename='word_timings.npy'):
    """Save word timings to a NumPy file."""
    np.save(filename, np.array(timings))

def transcribe_audio(audio_file_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)

    word_timing = []
    word_count = 0
    next_time_mark = 10  

    if 'segments' in result:
        for segment in result['segments']:
            start_time = segment['start']
            segment_word_count = len(segment['text'].split())
            word_count += segment_word_count
            
            while start_time >= next_time_mark:
                word_timing.append([next_time_mark, word_count])
                next_time_mark += 10

    return result["text"], word_timing

def garbage_collection(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return file_path

if __name__ == '__main__':
    start_time = time.time()
    yt_url = 'https://www.youtube.com/watch?v=QAAfDQx8DDQ'
    audio_file_path = download_audio(yt_url)
    try:
        subtitles, word_timings = transcribe_audio(audio_file_path)
        save_subtitles(subtitles)
        save_word_timings(word_timings)
    finally:
        garbage_collection(audio_file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))
