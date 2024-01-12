import json
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.http import JsonResponse
from .models import Student,Voter
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout 
from student.forms import UserCreationForm, LoginForm

# Create your views here.
def votingTemp(request):
    students = Voter.objects.filter(id__lte=2)
    template = loader.get_template('votingtemp/index.html')
    context = {
        "students": students
    }
    return HttpResponse(template.render(context, request))

def index(request):
    students = Student.objects.filter(id__lte=2)
    template = loader.get_template('student/index.html')
    context = {
        "students": students
    }
    return HttpResponse(template.render(context, request))
def voter(request):
    students = Voter.objects.filter(id__lte=2)
    template = loader.get_template('student/index.html')
    context = {
        "students": students
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def my_view(request, id=None):
    if request.method == 'GET':
        if id is not None:
            # Retrieve a specific instance
            try:
                instance = Voter.objects.get(id=id)
                data = {'message': 'Retrieved instance', 'instance': instance}
                return JsonResponse(data)
            except Voter.DoesNotExist:
                return JsonResponse({'message': 'Instance not found'}, status=404)
        else:
            voters = Voter.objects.filter(id__lte=1000000000)
            template = loader.get_template('student/voters.html')
            context = {
                "voters": voters
            }
            return HttpResponse(template.render(context, request))


    elif request.method == 'POST':
        # Create a new instance
        id_number = request.POST.get('id_number')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name= request.POST.get('last_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        region = request.POST.get('region')
        new_instance = Voter.objects.create(
            id_number=id_number,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            age=age,
            gender=gender,
            phone=phone,
            city=city,
            region=region
            )
        new_instance = Voter.objects.filter(id__lte=8)
        template = loader.get_template('student/voters.html')
        context = {
                "voters": new_instance
            }
        if(new_instance):
            return HttpResponse(template.render(context, request))
        else:
            print(new_instance)
def edit(request,id):
        try:
            instance = Voter.objects.get(id=id)
            instance.id_number = request.POST.get('id_number')
            instance.first_name=request.POST.get('first_name')
            instance.middle_name=request.POST.get('middle_name')
            instance.last_name=request.POST.get('last_name')
            instance.age=request.POST.get('age')
            instance.gender=request.POST.get('gender')
            instance.phone=request.POST.get('phone')
            instance.city=request.POST.get('city')
            instance.region=request.POST.get('region')
            instance.save()
            data = {'message': 'Updated instance', 'instance': instance}
            return redirect('voter')
        except Voter.DoesNotExist:
            return JsonResponse({'message': 'Instance not found'}, status=404)
def  delete(request,id):
    try:
        instance = Voter.objects.get(id=id)
        instance.delete()
        return redirect('voter')
    except Voter.DoesNotExist:
        return JsonResponse({'message': 'Instance not found'}, status=404)

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'student/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'student/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
