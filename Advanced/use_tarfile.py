import tarfile
import os

os.chdir('Data')

# Test extract
tar = tarfile.open('news20.tar.gz')
tar.extractall()
tar.close()


"""
import shutil

def extract_all(archives, extract_path):
    for filename in archives:
        shutil.unpack_archive(filename, extract_path)


extract_all('news20.tar.gz', '.')

"""