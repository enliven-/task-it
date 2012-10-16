from datetime import datetime
from django import forms

from collegecircles.swaps.models import Offer, Swap

from collegecircles.tribes.models import Tribe

from django.db.models import Q

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        exclude = ('offerer', 'state', 'offered_time', 'swapped_by', 'acceptor', 'acceptors')


    def __init__(self, user, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['circles'].widget.attrs = {'class': 'select_choice'}
        self.fields['circles'].queryset = Tribe.objects.filter(members=user)
        self.fields['circles'].help_text = "Hold control/cmd to multiple select circles you want to post this in."
        self.fields['circles'].error_messages['required'] = "You have to select atleast one circle. Chose '!Open/Default!' to make it visible to everyone."



class ProposeSwapForm(forms.ModelForm):
    
    class Meta:
        model = Swap
        fields = ('proposing_offer',)
        
        
#    def __init__(self, user=None, *args, **kwargs):
#        if user:
#            self.fields['responding_offer'].queryset = Offer.objects.filter(offerer=user)
#        super(ProposeSwapForm, self).__init__(*args, **kwargs)




class ProposingOfferForm(forms.ModelForm):
    
    class Meta:
        model = Offer
        fields = ('short_description', 'offering',)
        