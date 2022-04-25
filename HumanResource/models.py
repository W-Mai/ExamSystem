from django.db import models

# Create your models here.

from Utils.utils import *


class GenderFiledChoice(models.IntegerChoices):
    MALE = 0, "男"
    FEMALE = 1, "女"
    UNKNOWN = 2, "其他"


class GenderField(models.IntegerField):
    def __init__(self, choices=GenderFiledChoice.choices, verbose_name="性别", default=GenderFiledChoice.UNKNOWN, *args,
                 **kwargs):
        super().__init__(choices=choices, default=default,
                         verbose_name=verbose_name, *args, **kwargs)


class Human(BaseModel):
    name = models.CharField(max_length=50, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = GenderField()

    department = models.ForeignKey('Department', verbose_name="部门", on_delete=models.DO_NOTHING)
    attendance_status = models.ForeignKey('AttendanceStatus', verbose_name="考勤状态", on_delete=models.DO_NOTHING)


class Department(BaseModel):
    name = models.CharField(max_length=50, verbose_name="部门名称")


class AttendanceStatus(BaseModel):
    name = models.CharField(max_length=50, verbose_name="考勤状态")
