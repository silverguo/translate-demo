from django.shortcuts import render

from .forms import TranslateForm

from .algo.nmt_request import TranslateAPI

translate_api = TranslateAPI()

# Create your views here.

def nmt(request):

    if request.method == 'POST':
        tform = TranslateForm(request.POST)
        if tform.is_valid():
            text_src = tform.cleaned_data['record_src']
            lang_src = tform.cleaned_data['lang_src']
            lang_tgt = tform.cleaned_data['lang_tgt']
            model_id = tform.cleaned_data['model_id']


            # translate
            text_tgt = translate_api.translate(lang_src, lang_tgt, 
                                               model_id, text_src)

            tform = TranslateForm({'lang_src': lang_src, 
                                   'lang_tgt': lang_tgt, 
                                   'model_id': model_id,  
                                   'record_src': text_src, 
                                   'record_tgt': text_tgt})

            return render(request, 'nmt/nmt.html', {'form': tform})

        else:
            print(tform.errors)
    
    return render(request, 'nmt/nmt.html', {'form': TranslateForm({'lang_src': 'en', 
                                                                   'lang_tgt': 'fr', 
                                                                   'model_id': 1})})

