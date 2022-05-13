from django.db import models


class Message(models.Model):
	full_name = models.CharField(max_length=240, null=False, blank=False)
	email = models.EmailField(null=True, blank=True)
	phone_number = models.PositiveIntegerField(blank=False, null=False)
	branch = models.CharField(max_length=56, blank=False, null=False)
	message_query = models.TextField(blank=False, null=False)
	received_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.full_name} - {self.received_at}'


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)