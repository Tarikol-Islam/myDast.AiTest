from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserMessage(models.Model):
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name="Message Creator", on_delete=models.CASCADE)
    



    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("UserMessage_detail", kwargs={"pk": self.pk})
