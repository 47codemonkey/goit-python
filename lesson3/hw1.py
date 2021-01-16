import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.

files = os.listdir(path)


music = []
imgs = []
docs = []


audio_fileformat = ('MP3', 'OGG', 'WAV', 'AMR')
img_fileformat = ('JPEG', 'PNG', 'JPG')
docs_fileformat = ('DOC', 'DOCX', 'TXT')


audio_fileformat = [(elem.lower()) for elem in audio_fileformat]
img_fileformat = [(elem.lower()) for elem in img_fileformat]
docs_fileformat = [(elem.lower()) for elem in docs_fileformat]

   
for file in files:  
    if file.rsplit('.')[-1] in audio_fileformat:
        music.append(file)
    elif file.rsplit('.')[-1] in img_fileformat:
        imgs.append(file)   
    elif file.rsplit('.')[-1] in docs_fileformat:
        docs.append(file)
        
  
print(f"music: {music}")
print(f"images: {imgs}")
print(f"documents: {docs}") 
        
  