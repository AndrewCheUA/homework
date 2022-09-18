import pathlib
import re
import shutil
import sys
import os

def main():
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()
    path = sys.argv[1]
    if not (os.path.exists(path) and Path(path).is_dir()):
        path('Path incorrect')
        exit()

    f_catalog = ["images", "video", "documents", "music", "archives"]

    def normalize(file):
        TRANS = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g',
            1043: 'G', 1076: 'd', 1044: 'D', 1077: 'e', 1045: 'E', 1105: 'e', 1025: 'E',
            1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z', 1080: 'i', 1048: 'I', 1081: 'j', 
            1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 1084: 'm', 1052: 'M', 
            1085: 'n', 1053: 'N', 1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 
            1056: 'R', 1089: 's', 1057: 'S', 1090: 't', 1058: 'T', 1091: 'u', 1059: 'U', 
            1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 
            1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH', 1097: 'sch', 1065: 'SCH', 
            1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: '', 1068: '', 1101: 'e', 
            1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'je', 
            1028: 'JE', 1110: 'i', 1030: 'I', 1111: 'ji', 1031: 'JI', 1169: 'g', 
            1168: 'G'}
        file_name = re.sub('\W', "'_'", file.name.rstrip(file.suffix).translate(TRANS)) + file.suffix
        return file_name

    def sort_funct(imported_main, file_obj):
        images = [".jpg", ".jpeg", ".png", ".svg"]
        video = [".avi", ".mp4", ".mov", "mkv"]
        documents = [".doc", "docx", ".txt", ".pdf", ".xlsx", ".pptx"]
        music = [".mp3", ".ogg", ".wav", ".amr"]
        archives = [".zip", ".gz", ".tar"]
        
        images_p = os.path.join(imported_main,"images")
        video_p = os.path.join(imported_main,"video")
        documents_p = os.path.join(imported_main,"documents")
        music_p = os.path.join(imported_main,"music")
        archives_p = os.path.join(imported_main,"archives")
        if str(file_obj.suffix) in images:
            pathlib.Path(images_p).mkdir(exist_ok=True)
            file_name = normalize(file_obj)
            file_obj.rename(os.path.join(images_p, file_name))
        
        elif str(file_obj.suffix) in video:
            pathlib.Path(video_p).mkdir(exist_ok=True)
            file_name = normalize(file_obj)
            file_obj.rename(os.path.join(video_p, file_name))
        
        elif str(file_obj.suffix) in documents:
            pathlib.Path(documents_p).mkdir(exist_ok=True)
            file_name = normalize(file_obj)
            file_obj.rename(os.path.join(documents_p, file_name))
        
        elif str(file_obj.suffix) in music:
            pathlib.Path(music_p).mkdir(exist_ok=True)
            file_name = normalize(file_obj)
            file_obj.rename(os.path.join(music_p, file_name))
        
        elif str(file_obj.suffix) in archives:
            pathlib.Path(archives_p).mkdir(exist_ok=True)
            arc_name = re.sub(str(file_obj.suffix),"",file_obj.name)
            shutil.unpack_archive(file_obj.name, archives_p / arc_name)
            file_obj.unlink()
        else:
            file_name = normalize(file_obj)
            file_obj.rename(os.path.join(imported_main, file_name))


    def sort_folders(folder):
        for item in folder.iterdir():
            if item.is_file():
                sort_funct(path, item)
            elif item.is_dir() and not any(item.iterdir()) and item.name not in f_catalog:
                    item.rmdir()
            elif item.is_dir() and any(item.iterdir()) and item.name not in f_catalog:
                sort_folders(item)
            
    def sort_main_folder(path):
        for file_obj in path.iterdir():
            if file_obj.is_dir() and file_obj.stat().st_size > 0 and file_obj.name not in f_catalog:
                sort_folders(file_obj)
            elif file_obj.is_file():
                sort_funct(path, file_obj)
            if file_obj.is_dir() and not any(file_obj.iterdir()) and file_obj.name not in f_catalog:
                file_obj.rmdir()



if __name__ == '__main__':
    exit(main())