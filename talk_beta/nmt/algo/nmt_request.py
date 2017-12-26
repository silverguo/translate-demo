import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from nltk.tokenize import sent_tokenize

__all__ = ['translate_api_request']

# rest api for translate
def translate_api_request(src):

    req_rest = Request('http://127.0.0.1:9001/translator/translate')
    req_rest.add_header('Content-Type', 'application/json; charset=utf-8')
    sent_list = [{'src': sentence.strip()} for sentence in sent_tokenize(src)]
    djson = json.dumps(sent_list).encode('utf-8')
    resp = urlopen(req_rest, djson)
    tgt = resp.read().decode('utf-8')
    return " ".join(([res[0]['tgt'] for res in json.loads(tgt)]))
