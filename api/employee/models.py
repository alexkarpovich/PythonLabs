from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    summary_description = models.TextField()
    skype = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Language(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class EmployeeLanguage(models.Model):
    employee = models.ForeignKey(Employee)
    language = models.ForeignKey(Language)
    lang_level = (
        ('b', 'Basic'),
        ('pi', 'Pre-intermediate'),
        ('i', 'Intermediate'),
        ('a', 'Advanced'),
    )
    level = models.CharField(max_length=2, choices=lang_level)

    class Meta:
        db_table = 'employee_language'
        unique_together = ('employee', 'language',)

    def __str__(self):
        return self.employee.last_name + ' ' + self.language.name