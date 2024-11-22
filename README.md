# Mac Time Tracker (맥 타임좌)

A macOS application for tracking app usage time, built with Python and PyQt5.

## Project Structure

```
timer/
├── src/
│   ├── core/          # Core functionality
│   │   ├── config.py
│   │   ├── data_manager.py
│   │   └── status_bar.py
│   ├── ui/            # User Interface
│   │   ├── widgets/
│   │   │   ├── app_tracking.py
│   │   │   ├── home_widget.py
│   │   │   └── timer_widget.py
│   │   └── timer_setting.py
│   └── main.py
└── README.md
```

## Features

- Track app usage time
- Display status in macOS menu bar
- Timer functionality
- Modern and minimalist UI

## Requirements

- Python 3.x
- PyQt5
- AppKit
- Cocoa
- objc

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ksbelphegor/Mac_Timetracker.git
cd Mac_Timetracker
```

2. Install dependencies:
```bash
pip install PyQt5 pyobjc-framework-Cocoa
```

## Usage

Run the application:
```bash
python src/main.py
```

## Development

The project is organized into several modules:

- `core/`: Contains core functionality
  - `config.py`: Configuration settings
  - `data_manager.py`: Data handling and persistence
  - `status_bar.py`: macOS status bar integration

- `ui/`: User interface components
  - `widgets/`: Individual UI widgets
  - `timer_setting.py`: Timer configuration

## License

MIT License
