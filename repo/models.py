from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=128, help_text="title of the document")
    content = models.TextField(blank=True, help_text="content of the docuemnt")
    created_time = models.DateTimeField(auto_now_add= True)
    updated_time = models.DateTimeField(auto_now= True)
    created_by = models.ForeignKey(User, help_text="Document created by", on_delete=models.PROTECT, related_name="docs_created")
    updated_by = models.ForeignKey(User, null=True, help_text="Document last updated by", on_delete=models.PROTECT, related_name="docs_last_updated")


class Questionnaire(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_time = models.DateTimeField(auto_now_add= True)
    updated_time = models.DateTimeField(auto_now= True)
    created_by = models.ForeignKey(User, help_text="Questionnaire created by", on_delete=models.PROTECT, related_name="quests_created")
    updated_by = models.ForeignKey(User, null=True, help_text="Questionnaire last updated by", on_delete=models.PROTECT, related_name="quests_last_updated_by")
