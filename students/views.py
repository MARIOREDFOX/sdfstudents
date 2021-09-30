from django.shortcuts import render
from .forms import StudentForms 
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addStudent(request):
    form = StudentForms()
    if request.method == "POST":
        print("submitted")
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
    content = {"forms": form}
    return render(request, 'index.html', content)
    