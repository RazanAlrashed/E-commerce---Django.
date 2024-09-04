from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse , JsonResponse
from .models import storetype,itemdetails,items,cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .form import creatuserform,loginuserform
# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render({'request': request}))

def listitems(request):
    p=items.objects.filter(st_id=1)
    template=loader.get_template('listitems.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def Elistitems(request):
    p=items.objects.filter(st_id=2)
    template=loader.get_template('Elistitems.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def details(request,id):
    template=loader.get_template('details.html')
    data=itemdetails.objects.select_related('items').filter(id=id).first()
    data.total=data.qty * data.items.price
    return HttpResponse(template.render({'data':data , 'request':request}))

def Edetails(request,id):
    template=loader.get_template('Edetails.html')
    data=itemdetails.objects.select_related('items').filter(id=id).first()
    data.total=data.qty * data.items.price
    return HttpResponse(template.render({'data':data , 'request':request}))
@csrf_exempt
def add_to_cart(request):
    id=request.POST.get("id")
    p=cart(itemid=id)
    p.save()
    row=cart.objects.all()
    count=0
    for item in row:
        count=count+1
    request.session["cart"]=count
    return JsonResponse({'count' : count})

@login_required(login_url='/auth_login/')
def checkout(request):
    template=loader.get_template('checkout.html')
    return HttpResponse(template.render({'request': request}))

@csrf_exempt
def auth_login(request):
    form=loginuserform()
    if request.method=='POST':
        form=loginuserform(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'checkout.html')
    context={'form':form}
    return render(request,'auth_login.html',context)

@csrf_exempt

def auth_register(request):
    template=loader.get_template('auth_register.html')
    form=creatuserform()
    if request.method=='POST':
        form=creatuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))

def show_cart(request):
    cart_items = cart.objects.all()
    return render(request, 'checkout.html', {'cart': cart_items})
