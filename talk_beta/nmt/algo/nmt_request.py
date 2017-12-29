import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import spacy

class TranslateAPI:

    def __init__(self):
        self.nlp_en = spacy.load('en_core_web_sm', disable=['ner'])
        self.nlp_fr = spacy.load('fr_core_news_sm', disable=['ner'])

    def translate(self, lang_src, lang_tgt, model_id, text_src):

        if lang_src == 'en':
            lsent = self.nlp_en(text_src).sents
        elif lang_src == 'fr':
            lsent = self.nlp_fr(text_src).sents
        else:
            return 'internal error'
        
        lreq = []
        for sent in lsent:
            # lreq.append({'src': ' '.join([token.text for token in sent]), 'id': int(model_id)})
            lreq.append({'src': ' '.join([token.text for token in sent])})

        if lang_src == 'en' and lang_tgt == 'fr':
            api_port = '9201'
        elif lang_src == 'fr' and lang_tgt == 'en':
            api_port = '9202'
        else:
            return 'internal error'

        req_rest = Request('http://127.0.0.1:{}/translator/translate'.format(api_port))
        req_rest.add_header('Content-Type', 'application/json; charset=utf-8')
        djson = json.dumps(lreq).encode('utf-8')
        resp = urlopen(req_rest, djson)
        tgt = resp.read().decode('utf-8')
        return " ".join(([res[0]['tgt'] for res in json.loads(tgt)]))


