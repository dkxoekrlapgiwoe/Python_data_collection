import json
import os
from core.config import DATA_DIR, APP_USAGE_FILE, TIMER_DATA_FILE

class DataManager:
    @staticmethod
    def ensure_data_directory():
        """데이터 저장 디렉토리가 존재하는지 확인하고 없으면 생성합니다."""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

    @staticmethod
    def load_app_usage():
        """앱 사용 데이터를 로드합니다."""
        try:
            if os.path.exists(APP_USAGE_FILE):
                with open(APP_USAGE_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"앱 사용 데이터 로드 중 오류 발생: {e}")
        return {}

    @staticmethod
    def save_app_usage(data):
        """앱 사용 데이터를 저장합니다."""
        try:
            DataManager.ensure_data_directory()
            with open(APP_USAGE_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"앱 사용 데이터 저장 중 오류 발생: {e}")

    @staticmethod
    def load_timer_data():
        """타이머 데이터를 로드합니다."""
        try:
            if os.path.exists(TIMER_DATA_FILE):
                with open(TIMER_DATA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"타이머 데이터 로드 중 오류 발생: {e}")
        return {
            'app_name': None,
            'start_time': None,
            'total_time': 0,
            'windows': {},
            'current_window': None
        }

    @staticmethod
    def save_timer_data(data):
        """타이머 데이터를 저장합니다."""
        try:
            DataManager.ensure_data_directory()
            with open(TIMER_DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"타이머 데이터 저장 중 오류 발생: {e}")
