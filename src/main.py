import os
import sys

# src 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = current_dir
sys.path.append(src_dir)

from PyQt5.QtWidgets import QApplication
from ui.timer_setting import TimeTracker
from core.data_manager import DataManager

def main():
    try:
        # 데이터 디렉토리 확인
        DataManager.ensure_data_directory()
        
        # 앱 실행
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        
        tracker = TimeTracker()
        tracker.show()
        
        sys.exit(app.exec_())
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == '__main__':
    main()