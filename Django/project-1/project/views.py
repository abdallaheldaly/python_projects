from django.shortcuts import render
#from .models import Project

# Create your views here.
def index(request):
#    project = Project.objects.all()
#    context = {
#        'projects':projects
#    }

    return render(request, 'project/index.html')# , context
