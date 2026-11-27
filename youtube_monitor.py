import yt_dlp
import logging

CHANNEL_URL = "https://www.youtube.com/@houseofrepresentativesnepa7440/live"

def get_live():
    options = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "noplaylist": True,
        "format": "best",
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(CHANNEL_URL, download=False)

        if not info:
            return None

        if info.get("is_live") is not True:
            return None

        return {
            "title": info.get("title", ""),
            "video_url": info.get("url", ""),
            "video_id": info.get("id", ""),
        }

    except Exception as error:
        logging.warning("YouTube Live check failed: %s", error)
        return None


if __name__ == "__main__":
    live = get_live()

    if live:
        print("LIVE DETECTED")
        print("Title:", live["title"])
        print("Video ID:", live["video_id"])
    else:
        print("No active live stream.")
