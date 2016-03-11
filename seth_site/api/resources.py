from flask_restful import Resource, abort, reqparse
from bs4 import BeautifulSoup
import requests

parser = reqparse.RequestParser()
parser.add_argument('url')

def parse_description(soup):
    desc = ''
    for meta in soup.findAll('meta'):
        if 'description' == meta.get('name', '').lower():
            desc = meta['content']
    return desc

class LinkPreview(Resource):
    def get(self):
        args = parser.parse_args()
        url = args['url']
        try:
            r = requests.get(url)
        except:
            return abort(404)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html5lib')
            title = soup.title.string
            description = parse_description(soup)
            return {
                'title': title.strip(),
                'description': description.strip(),
                'url': url
            }
        else:
            return abort(404)
