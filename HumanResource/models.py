from django.db import models

# Create your models here.

from Utils.utils import *


class GenderFiledChoice(models.IntegerChoices):
    MALE = 0, "男"
    FEMALE = 1, "女"
    UNKNOWN = 2, "其他"


class GenderField(models.IntegerField):
    def __init__(self, verbose_name="性别", *args, **kwargs):
        super().__init__(choices=GenderFiledChoice.choices, default=GenderFiledChoice.UNKNOWN,
                         verbose_name=verbose_name, *args, **kwargs)


class Human(BaseModel):
    name = models.CharField(max_length=50, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = GenderField()
