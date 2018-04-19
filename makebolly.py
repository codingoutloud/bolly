import os
import sys
import glob
import moviepy.editor 


def is_image(file_name):
    image_extensions = ('.png', '.jpg')
    return file_name.endswith(image_extensions)

def is_audio(file_name):
    audio_extensions = ('.mp3')
    return file_name.endswith(audio_extensions)

def get_media(downloads):
    "get list of media files in order based on file creation time"
    files = glob.glob('%s/*.png' % downloads)
    files.extend(glob.glob('%s/*.jpg' % downloads))
    files.extend(glob.glob('%s/*.mp3' % downloads))
    files.sort(key=os.path.getmtime)
    return files


if len(sys.argv) > 1:
    data_root = sys.argv[1]
else:
    data_root = '/media'

print('* DATA ROOT = %s' % data_root)

media_files = get_media('%s/downloads' % data_root)

print(*media_files, sep='\n') #print('\n'.join(media_files))
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
print('CLIPS COUNT = %d' % len(clips))

#concat_clip = moviepy.editor.concatenate_videoclips(clips, method='compose')
concat_clip = moviepy.editor.concatenate_videoclips(clips)

print('ABOUT TO WRITE %d CLIPS' % len(clips))
output_video_path = '%s/uploads/bolly.mp4' % data_root
concat_clip.write_videofile(output_video_path, fps=24)

