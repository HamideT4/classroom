from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Etudiant, Groupe, Commande
from .forms import EtudiantForm, GroupeForm, CommandeForm
from django.http import  HttpResponseRedirect
from django.db.models import Q

from .models import Etudiant, Groupe, Commande
from .forms import EtudiantForm, GroupeForm

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
	groupes = Groupe.objects.all().order_by('nom')
	return render(request, 'groupes/groupes_list.html', {'groupes': groupes,})

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
            submitted=True
      return render(request, 'groupes/add_groupe.html', {
        'form': form,
        'submitted': submitted,
        })

def update_groupe(request, groupe_id):
    groupe = Groupe.objects.get(pk=groupe_id)
    form = GroupeForm(request.POST or None, instance=groupe)
    if form.is_valid():
        form.save()
        return redirect('groupes_list')
    return render(request, 'groupes/update_groupe.html', {
        'groupe': groupe,
        'form': form,
    })  

def delete_groupe(request, groupe_id):
    groupe = Groupe.objects.get(pk=groupe_id)
    groupe.delete()
    return redirect('groupes_list')

def search_student(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(nom__icontains=query) | Q(email__icontains=query))
        students = Etudiant.objects.filter(mutiple_q)
        if students:
            return render(request, 'students/students_list.html', {
                'students': students
            })
        else:
            print('Not found ...')
            return render(request, 'students/not_found.html', {})

def search_group(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(nom__icontains=query))
        groupes = Groupe.objects.filter(mutiple_q)
        if groupes:
            return render(request, 'groupes/groupes_list.html', {
                'groupes': groupes
            })
        else:
            print('Not found ...')
            return render(request, 'groupes/not_found.html', {})
def commande_list(request):
	commandes = Commande.objects.all().order_by('menu')
	return render(request, 'commandes/commande_list.html', {
		'commandes': commandes,
	})

def add_commande(request):
      submitted = False
      if request.method == "POST":
            form = CommandeForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_commande?submitted=True')
      else:
            form = CommandeForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'commandes/add_commande.html', {
        'form': form,
        'submitted': submitted,
        })

def update_commande(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    form = CommandeForm(request.POST or None, instance=commande)
    if form.is_valid():
        form.save()
        return redirect('commande_list')
    return render(request, 'commandes/update_commande.html', {
        'commande': commande,
        'form': form,
    })  

def delete_commande(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    commande.delete()
    return redirect('commande_list')

def search_commande(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(menu__icontains=query))
        commandes = Commande.objects.filter(mutiple_q)
        if commandes:
            return render(request, 'commandes/commande_list.html', {
                'commandes': commandes
            })
        else:
            print('Not found ...')
            return render(request, 'commandes/not_found.html', {})
