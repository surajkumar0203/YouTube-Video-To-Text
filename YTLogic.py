from pytubefix import YouTube
import os
import re
from pytube.exceptions import VideoUnavailable


def videoToText(url):
    try:
        yt = YouTube(url)
        subtitles = yt.captions
        if subtitles:
            for subtitle in subtitles:
                caption = yt.captions[subtitle.code]
                caption.save_captions(f"temp-sk_{subtitle.code}.txt")
        else:
            return {"error":"No Subtitles"}
    except VideoUnavailable:
        return {"error":"The video is unavailable."}
    except Exception as e:
        print(e)
        return {'error':'Check Your URL or Internet'}

    directory=os.listdir()
    fileNames=[file for file in directory if file.startswith("temp-")]

    
    text = []
    for fileName in fileNames:
        with open(fileName,"r") as rb:
            lines=rb.readlines()
        cleaned_lines = []
        for line in lines:
            if re.match(r'^\d+\s*$', line):
                continue
            if re.match(r'^\d{2}:\d{2}:\d{2},\d{3}', line):
                continue
            
            cleaned_lines.append(line.strip())

        text.append(cleaned_lines)

        output_fileName = "".join(fileName.split("-")[1:]).replace('.txt','')
        os.remove(fileName)

    return text
       