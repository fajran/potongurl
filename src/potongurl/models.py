from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from potongurl import utils

class Link(models.Model):
    user = models.ForeignKey(User, null=True, default=None)
    hash = models.CharField(max_length=10, unique=True,
                            null=True, default=None)
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def save(self):
        models.Model.save(self)
        self.hash = utils.get_hash(self.id)
        models.Model.save(self)

    def new_url(self):
        if self.hash is None:
            return None

        site = Site.objects.get_current()
        return 'http://%s/%s' % (site.domain, self.hash)

    def url_excerpt(self):
        if len(self.url) < 50:
            return self.url
        else:
            return '%s...' % self.url[:47]

