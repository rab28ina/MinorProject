from django.db import models

class Teachers(models.Model):
    teacherId = models.IntegerField()
    teacherName = models.CharField(max_length=100)
    teacherPhone = models.CharField(max_length=10)
    teacherEmailId = models.EmailField(max_length=254)
    '''def __unicode__(self):
        return (self.teacherId, self.teacherName,self.teacherPhone,self.teacherEmailId)'''


