from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userena.models import UserenaLanguageBaseProfile

from userena.models import upload_to_mugshot
from userena.utils import get_gravatar
from userena import settings as userena_settings


from collegecircles.tribes.models import Tribe
import userena
import datetime

class Profile(UserenaLanguageBaseProfile):
    """ Default profile """
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )


    GRAVATAR_CHOICES = (
        ('mm', _('mm')),
        ('identicon', _('identicon')),
        ('monsterid', _('monsterid')),
        ('wavatar', _('wavatar')),

    )


    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile') 

    gender = models.PositiveSmallIntegerField(_('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)
    website = models.URLField(_('website'), blank=True, verify_exists=True)
    location =  models.CharField(_('location'), max_length=255, blank=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    about_me = models.TextField(_('about me'), blank=True)

    gravatar_choice = models.CharField(_('gravatar'), default='monsterid', choices=GRAVATAR_CHOICES, max_length=20, blank=True, null=True)


    @property
    def age(self):
        if not self.birth_date: return False
        else:
            today = datetime.date.today()
            # Raised when birth date is February 29 and the current year is not a
            # leap year.
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)
            if birthday > today: return today.year - self.birth_date.year - 1
            else: return today.year - self.birth_date.year



    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        userena_settings.USERENA_MUGSHOT_DEFAULT = 'monsterid'
        open_circle = None
        try:
            open_circle = Tribe.objects.get(name='0pen/Default')
            print "open circle, ", open_circle
        except:
            pass
        
        open_circle.members.add(self.user)
        print "i joined ", Tribe.objects.filter(members=self.user)


    def get_circles(self):
        return Tribe.objects.filter(members=self.user)