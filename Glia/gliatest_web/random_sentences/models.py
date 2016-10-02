from django.db import models


class sentence(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content
