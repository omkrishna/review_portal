from django.shortcuts import render, redirect
from .models import Course, Professor, Review
from .forms import CreateReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
	courses = Course.objects.all()[:5]
	professors = Professor.objects.all()[:5]
	reviews = Review.objects.all()[:3]
	context = {
		'courses' : courses,
		'professors' : professors,
		'reviews' : reviews,
	}
	return render(request,'review/home.html',context)



def courses(request):
	courses = Course.objects.all()
	professors = Professor.objects.all()
	
	context = {
		'courses' : courses,
		'professors' : professors,
		
	}
	return render(request,'review/courses.html',context)

def profs(request):
	courses = Course.objects.all()
	professors = Professor.objects.all()
	
	context = {
		'courses' : courses,
		'professors' : professors,
		
	}
	return render(request,'review/profs.html',context)


def course_detail(request, id):
	course = Course.objects.get(id=id)
	courses = Course.objects.all()
	professors = Professor.objects.all()
	reviews = Review.objects.filter(title_id=course.id)
	context = {
		'cr' : course,
		'courses' : courses,
		'professors' : professors,
		'reviews' : reviews,
	}
	return render(request,'review/course_detail.html',context)


def prof_detail(request, id):
	prof = Professor.objects.get(id=id)
	courses = Course.objects.all()
	professors = Professor.objects.all()
	reviews = Review.objects.filter(P_name_id=prof.id)
	context = {
		'prof' : prof,
		'courses' : courses,
		'professors' : professors,
		'reviews' : reviews,
	}
	return render(request,'review/prof_detail.html',context)


@login_required
def review_create(request):
	if request.method == 'POST':
		form = CreateReviewForm(request.POST)
		if form.is_valid ():
			form.save()
			messages.success(request, f'Review Posted')
			return redirect('homepage')
			
	else:
		form = CreateReviewForm()
	return render(request,'review/review_form.html',{'form':form}) 