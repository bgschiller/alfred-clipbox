from __future__ import print_function
import os
import sys
import random
import string
import datetime

def rewrite_name(fname):
    """
    Some names are common enough that they're not
    worth including as part of the url.
    *-capture.png should be rewritten as just *.png
    """
    return (fname
        .replace('-capture.png', '.png')
        .replace('-recording.mp4', '.mp4')
        .replace('-clip.txt', '.txt'))

alphabet = string.ascii_letters + string.digits
def random_key(filename):
    prefix = ''.join(random.choice(alphabet) for _ in range(7))
    head, tail = os.path.split(filename)
    date = str(datetime.datetime.now())[:10]
    return rewrite_name('{}-{}-{}'.format(prefix, date, tail))

url_prefix = os.getenv('URL_PREFIX')

if __name__ == '__main__':
    file_name = sys.argv[1]
    obj_key = random_key(file_name)
    url = url_prefix + obj_key
    print(file_name, obj_key, url)
