from django.shortcuts import render

# Create your views here.
def project(request):
    context={'Project':'active'}
    return render(request,'serv/project.html',context)