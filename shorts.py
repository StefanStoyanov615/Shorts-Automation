import yt_dlp
import os
import re

# YouTube channel link (change this)
CHANNEL_URL = "https://www.youtube.com/@griffinsshorts"

# Optional: path to cookies file (set to None if not using cookies)
COOKIES_FILE = None  # Example: "cookies.txt"

# Ensure we only grab Shorts
if not CHANNEL_URL.rstrip("/").endswith("/shorts"):
    if not CHANNEL_URL.rstrip("/").endswith("/videos"):
        CHANNEL_URL = CHANNEL_URL.rstrip("/") + "/shorts"
    else:
        CHANNEL_URL = CHANNEL_URL.replace("/videos", "/shorts")

# Extract channel name
match = re.search(r"@([a-zA-Z0-9_.-]+)", CHANNEL_URL)
channel_name = match.group(1) if match else "unknown_channel"

# Output folder: YouTube/<channel_name>
output_dir = os.path.join("YouTube", channel_name)
os.makedirs(output_dir, exist_ok=True)

ydl_opts = {
    "format": "best",
    "outtmpl": os.path.join(output_dir, "%(upload_date)s - %(title)s.%(ext)s"),
    "merge_output_format": "mp4",
    "noplaylist": False,
    "ignoreerrors": True,
    "cookiefile": COOKIES_FILE,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([CHANNEL_URL])
