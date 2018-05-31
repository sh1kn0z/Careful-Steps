import zipfile
import rarfile
import magic
import sys

path = '/home/sh1kn0z/Downloads/archives/unzipme.'
count = 0

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
