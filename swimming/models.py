from django.db import models


class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    head_coach = models. CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50)
    athletes = models.ManyToManyField('Athlete', null=True, blank=True)

    class Meta(object):
        ordering = ('name',)

    def __unicode__(self):
        return u'%s | %s' % (self.name, self.school)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Team, self).save(*args, **kwargs)


class Athlete(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    height = models.CharField(null=True, blank=True, max_length=20)
    year = models.CharField(max_length=20)
    hometown = models.CharField(max_length=100)
    photo = models.ImageField()
    gender = models.CharField(null=False, blank=False, max_length=50)

    def __unicode__(self):
        return u'%s' % (self.name)


class Schedule(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    results = models.CharField(max_length=100)
