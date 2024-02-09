from pathlib import Path
from colorama import Fore
import colorama
import sys
colorama.init(autoreset=True)
def get_all_files_and_directories(directory_path, level=1):
    path = Path(directory_path)
    #Creating empty list for future directories and file catalog
    all_items = []
    try:
        for item in path.iterdir():
            #Creating vocabulary item where name = file or directory name, level = level of object nesting, type = d is directory, f is file 
            item_info = {'name': item.name, 'level': level, 'type': 'f' if item.is_file() else 'd'}
            all_items.append(item_info)
            if item.is_dir():
                #Recursively get all files and folders
                all_items.extend(get_all_files_and_directories(item, level + 1))
    #Handling cases with directory errors
    except Exception as e:
        print(Fore.RED + f"Directory error: {e}")
        return sys.exit()
    return all_items

#Handling cases when command line argunent missed
if len(sys.argv) < 2:
    print(Fore.RED + "Command line argument error - directory path not provided")
    sys.exit()

directory_path = sys.argv[1]
all_items_list = get_all_files_and_directories(directory_path)

print(Fore.CYAN + "\U0001F5C1 ",Path(directory_path).name)
for item in all_items_list:
    if item['type'] == 'd':
        print(Fore.CYAN + f"{'.' * (item['level']) * 3}\U0001F5C1  {item['name']}")
    else:
        print(Fore.GREEN + f"{'.' * (item['level']) * 3}\U0001F5B9 {item['name']}")