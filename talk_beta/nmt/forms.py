from django import forms
from .models import Translate

class TranslateForm(forms.ModelForm):
    lang_src = forms.ChoiceField(choices=(('en', 'English'), ('fr', 'French'),),
                                 widget=forms.Select(attrs={'class':'btn-default'}), 
                                 required=True)
    lang_tgt = forms.ChoiceField(choices=(('en', 'English'), ('fr', 'French'),),
                                 widget=forms.Select(attrs={'class':'btn-default'}), 
                                 required=True)
    model_id = forms.ChoiceField(choices=((1, '1'), (2, '2'), (3, '3'),),
                                 widget=forms.Select(attrs={'class':'btn-default'}), 
                                 required=True)
    record_src = forms.CharField(label='Source sentence', 
                                 widget=forms.Textarea(attrs={'class':'form-control', 'rows': '16', 
                                                              'id': 'src-text', "style": "font-size: 16px"}), 
                                 required=True)
    record_tgt = forms.CharField(label='Target sentence', 
                                 widget=forms.Textarea(attrs={'class':'form-control', 'rows': '16', 
                                                              'id': 'tgt-text', "style": "font-size: 16px"}), 
                                 required=False)

    class Meta:
        model = Translate
        fields = ['lang_src', 'lang_tgt', 'model_id', 'record_src', 'record_tgt']