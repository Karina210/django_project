from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, resolve_url
from django.template import loader
# from home.forms import FeedbackForm
from home.forms import CustomerForm
from home.models import Customer


def index(request):
    templates = loader.get_template('index.html')
    context = {'message': ' Hello django templates'}

    return HttpResponse(templates.render(context, request))


def new(request):
    new = Customer.objects.all()
    context = {'new': new }
    return render(request, 'new.html', context)


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


# def feedback(request):
#     if request.method == 'GET':
#         context = {'form': FeedbackForm()}
#         return render(request, 'forms/feedback.html', context)
#     elif request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             customer = Customer(firstname=data.get("name"), lastname=data.get("lastname"), age=data.get("age"))
#             print(customer)
#             customer.save()
#         else:
#             print(f'Error validation! {form.errors}')
#
#     return redirect('customers_list_url')


# def customers(request):
#     list=Customer.objects.all()
#
#     context = {'customersList': list}
#     return render(request, "layout/customers.html", context)


def delete_customer(request, customerId):
    customer_for_delete = Customer.objects.get(id=customerId)
    if customer_for_delete is None:
        raise Exception(f'Customer with id {customerId} not found')
    customer_for_delete.delete()
    return redirect('customers_list_url')


def list_customers(request):
    list = Customer.objects.all()

    context = {'customersList': list}
    return render(request, 'customers.html', context)


def create_customer_form(request):
    context = {'url': resolve_url('create_customer'), 'form': CustomerForm(), 'button_message': 'Create'}
    return render(request, 'forms/customer.html', context)


def create_customer(request):
    if request.method != 'POST':
        raise Exception('Not POST method')

    customer_form = CustomerForm(request.POST)
    if not customer_form.is_valid():
        raise Exception('Invalid customer creation form')

    customer_form.save()
    return redirect('customers_list_url')


def find(request, customer_id):
    if customer_id is None:
        raise Exception('Need customer id')

    customer = Customer.objects.get(id=customer_id)
    if customer is None:
        raise Http404(f'Customer "{customer_id}" not found')

    context = {'customer': customer}
    return render(request, 'customer.html', context)


def update(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if customer is None:
        raise Http404(f'Customer "{customer_id}" not found')

    if request.method == 'GET':
        form = CustomerForm(instance=customer)
        context = {'url': resolve_url('update_customer', customer_id=customer.id), 'form': form, 'button_message': 'Update'}
        return render(request, 'forms/customer.html', context)
    elif request.method == 'POST':
        pass
    else:
        raise Exception('Method not allowed')



