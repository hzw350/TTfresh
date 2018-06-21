# coding=utf-8
from django.db import models


# 用户表
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=50)
    uphone = models.CharField(max_length=11,default='',blank=True)
    uaddress = models.CharField(max_length=100,default='',blank=True)
    ucode = models.CharField(max_length=6,default='',blank=True)

    class Meta():
        db_table = 'UserInfo'


# 用户收货地址的表
class ReceiverInfo(models.Model):
    rname = models.CharField(max_length=20)
    raddress = models.CharField(max_length=20)
    rcode = models.CharField(max_length=6)
    rphone = models.CharField(max_length=11)
    ruser = models.ForeignKey('UserInfo')

    class Meta():
        db_table = 'ReceiverInfo'
