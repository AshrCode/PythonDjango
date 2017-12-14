from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import List
# Create your views here.


def index(request):
    all_todo_items = List.objects.all()
    html = '<h2>Todo Items</h2>'
    template = loader.get_template('todolist/index.html')

    # following is a dictionary
    context = {
        'list': all_todo_items
    }
    """
    for list in all_todo_items:
        url = '/todolist/' + str(list.id) + '/'
        html += '<a href="' + url + '">' + list.title + '</a></br>'
    """
    return HttpResponse(template.render(context, request))


def detail(request, list_id):
    todo_item = List.objects.filter(id=list_id)
    context = {'list_item': todo_item}

    # return HttpResponse("<h2>Details for Todo List item " + list_id + "</h2>")
    return render(request, 'todolist/detail.html', context)
