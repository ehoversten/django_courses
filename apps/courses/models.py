from __future__ import unicode_literals
from django.db import models
# import validatiors
from  django.core.validators import validate_email
from django.core.exceptions import ValidationError


def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# Create your models here.

class CourseManager(models.Manager):
    # def basic_validator(self, postData):
    # #create a DICT to hold our errors
    #     errors = {}
    #     if len(postData['name']) < 1:
    #         errors["name"] = "Name field cannot be empty"
    #     if len(postData['desc']) < 10:
    #         errors["desc"] = "Description should be at least 10 characters"
    #     return errors

    # form is the request.POST dictionary OBJECT
    def validator(self, form):
        #create a LIST to hold our errors
        errors = []
        if not form['name']:
            errors.append("Course Name is required")
        if not form['desc']:
            errors.append("Course Description is required.")

        if not errors:
            course = Course.objects.create(name=form['name'], desc=form['desc'])
            return (True, course)
        else:
            return (False, errors)



class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "<Course Object: {}| {}, {}>".format(self.id, self.name, self.desc)

    objects = CourseManager()
