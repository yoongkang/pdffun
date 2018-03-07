from django.db import models


def invoice_file(instance, filename):
    return f"mypdf_{instance.id}.pdf"


class Invoice(models.Model):
    document = models.FileField(upload_to=invoice_file)

    def __str__(self):
        return f'Invoice #{self.id}'
