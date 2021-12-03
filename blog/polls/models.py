from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(_('question text'), max_length=200)
    pub_date = models.DateTimeField(_('date published'))

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, 
                                  verbose_name="question")
    choice_text = models.CharField(_("choice_text"), max_length=200)
    votes = models.IntegerField(_("votes"), default=0)

    class Meta:
        verbose_name = "choice"
        verbose_name_plural = "choices"

    def __str__(self):
        return self.choice_text