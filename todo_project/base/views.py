from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def home(request):
    todos = Todo.objects.all() # Fetch all Todo objects from the database 
    return render(request, "index.html", context={"todos": todos})

def todo_types(request):
    return render(request, "todo_types.html")

def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(
            name = name, 
            description = description, 
            status = status
            )
        # Todo.objects.create(**request.POST)
        return redirect('home/') 
    return render(request, 'create.html', context={"message": "Todo created successfully!"})
