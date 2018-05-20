from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    all_courses = Course.objects.all()
    print("*"*25)
    print('All Courses: ', all_courses)
    print("*"*25)
    context = {
        'courses' : all_courses
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    print("-"*25)
    print('Form Post: ', request.POST)
    print("-"*25)
    # pass the post data to the method we wrote and save the response in a variable called errors
    # errors = Course.objects.basic_validator(request.POST)
    #     # check if the errors object has anything in it
    # if len(errors):
    #     # if the errors object contains anything, loop through each key-value pair and make a flash message
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #         return redirect('/')
    #     else:
    #         # if the errors object is empty, that means there were no errors!
    #         # retrieve the blog to be updated, make the changes, and save
    #         course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    #         # blog = Blog.objects.get(id = id)
    #         # blog.name = request.POST['name']
    #         # blog.desc = request.POST['desc']
    #         # blog.save()
    #         print("#"*25)
    #         print('Course: ', course)
    #         print("#"*25)
    #
    #         print("*"*25)
    #         print('Success post: ', request.POST)
    #         print("*"*25)
    #         messages.success(request, "Course successfully added")
    #         return redirect('/', course)

    results = Course.objects.validator(request.POST)
    print("#"*20)
    print('Results: ', results)
    print("#"*20)
    if results[0]:
        return redirect('/')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)

    return redirect('/')

def to_remove(request, id):
    this_course = Course.objects.get(id=id)
    print("-"*25)
    print('Course to-remove OBJECT contains: ', this_course)

    context = {
        'course' : this_course
    }
    print("x"*25)
    print("Context contains: ", context)
# --- Pass our USER OBJECT in our context to our HTML view
    return render(request, 'courses/remove.html', context)

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/courses')
