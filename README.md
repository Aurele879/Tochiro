# Tochiro

![Logo](assets/icon_mini.png)

A lightweight desktop wrapper for Google Gemini built with Python and [pywebview](https://pywebview.flowrl.com/).

##  ⚙️ Features

- **Native Window:** Runs Gemini in a standalone, resizable $1280 \times 720$ desktop window.
- **Session Persistence:** Saves login sessions, cookies, and cache locally (`gemini_profile/`) so you stay signed in.
- **Custom Branding:** Supports custom application icons via `assets/icon.ico`.

## 💻 Prerequisites

- Python 3.8+
- `pywebview` library

Install the dependency:

```bash
pip install pywebview
```

> **Note:** On Windows, `pywebview` relies on Microsoft Edge WebView2. On Linux, ensure `pygobject` and `webkit2gtk` (or Qt) packages are installed.

## 📋 Project Structure

```text
.
├── main.pyw
├── assets/
│   └── icon.ico
└── gemini_profile/      # Created automatically on first run
```

## 🤖 Usage

Run the application:

```bash
python main.pyw
```
