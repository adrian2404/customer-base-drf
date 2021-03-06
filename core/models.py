from django.db import models

# Create your models here.

class Profession(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class DataSheet(models.Model):
    description = models.CharField(max_length=100)
    historical_data = models.TextField()

    def __str__(self):
        return self.description


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    professions = models.ManyToManyField(Profession)
    data_sheet = models.OneToOneField(DataSheet, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    doc_num = models.CharField(max_length=12, unique=True, null=True, blank=True)

    @property
    def status_string(self):
        if self.active:
            return 'Customer is active'
        else:
            return 'Customer is not active'

    def num_professions(self):
        return self.professions.all().count()

    def __str__(self):
        return self.name

class Document(models.Model):
    PP = 'PP'
    ID = 'ID'
    OT = 'OT'

    DOC_TYPES = (
        (PP, 'Passport'),
        (ID, 'Identity card'),
        (OT, 'Others'),
    )
    dtype = models.CharField(choices=DOC_TYPES, max_length=2)
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return '{} for {}'.format(self.doc_number, self.customer.name)
