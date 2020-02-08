from zipfile import ZipFile
import os

os.chdir('Data')

# Test archive
with ZipFile('test.zip', 'w') as myzip:
    myzip.write('bank.csv', arcname='Bank.dat')


# Test extract
with ZipFile('test.zip', 'r') as myzip:
    myzip.extractall(path='.')

