import yt_dlp
import datetime
from .downloader import download
from django.shortcuts import render

def check_ytb_url(url):
    res = url
    if "youtu.be" in url:
        video_id = url.split('/')[-1]
        url = f"https://www.youtube.com/watch?v={video_id}"
    elif "shorts" in url:
        video_id = url.rstrip('/').split('/')[-1]
        url = f"https://www.youtube.com/watch?v={video_id}"
    return url

def format_duration(seconds):
    return "Unknown" if seconds is None else str(datetime.timedelta(seconds=seconds))

def home(request):
    v_url = request.GET.get('q', '').strip()
    v_info = {}
    video_info = {}

    if v_url:
        v_url = check_ytb_url(v_url)

        try:
            ydl_opts = {
                'quiet': True,
                'skip_download': True,
                'force_generic_extractor': True,
                'extract_flat': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(v_url, download=False)

            v_info = {
                'title': info.get('title'),
                'author': info.get('uploader'),
                'views': info.get('view_count'),
                'length': format_duration(info.get('duration')),
                'thumbnail_url': info.get('thumbnail'),
            }

            download(v_url)

        except Exception as e:
            v_info = {'error': f"Failed to fetch: {str(e)}"}
    else:
        v_info = {'error': "URL not valid."}

    return render(request, 'home.html', {
        'video_url': v_url,
        'video_info': v_info,
    })