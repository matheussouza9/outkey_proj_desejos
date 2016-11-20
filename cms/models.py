from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Desejo(models.Model):
    descricao = models.CharField(max_length = 1000)
    dono = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('cms:cms_show_desejo', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "ID %s - %s - %s" %(self.id, self.dono.username, self.descricao)
