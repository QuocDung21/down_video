# import streamlit as st
# from pytubefix import YouTube
# from pytubefix.cli import on_progress
# from pytubefix import Playlist
# st.title('YouTube Video Downloader ')
# url = st.text_input('Enter YouTube URL:', '')
# download_type = st.selectbox('Select download type:', ['Video', 'MP3', 'Playlists'])
# if st.button('Download'):
#     if url:
#         try:
#             yt = YouTube(url, on_progress_callback=on_progress)
#             st.write(f"**Title:** {yt.title}")
#             if download_type == 'Video':
#                 ys = yt.streams.get_highest_resolution()
#                 # Start download
#                 ys.download()
#                 st.success('Video download complete!')
#             elif download_type == 'MP3':
#                 ys = yt.streams.filter(only_audio=True).first()
#                 ys = yt.streams.get_audio_only()
#                 ys.download(mp3=True)
#             elif download_type == 'Playlists':
#                 pl = Playlist(url)
#                 for video in pl.videos:
#                     ys = video.streams.get_audio_only()
#                     ys.download(mp3=True)
#         except Exception as e:
#             st.error(f'An error occurred: {e}')
#     else:
#         st.error('Please enter a valid YouTube URL.')


import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Playlist

st.title('Tool')
url = st.text_input('Enter YouTube URL:', 'https://www.youtube.com/watch?v=Y0Ojxw911s8')
path = st.text_input('Enter path:', 'C:/Users/quocdung/Downloads')
# download_type = st.selectbox('Select download type:', ['Video', 'MP3', 'Playlists'])
download_type = st.selectbox('Select download type:', ['Video', 'Mp3'])
# path = 'C:/Users/quocdung/Downloads'
if st.button('Tải'):
    if url:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            st.write(f"**Title:** {yt.title}")
            if download_type == 'Video':
                ys = yt.streams.get_highest_resolution()
                ys.download(path,filename='downloaded_video.mp4')
                # with open('downloaded_video.mp4', 'rb') as f:
                #     st.download_button('Download Video', f, file_name='downloaded_video.mp4')
                st.success('Down Video complete !')
            elif download_type == 'Mp3':
                ys = yt.streams.filter(only_audio=True).first()
                ys.download(path,filename='downloaded_audio.mp3')
                # with open('downloaded_audio.mp3', 'rb') as f:
                #     st.download_button('Download MP3', f, file_name='downloaded_audio.mp3')
                st.success('Down MP3 complete!')
            elif download_type == 'Playlists':
                pl = Playlist(url)
                for index, video in enumerate(pl.videos):
                    ys = video.streams.get_audio_only()
                    filename = f'downloaded_audio_{index}.mp3'
                    ys.download(filename=filename)
                    with open(filename, 'rb') as f:
                        st.download_button(f'Download MP3 - {video.title}', f, file_name=filename)
                st.success('Playlist download complete!')
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please enter a valid YouTube URL.')
