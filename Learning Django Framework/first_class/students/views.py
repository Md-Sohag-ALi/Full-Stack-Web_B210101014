from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
# Create your views here.
def student_list(request):
    students = Student.objects.all() # student table er so data chole asbe
    return render(request,'students/student_list.html',{'students': students})
    
def student_create(request):
    if request.method == 'POST':#form submit hole
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else :
        form = StudentForm()#যখন user প্রথমবার page open করে (GET request)
    return render(request,'students/student_create.html',{'form':form})    


def student_update(request ,pk):
    student = get_object_or_404(Student,pk = pk)
    if request.method == 'POST': #update button a chap dile
        form = StudentForm(request.POST ,request.FILES ,instance=student) #form banano hocche,instance =student mane ager student update korbe
        if form.is_valid():
            form.save()
            return redirect('student_list')#save হওয়ার পর list page-এ নিয়ে যাবে
    else:
        form=StudentForm(instance=student)
    return render(request,'students/student_create.html',{'form': form})    
   
def student_delete(request,pk):
    student = get_object_or_404(Student,pk =pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html',{'student': student})

        