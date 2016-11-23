from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Desejo(models.Model):
    descricao = models.CharField(max_length=1000)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('api:api_retrieve_update_destroy_desejo', kwargs={'pk': self.pk})
        #return reverse('cms:cms_show_desejo', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "#%s | Dono: %s | Descricao: %s" %(self.id, self.dono.username, self.descricao)
