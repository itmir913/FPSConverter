# FPSConverter

![2024-11-04 135359](https://github.com/user-attachments/assets/fe7c8709-5400-461f-8bcf-b37f5bc9e704)

## 개요
FPS Converter 프로그램은 엑셀 파일로 작성된 온라인 저지 문제를 freeproblemset.xml 파일로 변환하는 Python 기반 GUI 프로그램입니다.

## FPS
Free Problem Set 프로젝트는 ACM/ICPC 대회 문제를 저장하고 공유하기 위한 표준 XML 형식을 제공합니다.  
이 오픈 소스 프로젝트는 온라인 저지 간 문제 교환을 용이하게 하며, HUSTOJ와 같은 다양한 시스템을 지원합니다.  
참고: [https://github.com/zhblue/freeproblemset](https://github.com/zhblue/freeproblemset)

## 사용 방법
1. 프로그램을 실행합니다.
2. Excel 파일을 드래그 앤 드롭합니다.

## 엑셀파일 양식
변환 가능한 엑셀 파일 양식은 [your_excel_file.xlsx](https://github.com/itmir913/FPSConverter/blob/main/your_excel_file.xlsx) 파일을 참고하세요.

## 빌드 방법
PyInstaller를 사용하여 프로그램을 빌드할 수 있습니다.  
  
아래 명령어를 사용하세요:  

```bash
pyinstaller -F -w fps.py --additional-hooks-dir=.
```
