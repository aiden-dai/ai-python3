import os

# List all the files and dirs

pwd = os.getcwd()
print(pwd)

# os.chdir('..')
# pwd = os.getcwd()
# print(pwd)

# os.listdir, os.mkdir, os.rmdir,
for file in os.listdir(pwd):
    # print(file)
    print('{} is directory {}'.format(
        file, os.path.isdir(os.path.join(pwd, file))))


# os.remove(path) delete file
# os.rename(src, dst) Rename the file or directory src to dst

if os.path.exists('test.txt'):
    print('file exists')
    os.rename('test.txt', 'test1.txt')
    os.remove('test1.txt')
    # os.remove(os.path.join(os.getcwd(), 'test1.txt'))
