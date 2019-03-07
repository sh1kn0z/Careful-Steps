# first extract the main zip file to get 'archives' folder

import zipfile
import rarfile
import magic
import sys

path = '/path_to_directory/unzipme.'

i = 0

while True:
    filename = path + str(i)
    filetype = magic.from_file(filename, mime=True)
    if filetype.endswith('x-rar'):
        unzipme = rarfile.RarFile(filename)
    elif filetype.endswith('zip'):
        unzipme = zipfile.ZipFile(filename)

    char = unzipme.comment.split(",")[0]

    sys.stdout.write(char)
    sys.stdout.flush()

    i = i + int(unzipme.comment.split(",")[1])

    if int(unzipme.comment.split(",")[1]) == 0:
        break
