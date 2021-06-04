import os
import shutil
import time

# temporary imported files

src_files = 'files'
for file in os.listdir(src_files):
    if 'jpg' in file:
        m_time = os.path.getmtime(os.path.join(src_files,file))
        real_time = time.localtime(m_time)
        dt = time.strftime("%Y-%m-%d", real_time)
        year,month,day = dt.split('-')
        if os.path.exists( os.path.join( 'newWorld_2','images',year) ):
            if os.path.exists( os.path.join('newWorld_2', 'images',year, month) ):
                shutil.copy(os.path.join(src_files,file),os.path.join('newWorld_2','images', year, month))
            else:
                os.makedirs(os.path.join('newWorld_2', 'images',year, month) )
                shutil.copy(os.path.join(src_files,file),os.path.join('newWorld_2','images', year, month))
        else:
            os.makedirs(os.path.join('newWorld_2','images', year, month))
            shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'images',year, month))

    elif 'mp4' in file:
        m_time = os.path.getmtime(os.path.join(src_files, file))
        real_time = time.localtime(m_time)
        dt = time.strftime("%Y-%m-%d", real_time)
        year, month, day = dt.split('-')
        if os.path.exists( os.path.join( 'newWorld_2','videos',year) ):
            if os.path.exists( os.path.join('newWorld_2', 'videos',year, month) ):
                shutil.copy(os.path.join(src_files,file),os.path.join('newWorld_2','videos', year, month))
            else:
                os.makedirs(os.path.join('newWorld_2', 'videos',year, month) )
                shutil.copy(os.path.join(src_files,file),os.path.join('newWorld_2','videos', year, month))
        else:
            os.makedirs(os.path.join('newWorld_2','videos', year, month))
            shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'videos',year, month))



