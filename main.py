import os
import re
from pathlib import Path
from pytube import YouTube

def setup():
    Path("downloads").mkdir(exist_ok=True)
    
def get_format_menu():
    print("====FORMATO_DE_AUDIO====")
    print("1) MP3")
    print("2) AAC")
    print("3) FLAC")
    return input("Elige una opción: ")
    
def get_video_format_menu():
    print("====FORMATO_DE_VIDEO====")
    print("1) MP4")
    print("2) AVI")
    print("3) MKV")
    return input("Elige una opción: ")
    
def get_link():
    return input("====LINK====\nCopia y pega la URL: ")
    
def download_audio(link, format_option):
    try:
        yt = YouTube(link)
        print(f"Descargando {yt.title}")
        if format_option == '1':
            yt.streams.filter(only_audio=True, file_extension='mp4').first().download(output_path="downloads")
        elif format_option == '2':
            yt.streams.filter(only_audio=True, file_extension='aac').first().download(output_path="downloads")
        elif format_option == '3':
            yt.streams.filter(only_audio=True, file_extension='flac').first().download(output_path="downloads")
        else:
            print("Opción no válida.")
    except Exception as e:
        print(f"Error descargando {link}: {e}")
        
def download_video(link, format_option):
    try:
        yt = YouTube(link)
        print(f"Descargando {yt.title}")
        if format_option == '1': 
            yt.streams.filter(file_extension='mp4').first().download(output_path="downloads")
        elif format_option == '2':           
            yt.streams.filter(file_extension='avi').first().download(output_path="downloads")
        elif format_option == '3':            
            yt.streams.filter(file_extension='mkv').first().download(output_path="downloads")
        else:
            print("Opción no válida.")
    
    except Exception as e:
        print(f"Error descargando {link}: {e}")
        
def main():
    while True:
        print("====MENU_PRINCIPAL====")
        print("1) Descargar audio")
        print("2) Descargar video")
        print("3) Salir")
        option = input("Elige una opción: ")
        
        if option == '1':
            audio_format_option = get_format_menu()
            link = get_link()
            download_audio(link, audio_format_option)
        
        elif option == '2':
            video_format_option = get_video_format_menu()
            link = get_link()
            download_video(link, video_format_option)
        
        elif option == '3':
            break
        
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    setup()
    main()
