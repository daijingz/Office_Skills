import os
import shutil
import time

# temporary imported files
def copy_func(src_files,file,type_file):
    m_time = os.path.getmtime(os.path.join(src_files, file))
    real_time = time.localtime(m_time)
    dt = time.strftime("%Y-%m-%d", real_time)
    year, month, day = dt.split('-')
    if os.path.exists(os.path.join('newWorld_2', type_file, year)):
        if os.path.exists(os.path.join('newWorld_2', type_file, year, month)):
            shutil.move(os.path.join(src_files, file), os.path.join('newWorld_2', type_file, year, month))
        else:
            os.makedirs(os.path.join('newWorld_2', type_file, year, month))
            shutil.move(os.path.join(src_files, file), os.path.join('newWorld_2', type_file, year, month))
    else:
        os.makedirs(os.path.join('newWorld_2', type_file, year, month))
        shutil.move(os.path.join(src_files, file), os.path.join('newWorld_2', type_file, year, month))


src_files = 'files'
for file in os.listdir(src_files):
    if 'jpg' in file:
        copy_func(src_files,file,'images')

    elif 'mp4' in file:
        copy_func(src_files, file, 'videos')



