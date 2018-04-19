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

def try_write_videofile(output_video_path):
    try:
        print('ABOUT TO WRITE %d CLIPS to %s' % (len(clips), output_video_path))
        concat_clip.write_videofile(output_video_path, fps=24)
        print('successfully wrote %s' % output_video_path)
    except Exception as e:
        print('failed in writing %s with error %s' % (output_video_path, str(e)))


if len(sys.argv) > 1:
    data_root = sys.argv[1]
else:
    data_root = '/media'

print('* DATA ROOT = %s' % data_root)

media_files = get_media('%s/downloads' % data_root)

print(*media_files, sep='\n') #print('\n'.join(media_files))
print('--------------------------')

clips = []

for media_file in media_files:
    if is_image(media_file):
        print('Processing IMAGE file %s' % media_file)
        clips.append(moviepy.editor.ImageClip(media_file, duration=10).set_duration(10))
    elif is_audio(media_file):
        print('Skipping AUDIO file %s' % media_file)
        #audio_clip = AudioFileClip(media_file)
        #clips[-1].set_audio(audio_clip)
        ##clips.append(AudioFileClip(media_file))
    else:
        print('Skipping file %s' % media_file)

print('CLIPS COUNT = %d' % len(clips))
print('ABOUT TO CONCAT IMAGES')

output_video_ext = 'mp4'
output_video_path = '%s/uploads/bollyimages.%s' % (data_root, output_video_ext)
image_clips = moviepy.editor.ImageSequenceClip(media_files, fps=1)
image_clips.write_videofile(output_video_path, fps=1)

# 'compose' causing issue?
#concat_clip = moviepy.editor.concatenate_videoclips(clips, method='compose')
concat_clip = moviepy.editor.concatenate_videoclips(clips)

output_video_ext = 'mp4'
output_video_path = '%s/uploads/bolly.%s' % (data_root, output_video_ext)
try_write_videofile(output_video_path)

output_video_ext = 'mov'
output_video_path = '%s/uploads/bolly.%s' % (data_root, output_video_ext)
try_write_videofile(output_video_path)

output_video_ext = 'avi'
output_video_path = '%s/uploads/bolly.%s' % (data_root, output_video_ext)
try_write_videofile(output_video_path)

#concat_clip.write_videofile(output_video_path, fps=24, verbose=True, preset=ultrafast)


#   file_path=os.path.join(desktop,file)
#   video.write_videofile(file_path,
#                          verbose=True,
#                          codec="libx264",
#                          audio_codec='aac',
#                          temp_audiofile='temp-audio.m4a',
#                          remove_temp=True, 
#                          preset="medium",
#                          ffmpeg_params=["-profile:v","baseline", "-level","3.0","-pix_fmt", "yuv420p"])