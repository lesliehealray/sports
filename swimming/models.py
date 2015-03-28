from django.db import models


class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    head_coach = models. CharField(max_length=50)
    school = models.CharField(max_length=50)
    schedule = models.CharField(max_length=100)
    gender = models.CharField(unique=False, max_length=20)
    athletes = models.ManyToManyField('Athlete')

    class Meta(object):
        verbose_name_plural = 'Teams'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s | %s' % (self.name, self.school)


def save(self, *args, **kwargs):
    self.name = self.name.upper()
    super(Team, self).save(*args, **kwargs)


class Athlete(models.Model):
    name = models.CharField(unique=False, max_length=50)
    position = models.CharField(unique=False, max_length=20)
    height = models.CharField(unique=True, max_length=20)
    year = models.CharField(unique=False, max_length=20)
    hometown = models.CharField(unique=True, max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.name)
