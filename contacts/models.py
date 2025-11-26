from django.db import models

class Contact(models.Model):
    full_name = models.CharField("ПІБ", max_length=100)
    phone_number = models.CharField("Номер телефону", max_length=20)
    email = models.EmailField("E-mail", blank=True, null=True)
    note = models.TextField("Примітка", blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} – {self.phone_number}"
