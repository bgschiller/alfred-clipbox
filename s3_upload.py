import sys
import os
import boto3
import random
import string
import datetime

s3 = boto3.client('s3')

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

bucket_name = os.getenv('AWS_S3_BUCKET')
url_prefix = os.getenv('URL_PREFIX')

if __name__ == '__main__':
    file_name = sys.argv[1]
    obj_key = random_key(file_name)
    s3.upload_file(file_name, bucket_name, obj_key, ExtraArgs={'ACL': 'public-read'})
    url = url_prefix + obj_key
    sys.stdout.write(url)
