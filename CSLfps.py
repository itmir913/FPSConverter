import threading
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom
import tkinter as tk
from tkinter import messagebox
import tkinterdnd2 as tkdnd2
import os
import webbrowser

# Program Info
AUTHOR = "운양고등학교 이종환T"
VERSION = "2024.11.04."


def process_file(file_path):
    try:
        df = pd.read_excel(file_path, dtype=str)
        fps = ET.Element('CSLfps', version="1.2", url="https://github.com/zhblue/freeproblemset/")
        generator = ET.SubElement(fps, 'generator', name="CSL", url="https://github.com/melongist/CSL/tree/master/HUSTOJ/")

        current_item = None
        for index, row in df.iterrows():
            if row['type'] == 'problem':
                current_item = ET.SubElement(fps, 'item')

                title = ET.SubElement(current_item, 'title')
                title.text = f"<![CDATA[{row['title']}]]>"

                time_limit = ET.SubElement(current_item, 'time_limit', unit="s")
                time_limit.text = f"<![CDATA[{row['time_limit']}]]>"

                memory_limit = ET.SubElement(current_item, 'memory_limit', unit="mb")
                memory_limit.text = f"<![CDATA[{row['memory_limit']}]]>"

                description = ET.SubElement(current_item, 'description')
                description.text = f"<![CDATA[{row['description']}]]>"

                input_data = ET.SubElement(current_item, 'input')
                input_data.text = f"<![CDATA[{row['input']}]]>"

                output_data = ET.SubElement(current_item, 'output')
                output_data.text = f"<![CDATA[{row['output']}]]>"

                sample_input = ET.SubElement(current_item, 'sample_input')
                sample_input.text = f"<![CDATA[{row['sample_input']}]]>"

                sample_output = ET.SubElement(current_item, 'sample_output')
                sample_output.text = f"<![CDATA[{row['sample_output']}]]>"

                hint = ET.SubElement(current_item, 'hint')
                hint.text = f"<![CDATA[{row['hint']}]]>"

                source = ET.SubElement(current_item, 'source')
                source.text = f"<![CDATA[{row['source']}]]>"

            elif row['type'] == 'test':
                test_input = ET.SubElement(current_item, 'test_input')
                test_input.text = f"<![CDATA[{row['template_input']}]]>"

                test_output = ET.SubElement(current_item, 'test_output')
                test_output.text = f"<![CDATA[{row['template_output']}]]>"

            elif row['type'] == 'template' and pd.notna(row['template_language']):
                template = ET.SubElement(current_item, 'template', language=row['template_language'])
                template.text = f"<![CDATA[{row['template_input']}]]>"

            elif row['type'] == 'solution' and pd.notna(row['template_language']):
                solution = ET.SubElement(current_item, 'solution', language=row['template_language'])
                solution.text = f"<![CDATA[{row['template_input']}]]>"

            elif row['type'] == 'prepend' and pd.notna(row['template_language']):
                prepend = ET.SubElement(current_item, 'prepend', language=row['template_language'])
                prepend.text = f"<![CDATA[{row['template_input']}]]>"

            elif row['type'] == 'append' and pd.notna(row['template_language']):
                append = ET.SubElement(current_item, 'append', language=row['template_language'])
                append.text = f"<![CDATA[{row['template_input']}]]>"

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_directory = os.path.dirname(file_path)
        output_file_name = os.path.join(output_directory, f"{base_name}_cslfps_output.xml")

        xml_str = ET.tostring(fps, encoding='utf-8', xml_declaration=True)
        formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
        formatted_xml = formatted_xml.replace("&lt;![CDATA[", "<![CDATA[").replace("]]&gt;", "]]>")

        with open(output_file_name, "w", encoding="utf-8") as fh:
            fh.write(formatted_xml)

        # 메인 쓰레드에서 메시지 박스를 호출
        root.after(0, lambda: messagebox.showinfo("Success", f"XML file generated successfully:\n{output_file_name}"))

    except Exception as e:
        # 메인 쓰레드에서 오류 메시지를 호출
        error_message = str(e)
        root.after(0, lambda: messagebox.showerror("Error", error_message))


def process_file_in_thread(file_path):
    # 새로운 쓰레드에서 파일을 처리
    thread = threading.Thread(target=process_file, args=(file_path,))
    thread.start()


def drop(event):
    file_path = event.data
    process_file_in_thread(file_path)  # 파일을 처리하는 함수를 쓰레드로 실행


def show_program_info():
    info_title = "프로그램 정보"
    info_message = (
        f"Made by: {AUTHOR}\n"
        f"Version: {VERSION}\n"
        "\n"
        "CSLFPS Converter 프로그램은 엑셀 파일로 작성된 온라인 저지 문제를 fps.xml 파일로 변환하는 프로그램입니다.\n"
        "\n"
        "이 프로그램은 LGPL-2.1 라이선스 하에 배포되며, 자유롭게 사용 및 수정할 수 있습니다."
    )
    messagebox.showinfo(info_title, info_message)


def open_github():
    webbrowser.open("https://github.com/itmir913/FPSConverter/releases")


# Create main window
root = tkdnd2.Tk()  # Changed to initialize TkinterDnD
root.title("Excel to CSLfps.xml Converter")
root.geometry("500x300")

label = tk.Label(root, text="Drag and drop your Excel file here", pady=100, padx=50)
label.pack(fill=tk.BOTH, expand=True)

# Enable drag-and-drop on the label
label.drop_target_register(tkdnd2.DND_FILES)
label.dnd_bind('<<Drop>>', drop)

# Create the menu bar
menubar = tk.Menu(root)
about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="Program Info", command=show_program_info)
about_menu.add_command(label="GitHub", command=open_github)
menubar.add_cascade(label="About", menu=about_menu)

# Add the menu bar to the main window
root.config(menu=menubar)

root.mainloop()
