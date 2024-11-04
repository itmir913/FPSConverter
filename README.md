# FPSConverter

![2024-11-04 135359](https://github.com/user-attachments/assets/fe7c8709-5400-461f-8bcf-b37f5bc9e704)

## 개요
FPS Converter 프로그램은 엑셀 파일로 작성된 온라인 저지 문제를 fps.xml 파일로 변환하는 Python 기반 GUI 프로그램입니다.

## 사용 방법
1. 프로그램을 실행합니다.
2. Excel 파일을 드래그 앤 드롭합니다.

## 빌드 방법
PyInstaller를 사용하여 프로그램을 빌드할 수 있습니다.  
  
아래 명령어를 사용하세요:  

```bash
pyinstaller -F -w fps.py --additional-hooks-dir=.
```
