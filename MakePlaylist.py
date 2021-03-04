import os,sys,subprocess
file_path=os.path.abspath(os.getcwd());
list_dir=os.listdir(file_path)
with open('playlist.txt', 'w', encoding='utf-8') as playlist:
    for _file in list_dir:
        extention = _file.split('.')[-1]
        if extention == 'mp4':
            playlist.write(_file+'\n')
subprocess.run('mpv --playlist=playlist.txt', check=True, shell=True)
sys.exit()    



