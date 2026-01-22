import yt_dlp
import json

URL = "https://www.youtube.com/watch?v=RWJPrgYJT5M"

ydl_opts = {"proxy": "socks5://127.0.0.1:12334"}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)
    print(json.dumps(ydl.sanitize_info(info)))
