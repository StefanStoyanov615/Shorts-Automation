import yt_dlp
import os
import re

# TikTok profile link (change this)
PROFILE_URL = "https://www.tiktok.com/@username"

# Optional: path to cookies file (set to None if not using cookies)
COOKIES_FILE = None  # Example: "cookies.txt"

# Extract username from TikTok link
match = re.search(r"@([a-zA-Z0-9_.]+)", PROFILE_URL)
username = match.group(1) if match else "unknown_user"

# Output folder: TikTok/<username>
output_dir = os.path.join("TikTok", username)
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
    ydl.download([PROFILE_URL])
