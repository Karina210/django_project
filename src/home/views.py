from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from home.forms import FeedbackForm


def index(request):
    templates = loader.get_template('index.html')
    context = {'message': ' Hello django templates'}

    return HttpResponse(templates.render(context, request))


def query(request):
    contex = {'message': request.GET.get('name')}

    return HttpResponse(render(request, 'index.html', contex))


def name(request):
    value = request.GET.get('name')
    return HttpResponse("hi " + value)


def age(request):
    value = request.GET.get('age')
    if int(value) > 18:
        return HttpResponse('Yes')
    else:
        return HttpResponse('No')


def date1(request):
    value = request.GET.get('date')
    if '01.01' in value:
        return HttpResponse('hny ' + value)
    else:
        return HttpResponse(value)


def com(request):
    value = request.GET.get('com')
    c = 0
    for i in value:
        if i in 'aeiouyауоыиэяюёе':
            c += 1
    return HttpResponse(str(c) + ',' + str(len(value)))


def comm(request):
    value = request.GET.get('name')
    value2 = request.GET.get('comm')
    return HttpResponse('(c)' + ' ' + value + ' ' + value2)


def index1(request):
    context = {'message': request.GET.get('name')}
    context2 = {'ln': request.GET.get('ln')}
    return HttpResponse(render(request, 'index.html', context2))


def feedback(request):
    if request.method == 'GET':
        context = {'form': FeedbackForm()}
        return render(request, 'forms/feedback.html', context)
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(f'{data.get("name")}|{data.get("lastname")}|{data.get("age")}')
        else:
            print(f'Error validation! {form.errors}')

