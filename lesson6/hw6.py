import os
import shutil
import sys
import aioshutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from aiopath import AsyncPath
from asyncio import run, gather


FOLDERS = ["images", "documents", "audio", "video", "archives", "others"]

folder_ext_dict = {"images": ["JPEG", "PNG", "JPG", "SVG"],
                   "documents": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
                   "audio": ["MP3", "OGG", "WAV", "AMR"],
                   "video": ["AVI", "MP4", "MOV", "MKV"],
                   "archives": ["ZIP", "GZ", "TAR"],
                   "others": ["IPYNB"]}


def create_sorted_folders(cwd_path):

    for folder in FOLDERS:
        os.makedirs(f"{cwd_path}/{folder}", exist_ok=True)


def normalize(name):

    cyrillic = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    latin = ['a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i', 'yi', 'y', 'k', 'l', 'm',
             'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'yu', 'ya']

    name = "".join([x if x.isalnum() else "_" for x in name])

    mytable = {ord(cyr): lat for cyr, lat in zip(cyrillic, latin)}
    mytable.update({ord(cyr.upper()): lat.upper()
                   for cyr, lat in zip(cyrillic, latin)})

    result = name.translate(mytable)

    return result

files_path_list = []


async def files_handler(base_path, path):

        
        item_path = path
        item = str(path)
        folder_to_move = "others"


        file_name = item[item.rfind("\\"):item.rfind(".")]
        file_type = item.split(".")[-1]

        new_name = ".".join([normalize(file_name), file_type])

        for k, v in folder_ext_dict.items():

            if file_type.upper() in folder_ext_dict.get(k):
                folder_to_move = k
                break

        move_file_to_path = f"{base_path}/{folder_to_move}/{new_name}"

        if folder_to_move == "archives":
            await aioshutil.unpack_archive(str(item_path), move_file_to_path, file_type)
            os.remove(item_path)

        else:
            await aioshutil.move(item_path, move_file_to_path)
        return


async def main_move(base_path):

        items = files_path_list
        features = (files_handler(base_path, file) for file in items)

        await gather(*features)

def directories_handler(base_path, item):
    item_path = item

    dir_not_empty = next(item_path.iterdir(), None)

    if dir_not_empty:
        sort_docs(item_path, base_path)


def sort_docs(path, base_path=None):

    if not base_path:
        base_path = path
    directories = os.listdir(path)

    files_list = []
    directories_list = []

    def map_directories(item):
        item_path = f"{path}/{item}"
    
        nonlocal files_list
        nonlocal directories_list

        if os.path.isfile(item_path):
            files_path_list.append(Path(item_path).resolve())
            files_list.append(Path(item_path).resolve())
        elif os.path.isdir(item_path) and (item not in FOLDERS):
            directories_list.append(Path(item_path).resolve())

    with ThreadPoolExecutor() as executor:
        search = list(map(map_directories, list(directories)))    
    
    if directories_list:
        items = directories_list
        args = [(base_path, dir) for dir in items]
        
        with ThreadPoolExecutor() as executor:
            search = list(map(lambda x: directories_handler(*x), args))


def sort_folder(folder_path):

    try:
        create_sorted_folders(folder_path)
    except ValueError:
        "Please enter a correct path"

    sort_docs(folder_path)

    run(main_move(folder_path))

    for folder in os.listdir(folder_path):
        if folder not in FOLDERS:
            shutil.rmtree(f"{folder_path}/{folder}")


if __name__=="__main__":


    if len(sys.argv) > 1:

        create_sorted_folders(sys.argv[1])
        sort_folder(sys.argv[1])
    
    else:

        folder_path=input("Please enter the path: ")
        sort_folder(folder_path)
