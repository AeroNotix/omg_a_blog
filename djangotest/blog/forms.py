from django import forms as forms

choices = (
    ('general', 'General'),
    ('bug', 'Bug Report'),
    ('suggestion', 'suggestion')
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=choices)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)
    
cf=ContactForm()
