import os
import pprint as pp

music_directory = '/Users/dustinglassmoyer/Documents/old Music'
files = []
checksum_tuples = []
checksum_dict = {}

def find_file_type(directory, extension):
    global files
    for sub in os.listdir(directory):
        path = os.path.join(directory, sub)
        if has_extension(path, extension):
            files.append(path)
        elif os.path.isdir(path):
            find_file_type(path, extension)
        else:
            continue
    return files

def has_extension(path, extension):
    if path[-len(extension):].lower() == extension:
        return True
    else:
        return False

def get_checksum(path):
    command = "md5 '%s'" % path
    pipe = os.popen(command)
    md5sum = pipe.read()
    status = pipe.close()
    try:
        return (md5sum.split(' = ')[1], path)
    except:
        return None

def checksum_dict(tuples):
    global checksum_dict
    for t in tuples:
        print t
        if type(t) == tuple:
            for k, v in t:
                if k in checksum_dict.keys():
                    checksum_dict[k] = v
                else:
                    checksum_dict[k].append(v)
    return checksum_dict

files = find_file_type(music_directory, '.mp3')

for file in files[:100]:
    checksum_tuples.append(get_checksum(file))

pp.pprint(checksum_dict(checksum_tuples))