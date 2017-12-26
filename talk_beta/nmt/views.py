from django.shortcuts import render

from .forms import TranslateForm

# Create your views here.

def nmt(request):

    if request.method == 'POST':
        tform = TranslateForm(request.POST)
        if tform.is_valid():
            text_src = tform.cleaned_data['record_src']
            tform = TranslateForm({'lang_src': tform.cleaned_data['lang_src'], 
                                    'lang_tgt': tform.cleaned_data['lang_tgt'], 
                                    'record_src': text_src, 
                                    'record_tgt': text_src})

            return render(request, 'nmt/nmt.html', {'form': tform})

        else:
            print(tform.errors)
    
    return render(request, 'nmt/nmt.html', {'form': TranslateForm({'record_src': 'Hello world!'})})

