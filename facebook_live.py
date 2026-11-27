import os
import requests
import logging

PAGE_ID = os.getenv("FB_PAGE_ID", "")
PAGE_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")
GRAPH_VERSION = os.getenv("GRAPH_API_VERSION", "v23.0")

BASE_URL = f"https://graph.facebook.com/{GRAPH_VERSION}"


def start_facebook_live(title):
    if not PAGE_ID or not PAGE_TOKEN:
        raise RuntimeError("Facebook Page ID or Access Token missing.")

    url = f"{BASE_URL}/{PAGE_ID}/live_videos"

    payload = {
        "title": title,
        "description": title,
        "status": "LIVE",
        "access_token": PAGE_TOKEN
    }

    response = requests.post(url, data=payload, timeout=30)

    if not response.ok:
        raise RuntimeError(
            f"Facebook Live creation failed: {response.text}"
        )

    data = response.json()

    stream_url = data.get("secure_stream_url") or data.get("stream_url")

    if not data.get("id") or not stream_url:
        raise RuntimeError(
            f"Facebook did not return the required stream details: {data}"
        )

    logging.info("Facebook Live session created: %s", data["id"])

    return {
        "live_id": data["id"],
        "stream_url": stream_url
    }


def stop_facebook_live(live_id):
    url = f"{BASE_URL}/{live_id}"

    response = requests.post(
        url,
        data={
            "end_live_video": "true",
            "access_token": PAGE_TOKEN
        },
        timeout=30
    )

    if not response.ok:
        raise RuntimeError(
            f"Could not end Facebook Live: {response.text}"
        )

    logging.info("Facebook Live ended: %s", live_id)
    return response.json()
