import os

# YouTube official channel
YOUTUBE_CHANNEL = "https://www.youtube.com/@houseofrepresentativesnepa7440"

# Facebook Page credentials (GitHub Secrets बाट आउने)
FB_PAGE_ID = os.getenv("FB_PAGE_ID", "")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")

# Video settings
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

# Monitoring
CHECK_INTERVAL = 30
RECONNECT_DELAY = 10

# Branding
LOGO_PATH = "assets/logo.png"

# Headlines
TICKER_BACKGROUND = "#10264A"
TICKER_TEXT_COLOR = "#FFFFFF"
TICKER_SPEED = 180
