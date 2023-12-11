from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(blank=True,primary_key=True)
    d_name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.d_name


class Emp(models.Model):
    emp_no=models.IntegerField(blank=True,unique=2,primary_key=True)
    e_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField(blank=True)
    hire_date=models.DateField()
    sal=models.IntegerField(blank=True)
    comm=models.IntegerField(blank=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.e_name