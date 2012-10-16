from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from profiles.forms import SignupFormExtra

from django.contrib import admin
admin.autodiscover()

from userena.contrib.umessages import views as messages_views

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Demo Override the signup form with our own, which includes a
    # first and last name.
    # (r'^accounts/signup/$',
    #  'userena.views.signup',
    #  {'signup_form': SignupFormExtra}),

    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^$',
        direct_to_template,
        {'template': 'static/promo.html'},
        name='promo'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tribes/', include('collegecircles.tribes.urls')),
    (r'^swaps/', include('collegecircles.swaps.urls')),
    url(r'^feedback/$', messages_views.message_compose, {'recipients': 'viksit+Karansyal', 'template_name': 'feedback.html' }, name='feedback'),
    url(r'^feedback/history/$', messages_views.message_list, {'template_name': 'feedback_history.html' }, name='history')

)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

