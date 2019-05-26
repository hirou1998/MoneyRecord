from _datetime import datetime

from django.db import models


class HumanName(models.Model):
    class Meta:
        db_table = "human_name"

    human_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.human_name


class Category(models.Model):
    class Meta:
        db_table = "category"

    category = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.category


class List(models.Model):
    class Meta:
        db_table = "list"

    choices = (
        ("Borrow", "Borrow"),
        ("Lend", "Lend"),
        ("Done", "Done"),
    )

    state = models.CharField(verbose_name="state", choices=choices, max_length=20)
    date = models.DateField(verbose_name="Date", default=datetime.now)
    human_name = models.ForeignKey(HumanName, on_delete=models.PROTECT, verbose_name="Name")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    money = models.IntegerField(verbose_name="Amount", help_text="Currency = JPY")
    memo = models.CharField(max_length=500, verbose_name="Memo")
    deadline = models.DateField(verbose_name="Deadline", default=None, blank=True, null=True)

    def __str__(self):
        return self.memo