from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    data=Student.objects.all()
    context={"data": data}
    return render(request, 'index.html',context)



def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")

    return render(request, 'index.html')


def updateData(request, id):
    # Fetch the student object
    student = Student.objects.get(id=id)

    if request.method == "POST":
        # Update the student object with the new data
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.save()
        
        # Redirect to the index page after successful update
        return redirect("/")
    
    # Render the edit form with the student data for GET requests
    context = {"d": student}
    return render(request, 'edit.html', context)


def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")



def about(request):
    return render(request, 'about.html')