import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# class Poll(models.Model):
#     question = models.CharField(max_length=100)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now=True)

#     def  __str__(self):
#         return self.question


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    font_size = models.BigIntegerField()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, default=0, on_delete=models.CASCADE)
    # poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

# class Vote(models.Model):
#     choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
#     # poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
#     voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("poll", "voted_by")