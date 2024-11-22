import os
import sys

# src 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = current_dir
sys.path.append(src_dir)

from PyQt5.QtWidgets import QApplication
from ui.timer_king import TimerKing
from core.data_manager import DataManager
from core.config import APP_NAME, BUNDLE_ID
import objc
from Foundation import NSBundle

def main():
    try:
        # 데이터 디렉토리 확인
        DataManager.ensure_data_directory()
        
        # 앱 실행
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        app.setApplicationName(APP_NAME)
        
        # macOS 앱 설정
        bundle = NSBundle.mainBundle()
        info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        if info:
            info['CFBundleName'] = APP_NAME
            info['CFBundleIdentifier'] = BUNDLE_ID
            info['LSUIElement'] = True  # dock 아이콘 숨기기
        
        timer_app = TimerKing()
        timer_app.show()
        
        sys.exit(app.exec_())
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == '__main__':
    main()