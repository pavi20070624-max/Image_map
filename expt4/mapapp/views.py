from django.shortcuts import render
def map(request):
    return render(request,'map.html')
def restaurant(request):
    return render(request,'restaurant.html')
def dental(request):
    return render(request,'dental.html')
def showroom(request):
    return render(request,'showroom.html')
def school(request):
    return render(request,'school.html')
def hospital(request):
    return render(request,'hospital.html')
# Create your views here.
