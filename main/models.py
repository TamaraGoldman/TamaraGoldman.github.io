from django.db import models


class Feedback(models.Model):
    feedback = models.TextField('Отзыв')
    pub_date = models.DateTimeField('date published')

    
    def __str__(self):
        return self.feedback
