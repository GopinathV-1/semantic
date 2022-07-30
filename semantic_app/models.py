from django.db import models

class DrugSales(models.Model):

    DRUG_CHOICES = (
        ('M', 'Musculo-Skeletal System Drugs'),
        ('N', 'Nervous System Drugs'),
        ('R', 'Respiratory System Drugs'),
    )
    name = models.CharField(max_length=35, blank=False, null=False)
    drug_type = models.CharField(choices=DRUG_CHOICES, blank=False, null=False)
    day = models.PositiveSmallIntegerField(blank=False, null=False)
    month = models.PositiveSmallIntegerField(blank=False, null=False)
    year = models.PositiveSmallIntegerField(blank=False, null=False)
    sales = models.PositiveIntegerField(blank=False, null=False)


class DrugReview(models.Model):

    DRUG_CHOICES = (
        (10, 'Melatonin'),
        (20, 'Rituximab'),
        (30, 'Disulfiram'),
        (40, 'Erlotinib'),
        (50, 'Pazopanib'),
        (60, 'Eribulin'),
    )
    name = models.PositiveSmallIntegerField(choices=DRUG_CHOICES, blank=False, null=False)
    condition = models.CharField(blank=False, null=False)
    review = models.CharField(blank=True, null=True)
    date = models.DateField(blank=False, null=False)
    year = models.PositiveSmallIntegerField(blank=False, null=False)
    rating = models.PositiveSmallIntegerField(blank=False, null=False)
    useful_count = models.PositiveSmallIntegerField(blank=False, null=False)
