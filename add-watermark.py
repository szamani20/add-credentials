import os

PATH = 'path/to/Java/files'
RIGHT = '''/*
Created and maintained by Soroush Zamani
2019
Department of Computing and Software
McMaster University
 */'''


def append_to_front(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        # Remove the trailing whitespaces and append your content with a leading newline
        f.write(RIGHT.rstrip('\r\n') + '\n' + content)


for root, subdirs, files in os.walk(PATH):
    for file in files:
        if file.endswith('.java'):
            append_to_front(os.path.join(root, file))
