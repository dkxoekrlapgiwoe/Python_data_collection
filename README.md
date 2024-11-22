# 맥 타임좌 (Mac Time Tracker)

맥 타임좌는 macOS용 앱 사용 시간 추적 애플리케이션입니다.

## 디렉토리 구조

```
timer/
├── src/               # 소스 코드
│   ├── core/         # 핵심 기능
│   │   ├── config.py         # 설정
│   │   ├── data_manager.py   # 데이터 관리
│   │   └── status_bar.py     # 상태바 컨트롤러
│   ├── ui/           # 사용자 인터페이스
│   │   ├── widgets/          # UI 위젯
│   │   │   ├── app_tracking.py   # 앱 추적 위젯
│   │   │   ├── home_widget.py    # 홈 화면 위젯
│   │   │   └── timer_widget.py   # 타이머 위젯
│   │   └── timer_setting.py  # 타이머 설정
│   └── main.py       # 메인 실행 파일
└── README.md         # 프로젝트 문서
```

## 요구사항

- Python 3.x
- PyQt5
- AppKit
- Cocoa
- objc

## 실행 방법

```bash
python src/main.py
```
