import os
import shutil

GLOBAL_PATH = ''

folders = ['images', 'documents', 'audios']

imgs = ['.jpg', '.png', '.jpeg']
docs= ['.pdf', '.docx', '.txt', '.xlsx']
music = ['.mp3', '.ogg', '.wav', '.amr']


def normalize(string):

    t_dict = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
                  ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
                  ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ю'): 'yu',
                  ord('я'): 'ya', ord('ы'): 'y', ord('э'): 'e', ord('ё'): 'yo', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
                  ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y', ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M',
                  ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh', ord('Ц'): 'Ts',
                  ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ю'): 'Yu', ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Э'): 'E', ord('Ё'): 'Yo'}

    string_x = []

    normalized = ''

    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            string_x.append(c)
        else:
            c = c.translate(t_dict)
            string_x.append(c)

    return normalized.join(string_x)


def create_folder():

    for name in folders:
        directory = os.path.join(GLOBAL_PATH, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)


def transfer_file(files_info):

    create_folder()
    info = files_info.split(";")
    src = os.path.join(info[1], info[2]+info[3])
    dest = os.path.join(GLOBAL_PATH, info[0], normalize(info[2])+info[3])

    if info[0] == 'archives':
        shutil.unpack_archive(shutil.move(src, dest),
                              os.path.join(GLOBAL_PATH, info[0]))
        os.remove(dest)
    else:
        shutil.move(src, dest)
    try:
        os.rmdir(info[1])
    except OSError:
        pass


def distribute_file(collection, path, nesting):

    for file in collection:
        file_name, file_extension = os.path.splitext(file)
        if file_extension in imgs:
            transfer_file(f'images;{path};{file_name};{file_extension}')
        elif file_extension in docs:
            transfer_file(f'documents;{path};{file_name};{file_extension}')
        elif file_extension in music:
            transfer_file(f'audios;{path};{file_name};{file_extension}')


def catch_path(path, nesting=0):

    collection = []

    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            catch_path(os.path.join(path, file), nesting + 1)
        else:
            collection.append(file)

    distribute_file(collection, path, nesting)


def main():

    global GLOBAL_PATH
    GLOBAL_PATH = r'C:/Users/user/Desktop/Experimental/'
    catch_path(r'C:/Users/user/Desktop/Experimental/')


if __name__ == '__main__':
    main()