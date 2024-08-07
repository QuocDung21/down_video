import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Playlist
st.title('YouTube Video Downloader ')
url = st.text_input('Enter YouTube URL:', '')
download_type = st.selectbox('Select download type:', ['Video', 'MP3', 'Playlists'])
if st.button('Download'):
    if url:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            st.write(f"**Title:** {yt.title}")
            if download_type == 'Video':
                ys = yt.streams.get_highest_resolution()
                # Start download
                ys.download()
                st.success('Video download complete!')
            elif download_type == 'MP3':
                ys = yt.streams.filter(only_audio=True).first()
                ys = yt.streams.get_audio_only()
                ys.download(mp3=True)
            elif download_type == 'Playlists':
                pl = Playlist(url)
                for video in pl.videos:
                    ys = video.streams.get_audio_only()
                    ys.download(mp3=True)
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please enter a valid YouTube URL.')
