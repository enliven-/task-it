from django.conf.urls.defaults import *

from collegecircles.swaps import views, models
from collegecircles.swaps.forms import *


urlpatterns = patterns('',
    # offer
    url(r'^offer/(?P<offer_id>\d+)/$', 'collegecircles.swaps.views.offer', name='offer'),
    
    # all offers
    url(r'^$', 'collegecircles.swaps.views.offers', name="offer_list_all"),
       
    # your offers
    url(r'^your_offers/$', 'collegecircles.swaps.views.your_offers', name='offer_list_yours'),
    
    # swap
    url(r'^swap/(?P<swap_id>\d+)/$', 'collegecircles.swaps.views.swap', name='swap'),
    
    # swaps proposed_to_you
    url(r'^proposed_to_you/$', 'collegecircles.swaps.views.proposed_to_you', name='proposed_to_you'),
    
    # swaps proposed_by_you
    url(r'^proposed_by_you/$', 'collegecircles.swaps.views.proposed_by_you', name='proposed_by_you'),
    
    # your accepted swaps
    # url(r'^accepted/$', 'collegecircles.swaps.views.accepted_swaps', name='accepted_swaps'),
    
    # your dead swaps
    url(r'^dead/$', 'collegecircles.swaps.views.dead_swaps', name='dead_swaps'),
    
    # new offer
    url(r'^new/$', 'collegecircles.swaps.views.new', name='offer_new'),
    
    # edit offer
    url(r'^edit/(?P<offer_id>\d+)/$', 'collegecircles.swaps.views.edit_offer', name='offer_edit'),
    
    # cancel offer
    url(r'^cancel/(?P<offer_id>\d+)/$', 'collegecircles.swaps.views.cancel_offer', name='offer_cancel'),
    
    # delete offer
    url(r'^delete/(?P<offer_id>\d+)/$', 'collegecircles.swaps.views.delete_offer', name='offer_delete'),
    
    # propose swap
    url(r'^proposal/(?P<offer_id>\d+)/$', 'collegecircles.swaps.views.propose_swap', name='propose_swap'),
    
    # accept swap
    # url(r'^accept/(?P<swap_id>\d+)/$', 'collegecircles.swaps.views.accept_swap', name='accept_swap'),
    
    # reject swap
    url(r'^reject/(?P<swap_id>\d+)/$', 'collegecircles.swaps.views.reject_swap', name='reject_swap'),
    
    # cancel swap
    url(r'^cancel/(?P<swap_id>\d+)/$', 'collegecircles.swaps.views.cancel_swap', name='cancel_swap'),

    # accept offer
    url(r'^accept/(?P<offer_id>\d+)/$', 'collegecircles.swaps.views.accept_offer', name='accept_offer'),

    # your accepted offers
    url(r'^accepted/$', 'collegecircles.swaps.views.accepted_offers', name='accepted_offers'),

    # ajax validation
    #(r'^validate/$', 'ajax_validation.views.validate', {'form_class': BlogForm, 'callback': lambda request, *args, **kwargs: {'user': request.user}}, 'blog_form_validate'),
)