from django.db import models

# Create your models here.
class CommonCode(models.Model):
    common_code = models.CharField(max_length=2, blank=False, default='CC')
    upper_code = models.CharField(max_length=8,blank=False)
    lower_code= models.CharField(max_length=8, blank=False)

    class Meta :
        ordering = ['upper_code']

class CommonMenu(models.Model):
    common_code = models.CharField(max_length=2, blank=False, default='CM')
    upper_menu = models.CharField(max_length=8, blank=False)
    lower_menu = models.CharField(max_length=8, blank=False)

    class Meta :
        ordering = ['upper_menu']

class CCode(models.Model):
    common_code = models.CharField(max_length=2, blank=False, default='CC')
    upper_code = models.CharField(max_length=8,blank=False)
    lower_code= models.CharField(max_length=8, blank=False)

    class Meta :
        ordering = ['upper_code']


class CC2(models.Model):
        common_code = models.CharField(max_length=8, blank=False, default='', primary_key=True)
        parent_code = models.CharField(max_length=8, blank=True)
        name = models.CharField(max_length=50, blank=True)
        del_yn = models.CharField(max_length=1, blank=False, default='N')
        created_at = models.DateTimeField(auto_now_add=True)
        modified_at = models.DateTimeField(auto_now=True)
        created_user = models.CharField(max_length=11, default='')
        modified_user = models.CharField(max_length=11,default='')

        class Meta:
            ordering = ['common_code']