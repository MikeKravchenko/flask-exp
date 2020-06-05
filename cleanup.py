import os
from sightline.simon.data import Bucket
from sightline.simon.instance import login
from sightline.simon.module import Module


def clear_simon():
    if not os.environ.get('SIMON_V1_DOMAIN'):
        raise ValueError('SIMON_V1_DOMAIN must be set')
    if not os.environ.get('SIMON_V1_CLIENT_ID'):
        os.environ['SIMON_V1_CLIENT_ID'] = 'simon'
    if not os.environ.get('SIMON_V1_REFRESH_TOKEN'):
        os.environ['SIMON_V1_REFRESH_TOKEN'] = login('root', 'root')['refresh_token']

    for mod in Module.list():
        mod.unload()
        Module.remove(mod.id)

    for bucket in Bucket.list():
        bucket.delete()

if __name__ == "__main__":
    clear_simon()