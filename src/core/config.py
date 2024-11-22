import os

# 앱 기본 설정
APP_NAME = "맥 타임좌"
BUNDLE_ID = "com.mactimeja.app"

# 데이터 저장 설정
DATA_DIR = os.path.join(os.path.expanduser('~'), '.mactimeja')
APP_USAGE_FILE = os.path.join(DATA_DIR, 'app_usage.json')
TIMER_DATA_FILE = os.path.join(DATA_DIR, 'timer_data.json')

# 캐시 설정
APP_CACHE_LIFETIME = 2.0  # 초
APP_LIST_UPDATE_INTERVAL = 10000  # 밀리초
TIME_UPDATE_INTERVAL = 1000  # 밀리초

# UI 설정
STATUS_BAR_WIDTH = 90
STATUS_BAR_HEIGHT = 22
ICON_SIZE = 22
