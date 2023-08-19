from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now as tznow
from django.db import models

@python_2_unicode_compatible
class QA(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    last_modified = models.DateTimeField(default=tznow, editable=False)

    class Meta:
        db_table = 'nano_faq_qa'

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        self.last_modified = tznow()
        super(QA, self).save(*args, **kwargs)
