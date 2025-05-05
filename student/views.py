from django.shortcuts import render, HttpResponse
from .import models

# Create your views here.
def home(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        checkbox = request.POST.get('checkbox')
        photo = request.FILES.get('photo')
        
        
        if checkbox:
            checkbox = True
        else:
            checkbox = False
        
        student = models.Student(name=name, photo= photo, email=email, phone=phone, password=password, checkbox=checkbox)
        student.save()
        return HttpResponse("Student data saved successfully!")
    
    
    return render(request, 'student/index.html')
