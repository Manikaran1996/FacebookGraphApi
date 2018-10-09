import facebook
import requests
# from PIL import Image
import json


def get_images(_id='https://www.facebook.com/ABC-Co-228455837861421/'):
    token = 'EAAeFIxIo0v8BAKZCenufDXxu1ge5lfregcuuRRDZBmYWITbKRXYQKgjZBY3jApYNk14sVo1R74JF6M9shJwgZAxohrEMSs1IOqDpSRdcaLkcZAjkr0g5RTD7G5IRyCUkgb2tyZAietlrXloCHidH3RwgX4ZCn5CC3AKDYRM7MfKkn0V7TCxRxqZCAlCE6aZAtSmgZDC'
    graph = facebook.GraphAPI(access_token=token)
    res = graph.get_connections(connection_name='photos', id=_id, type='uploaded', fields='link')
    url = 'https://graph.facebook.com/v3.1/photos?id='+ _id +'&type=uploaded&fields=tags,id,link&access_token=' + token
    res = json.loads(requests.get(url).text)
    images = []
    for photo in res['data']:
        image = dict()
        image['id'] = photo['id']
        image['link'] = photo['link']
        image['url'] = 'https://graph.facebook.com/{}/picture?width=200&height=200'.format(photo['id'])
        try:
            image['tags'] = photo['tags']['data']
        except KeyError:
            image['tags'] = None
        # img = requests.get(url.format(photo['id'])).content
        # image = Image.open(io.BytesIO(img))
        images.append(image)
    return images
