from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    summary_description = models.TextField()
    skype = models.CharField(max_length=64)
    phone = models.CharField(max_length=64, blank=True, default=None)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Language(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return '{}'.format(self.name)

LANG_LEVEL_CHOICES = (
    ('b', 'Basic'),
    ('pi', 'Pre-intermediate'),
    ('i', 'Intermediate'),
    ('a', 'Advanced'),
)


class EmployeeLanguage(models.Model):
    employee = models.ForeignKey(Employee)
    language = models.ForeignKey(Language)

    level = models.CharField(max_length=2, choices=LANG_LEVEL_CHOICES)

    class Meta:
        db_table = 'employee_language'
        unique_together = ('employee', 'language',)

    def __str__(self):
        return '{} {}'.format(self.employee.last_name, self.language.name)


class Education(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'education'

    def __str__(self):
        return '{}'.format(self.name)


class EmployeeEducation(models.Model):
    employee = models.ForeignKey(Employee)
    education = models.ForeignKey(Education)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'employee_education'
        unique_together = ('employee', 'education',)

    def __str__(self):
        return '{} {}'.format(self.employee.last_name, self.education.name)