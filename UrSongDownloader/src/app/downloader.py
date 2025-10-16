import json
import yt_dlp


def download(url: str, codec="opus", path="./audio", max_size="128"):
    ydl_opts = {
        'format': f'bestaudio[abr<={max_size}]',
        'outmpl': '%(title)s.%(ext)s',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': f'{codec}',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)

# If you want to try without the web interface
if __name__ == "__main__":
    pass
    #dld = Downloader()
    #dld.download("https://www.youtube.com/watch?v=Ktv5dIBlvQ8")
