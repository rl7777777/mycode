#推送文件至阿里云oss
#pip install aliyun-python-sdk-oss2
import os
import shutil
import oss2

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'xxx')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'xxx')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'ewxxxz')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-accelerate.aliyuncs.com')


bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

for root, dirs, files in os.walk("dist", topdown=False):
    for name in files:
        fil=os.path.join(root, name)
        print fil
        with open(fil, 'rb') as fileobj:
            bucket.put_object(fil, fileobj)
