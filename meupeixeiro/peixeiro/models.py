from django.db import models
from django.contrib.auth.models import User


class UserPeixeiro(models.Model):
    """
    This class implements a default system user.
    """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    cnpj = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


    @staticmethod
    def create(kargs):
        user = UserPeixeiro()
        print kargs
        user_admin = User.objects.create_user(kargs['username'], kargs['email'],
                                                   kargs['password'])
        user.name = kargs['name']
        if 'rg' in kargs:
            user.rg = kargs['rg']
        if 'cpf' in kargs:
            user.cpf = kargs['cpf']
        if 'cnpj' in kargs:
            user.cnpj = kargs['cnpj']
        user.address = kargs['address']
        user.phone = kargs['phone']
        user.user = user_admin
        user.save()
