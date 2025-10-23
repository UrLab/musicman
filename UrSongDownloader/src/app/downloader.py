import json
import yt_dlp
import os



def download(url: str, codec="opus", path="./music", max_size="128"):
    ydl_opts = {
        'format': f'bestaudio[abr<={max_size}]',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '0',
        }],
        'quiet': False,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename

    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

# If you want to try without the web interface
if __name__ == "__main__":
    pass
    #dld = Downloader()
    #dld.download("https://www.youtube.com/watch?v=Ktv5dIBlvQ8")
