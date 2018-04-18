import os
import glob
import moviepy.editor 
#from moviepy.editor import *

source_dir = '/media/downloads/'
output_dir = '/media/uploads/'

def is_image(file_name):
    image_extensions = ('.png', '.jpg')
    return file_name.endswith(image_extensions)

def is_audio(file_name):
    audio_extensions = ('.mp3')
    return file_name.endswith(audio_extensions)

def get_media():
    "get list of media files in order based on file creation time"
    files = glob.glob('/media/downloads/*.png')
    files.extend(glob.glob('/media/downloads/*.jpg'))
    files.extend(glob.glob('/media/downloads/*.mp3'))
    files.sort(key=os.path.getmtime)
    return files


media_files = get_media()

print(*media_files, sep='\n') #print('\n'.join(media_files))
print(os.getcwd())
print('--------------------------')

clips = list()

for media_file in media_files:
    if is_image(media_file):
        print('Processing IMAGE file %s' % media_file)
        clips.append(moviepy.editor.ImageClip(media_file, duration=2))
    elif is_audio(media_file):
        print('Skipping AUDIO file %s' % media_file)
        #audio_clip = AudioFileClip(media_file)
        #clips[-1].set_audio(audio_clip)
        ##clips.append(AudioFileClip(media_file))
    else:
        print('Skipping file %s' % media_file)

print('ABOUT TO CONCAT IMAGES')
concat_clip = moviepy.editor.concatenate_videoclips(clips, method='compose')

print('ABOUT TO WRITE CLIPS')
concat_clip.write_videofile('/media/uploads/bolly.mp4', fps=24)

