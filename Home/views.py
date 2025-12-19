from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import payment_form as PaymentModel

# Create your views here.
def index(request):
    context = {
        'variable': "this is variable passed from views.py to index.html"
    }
    return render(request, 'index.html', context)
    # # return HttpResponse("this is homepage")

def about(request):
     return render(request, 'about.html')

def contactUS(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def service1(request):
    return render(request, 'service1.html')

def service2(request):
    return render(request, 'service2.html')

def service3(request):
    return render(request, 'service3.html')

def payment_Plans(request):
    return render(request, 'payment_Plans.html')

def payment_form(request):
    if request.method == 'POST':
        # read submitted form data
        plan = request.POST.get('plan', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        cardnumber = request.POST.get('cardnumber', '')
        phone = request.POST.get('phone', '')
        expdate = request.POST.get('expdate', '')
        cvv = request.POST.get('cvv', '')
        date = request.POST.get('date', '')

        record = PaymentModel(
            plan=plan,
            name=name,
            cardnumber=cardnumber,
            phone=phone,
            email=email,
            expdate=expdate,
            cvv=cvv,
            date=datetime.today()
        )
        record.save()
        context = {'selected_plan': plan, 'success': True, 'customer_name': name}
        return render(request, 'payment_form.html', context)

    # GET: read plan from querystring (?plan=Basic)
    plan = request.GET.get('plan', '')
    context = {'selected_plan': plan}
    return render(request, 'payment_form.html', context)