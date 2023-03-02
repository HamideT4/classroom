from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Etudiant, Groupe
from .forms import EtudiantForm, GroupeForm
from django.http import  HttpResponseRedirect
from django.db.models import Q

def index (request) :
    template = loader.get_template ('index.html')
    return HttpResponse (template.render ())

def students_list(request):
	students = Etudiant.objects.all().order_by('nom')
	return render(request, 'students/students_list.html', {
		'students': students,
	})

def add_student(request):
      submitted = False
      if request.method == "POST":
            form = EtudiantForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_student?submitted=True')
      else:
            form = EtudiantForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'students/add_student.html', {
        'form': form,
        'submitted': submitted,
        })

def update_student(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    form = EtudiantForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students_list')
    return render(request, 'students/update_student.html', {
        'student': student,
        'form': form,
    }) 

def delete_student(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    student.delete()
    return redirect('students_list')

def show_student(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    return render(request, 'students/show_student.html', {
        'student': student,
    })

def groupes_list(request):
	students = Groupe.objects.all().order_by('nom')
	return render(request, 'groupes/groupes_list.html', {'students': students,})

def add_groupe(request):
      submitted = False
      if request.method == "POST":
            form = GroupeForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_groupe?submitted=True')
      else:
            form = GroupeForm
      if 'submitted' in request.GET:
            submitted=False
      return render(request, 'groupes/add_groupe.html', {
        'form': form,
        'submitted': submitted,
        })

def update_groupe(request, groupe_id):
    student = Groupe.objects.get(pk=groupe_id)
    form = GroupeForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('groupes_list')
    return render(request, 'groupes/update_groupe.html', {
        'student': student,
        'form': form,
    })  

def delete_groupe(request, groupe_id):
    student = Groupe.objects.get(pk=groupe_id)
    student.delete()
    return redirect('groupes_list')

def search_student(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(name__icontains=query) | Q(email__icontains=query))
        students = Etudiant.objects.filter(mutiple_q)
        if students:
            return render(request, 'students/students_list.html', {
                'students': students
            })
        else:
            print('Not found ...')
            return render(request, 'students/not_found.html', {})
