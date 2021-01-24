import os
import sys
import pathlib


music = []
imgs = []
docs = []


def recursive(path):
    if path.is_dir():
        print(f"Folder's name: {path}---> {os.listdir(path)}")
        for i in os.listdir(path):
            if i == files:
                sorting(files)
    
        for fold in path.iterdir():      
            recursive(fold)
            
            
def sorting():
   
    audio_fileformat = ('MP3', 'OGG', 'WAV', 'AMR')
    img_fileformat = ('JPEG', 'PNG', 'JPG')
    docs_fileformat = ('DOC', 'DOCX', 'TXT')

    audio_fileformat = [(elem.lower()) for elem in audio_fileformat]
    img_fileformat = [(elem.lower()) for elem in img_fileformat]
    docs_fileformat = [(elem.lower()) for elem in docs_fileformat]
    my_files = files.copy()
    my_files = [(z.lower()) for z in my_files]

    for i in range(len(my_files)):
        if my_files[i].split('.')[-1] in audio_fileformat:
            music.append(files[i])
        elif my_files[i].split('.')[-1] in img_fileformat:
            imgs.append(files[i])
        elif my_files[i].split('.')[-1] in docs_fileformat:
            docs.append(files[i])

    
    print(f"music: {music}")
    print(f"images: {imgs}")
    print(f"documents: {docs}") 


def main():
    global files
    path = sys.argv[1]
    path = pathlib.Path(path)
    files = os.listdir(path)
    recursive(path)
    sorting()
    print(f"Base directory {path}")
    
if __name__ in "__main__":
    main()    
