from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .f import detail_form, FeedbackForm
from hostupload.models import *
from client_pages2.models import detail
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import datetime
from client_page1.views import fil, fil1
from client import views

def home(request,id):
    prop = Property_Upload.objects.get(id=id)
    pr_type= prop.pr_type
    if pr_type=='2':
        house = House.objects.get(pr=id)

        checkin = request.session['checkin']
        checkout = request.session['checkout']
        guests = request.session['guests']
        single_a,single_wa,double_a,double_wa,triple_a,triple_wa=fil(house, checkin, checkout, guests)
        request.session['single_a']=single_a
        request.session['single_wa'] = single_wa
        request.session['double_a'] = double_a
        request.session['double_wa'] = double_wa
        request.session['triple_a'] = triple_a
        request.session['triple_wa'] = triple_wa
        addres = Property_Upload.objects.get(id=id)
        print(request.session['single_a'])
        x= addres.address.street+','+addres.address.city
        list=[]

        for y in house.amenities.all():

             list.append(y)
        h=[]
        slide=Gallery.objects.filter()
        for i in slide:
            if i.pr.id==id:
                h.append(i.img)

        checkin = request.session['checkin']
        checkout = request.session['checkout']
        guests = request.session['guests']

        if request.method == "POST":
            form = detail_form(request.POST)
            checkin = request.session['checkin']
            checkout = request.session['checkout']
            guests = request.session['guests']

            if form.is_valid():
                detail_item = form.save(commit=False)
                detail_item.save()
                request.session['checkin']=checkin
                # checkout = str(form.cleaned_data['checkout'])
                request.session['checkout']=checkout
                # guests = form.cleaned_data['guests']
                request.session['guests']=guests
                #checkout = str(form.cleaned_data['checkout'])
                #request.session['guests'] = guests
                singlerooms = str(form.cleaned_data['single_a'])
                request.session['single_a'] = singlerooms
                singlerooms_attached = str(form.cleaned_data['single_wa'])
                request.session['single_wa'] = singlerooms_attached
                doublerooms = str(form.cleaned_data['double_a'])
                request.session['double_a'] = doublerooms
                doublerooms_attached = str(form.cleaned_data['double_wa'])
                request.session['double_wa'] = doublerooms_attached
                doublerooms_attached = str(form.cleaned_data['double_wa'])
                request.session['triple_a'] = triplerooms
                triplerooms_attached = str(form.cleaned_data['double_wa'])
                request.session['triple_wa'] = triplerooms_attached
                # print(request.session['guests'],request.session['checkin'])
        else:
            form = detail_form(request=request,initial={'checkout':request.session.get('checkout'),'checkin':request.session.get('checkin'),'guests':request.session.get('guests')})
        return render(request, 'client_pages2/home.html', {'h':h,'slide':slide,'form':form ,'house':house, 'list':list , 'address':x , 'pr_id':id})
        #return HttpResponse(h)
    else:
        hostel = Hostel.objects.get(pr=id)

        checkin = request.session['checkin']
        checkout = request.session['checkout']
        guests = request.session['guests']
        single_a, single_wa, double_a, double_wa, triple_a, triple_wa = fil1(hostel, checkin, checkout, guests)
        request.session['single_a'] = single_a
        request.session['single_wa'] = single_wa
        request.session['double_a'] = double_a
        request.session['double_wa'] = double_wa
        request.session['triple_a'] = triple_a
        request.session['triple_wa'] = triple_wa
        addres = Property_Upload.objects.get(id=id)

        x = addres.address.street + ',' + addres.address.city
        list = []

        for y in hostel.amenities.all():
            list.append(y)

        h = []
        slide = Gallery.objects.filter()
        for i in slide:
            if i.pr.id == id:
                h.append(i.img)

        checkin = request.session['checkin']
        checkout = request.session['checkout']
        guests = request.session['guests']

        if request.method == "POST":
            form = detail_form(request.POST)
            checkin = request.session['checkin']
            checkout = request.session['checkout']
            guests = request.session['guests']

            if form.is_valid():
                detail_item = form.save(commit=False)
                detail_item.save()
                request.session['checkin'] = checkin
                # checkout = str(form.cleaned_data['checkout'])
                request.session['checkout'] = checkout
                # guests = form.cleaned_data['guests']
                request.session['guests'] = guests
                # checkout = str(form.cleaned_data['checkout'])
                # request.session['guests'] = guests
                singlerooms = str(form.cleaned_data['single_a'])
                request.session['single_a'] = singlerooms
                singlerooms_attached = str(form.cleaned_data['single_wa'])
                request.session['single_wa'] = singlerooms_attached
                doublerooms = str(form.cleaned_data['double_a'])
                request.session['double_a'] = doublerooms
                doublerooms_attached = str(form.cleaned_data['double_wa'])
                request.session['double_wa'] = doublerooms_attached
                doublerooms_attached = str(form.cleaned_data['double_wa'])
                request.session['triple_a'] = triplerooms
                triplerooms_attached = str(form.cleaned_data['double_wa'])
                request.session['triple_wa'] = triplerooms_attached
                # print(request.session['guests'],request.session['checkin'])
        else:
            form = detail_form(request=request, initial={'checkout': request.session.get('checkout'),
                                                         'checkin': request.session.get('checkin'),
                                                         'guests': request.session.get('guests')})
        return render(request, 'client_pages2/hostel.html',
                      {'h': h, 'slide': slide, 'form': form, 'hostel': hostel, 'list': list, 'address': x , 'pr_id':id})
        # return HttpResponse(h)



@login_required(login_url='project:login')
def feedback(request,id):

    if request.method =='POST':
        form = FeedbackForm(request.POST)
        form1 = form.save(commit=False)
        form1.pr = Property_Upload.objects.get(id=id)
        form1.save()
        return redirect('/')
    else:
        form = FeedbackForm()
        return render(request,'client_pages2/feedback.html',{'form':form})