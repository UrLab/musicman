import json
import yt_dlp

class Downloader:

    def __init__(self, prefered_format="opus", out_path: str="."):
        self.prefered_format = prefered_format
        self.out_path = out_path
        
    def download(self, url: str, codec="opus", path="./audio", max_size="128"):
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

    def get_info(self, url):

        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False) 

        print("Title:", info.get('title'))
        print("Uploader:", info.get('uploader'))
        print("Upload date:", info.get('upload_date'))
        print("View count:", info.get('view_count'))
        print("Description:", info.get('description'))

# If you want to try without the web interface
if __name__ == "__main__":
    pass
    dld = Downloader()
    dld.download("https://www.youtube.com/watch?v=Ktv5dIBlvQ8")
