import datetime
import operator

from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode

from hostupload import models
from client.forms import DetailForm, booking_form
# Create your views here.
from hostupload.models import *



def home(request):

    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            place = form.cleaned_data['place']
            request.session['place'] = place
            checkin = str(form.cleaned_data['checkin'])
            request.session['checkin'] = checkin

            checkout = str(form.cleaned_data['checkout'])
            request.session['checkout'] = checkout

            guests = form.cleaned_data['guests']
            request.session['guests'] = guests
            return redirect('/client_page1/home/')

    else:
        form = DetailForm()

    dictionary = {}
    for houses in House.objects.all():
        if houses.avg_rating >= 1:
            dictionary[houses.pr_id] = houses.avg_rating

    sorted_d = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    key= [x[0] for x in sorted_d]
    keys = key[0:8]
    image_list = []
    address_list = []
    rating_list = []
    for i in keys:
        img = Gallery.objects.filter(pr_id=i)
        image = img[0].img
        image_list.append(image)
        address = Address.objects.get(id=i)
        street = address.street
        city = address.city
        state = address.state

        add = street + ' , ' + city + ' , ' + state
        address_list.append(add)
        rating = dictionary[i]
        rating_list.append(rating)
    mylist = zip(keys,image_list,address_list,rating_list)


    context = {'form':form, 'mylist':mylist}
    return render(request, 'client/home.html', context)








@login_required(login_url='project:login')
def bookRoom(request,id):

    FirstDate = request.session['checkin']
    SecDate =  request.session['checkout']
    guests = request.session['guests']
    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin

    StayDuration = timedeltaSum.days

    # request.session['single_a'] = 5
    # request.session['single_wa'] = 5
    # request.session['double_a'] = 5
    # request.session['double_wa'] = 5
    # request.session['triple_a'] = 5
    # request.session['triple_wa'] = 5
    # request.session['floorbed'] = 5

    property_id=id


    pricing = Pricing_House.objects.get(pr=property_id)

    cost_house = (request.session['single_a']) * (pricing.single_a) + (request.session['single_wa']) * (
        pricing.single_wa) + (request.session['double_a']) * (pricing.double_a) + (request.session['double_wa']) * (
                     pricing.double_wa) + (request.session['triple_a']) * (pricing.triple_a) + (
                 request.session['triple_wa']) * (pricing.triple_wa) + pricing.cleaning + pricing.security + pricing.extra

    total_cost = cost_house * StayDuration



    property = Property_Upload.objects.get(id=property_id)
    street = property.address.street
    city = property.address.city
    state= property.address.state
    zipcode = property.address.zipcode

    id = id


    context = {'checkin': FirstDate, 'checkout':SecDate,'stayduration':StayDuration,'id':id,'totalcost':total_cost, 'street':street,'city':city,'state':state,'zipcode':zipcode,'guests':guests}
    return render(request, 'project/booking_house.html', context)



def store_data_house(request,id):
    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    # request.session['single_a'] = 5
    # request.session['single_wa'] = 5
    # request.session['double_a'] = 5
    # request.session['double_wa'] = 5
    # request.session['triple_a'] = 5
    # request.session['triple_wa'] = 5
    # request.session['floorbed'] = 5


    pricing = Pricing_House.objects.get(pr=id)
    pr_ins = Property_Upload.objects.get(id=id)

    user = request.user

    cost_house= (request.session['single_a'])*(pricing.single_a) + (request.session['single_wa'])*(pricing.single_wa) +(request.session['double_a'])*(pricing.double_a) +(request.session['double_wa'])*(pricing.double_wa)+ (request.session['triple_a'])*(pricing.triple_a) + (request.session['triple_wa'])*(pricing.triple_wa)  + pricing.cleaning + pricing.security + pricing.extra

    total_cost = cost_house* StayDuration



    p=Booking_House.objects.create( check_in=FirstDate, check_out=SecDate, price_paid=total_cost,single_a = request.session['single_a'], single_wa= request.session['single_wa'], double_a=request.session['double_a'], double_wa=request.session['double_wa'], triple_a=request.session['triple_a'], triple_wa=request.session['triple_wa'],pr=pr_ins,user=user)
    p.save()

    del request.session['checkin']
    del request.session['checkout']
    del request.session['single_a']
    del request.session['single_wa']
    del request.session['double_a']
    del request.session['double_wa']
    del request.session['triple_a']
    del request.session['triple_wa']








    current_site = get_current_site(request)
    mail_subject = 'Your Booking is confirmed.'
    message = render_to_string('client/booking_confirm.html', {
        'user': user,
        'domain': current_site.domain,
        'id': id,
    })
    to_email = request.user.email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()






    context = { 'user_name': user}

    return render(request, 'project/payment.html', context)



@login_required(login_url='project:login')
def bookHostel(request,id):
    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']
    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    # request.session['single_a'] = 5
    # request.session['single_wa'] = 5
    # request.session['double_a'] = 5
    # request.session['double_wa'] = 5
    # request.session['triple_a'] = 5
    # request.session['triple_wa'] = 5

    property_id = id
    pricing = Pricing_Hostel.objects.get(id=property_id)
    guests = request.session['guests']
    cost_hostel = (request.session['single_a'])*(pricing.single_a) + (request.session['single_wa'])*(pricing.single_wa) +(request.session['double_a'])*(pricing.double_a) +(request.session['double_wa'])*(pricing.double_wa)+ (request.session['triple_a'])*(pricing.triple_a) + (request.session['triple_wa'])*(pricing.triple_wa) + pricing.cleaning + pricing.security + pricing.extra + pricing.cab + pricing.food

    total_cost = cost_hostel * StayDuration


    id = id

    property = Property_Upload.objects.get(id=property_id)
    street = property.address.street
    city = property.address.city
    state= property.address.state
    zipcode = property.address.zipcode

    images = Gallery.objects.get(pr=property_id)
    image = images.img


    context = {'checkin': FirstDate, 'checkout':SecDate,'stayduration':StayDuration, 'image':image, 'totalcost':total_cost, 'street':street,'city':city,'state':state,'zipcode':zipcode,'guests':guests,'id':id}

    return render(request, 'project/booking_hostel.html', context)





def store_data_hostel(request,id):
    FirstDate = request.session['checkin']
    SecDate = request.session['checkout']

    Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
    Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    timedeltaSum = Checkout - Checkin
    StayDuration = timedeltaSum.days

    # request.session['single_a'] = 5
    # request.session['single_wa'] = 5
    # request.session['double_a'] = 5
    # request.session['double_wa'] = 5
    # request.session['triple_a'] = 5
    # request.session['triple_wa'] = 5

    user = request.user
    pricing = Pricing_Hostel.objects.get(id=id)
    pr_ins = Property_Upload.objects.get(id=id)
    cost_hostel = (request.session['single_a'])*(pricing.single_a) + (request.session['single_wa'])*(pricing.single_wa) +(request.session['double_a'])*(pricing.double_a) +(request.session['double_wa'])*(pricing.double_wa)+ (request.session['triple_a'])*(pricing.triple_a) + (request.session['triple_wa'])*(pricing.triple_wa) + pricing.cleaning + pricing.security + pricing.extra + pricing.cab + pricing.food

    total_cost = cost_hostel * StayDuration

    p = Booking_Hostel.objects.create(check_in=FirstDate, check_out=SecDate, price_paid=total_cost, single_a = request.session['single_a'], single_wa=request.session['single_wa'], double_a=request.session['double_a'], double_wa=request.session['double_wa'], triple_a=request.session['triple_a'], triple_wa=request.session['triple_wa'],pr=pr_ins,user=user)
    p.save()


    current_site = get_current_site(request)
    mail_subject = 'Your Booking is confirmed.'
    message = render_to_string('client/booking_confirm.html', {
        'user': user,
        'domain': current_site.domain,
        'id': id,
    })
    to_email = request.user.email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()















    del request.session['checkin']
    del request.session['checkout']
    del request.session['single_a']
    del request.session['single_wa']
    del request.session['double_a']
    del request.session['double_wa']
    del request.session['triple_a']
    del request.session['triple_wa']

    return render(request, 'project/payment.html')


def cancelbooking_house(request,id):
    booking = Booking_House.objects.get(id = id)
    booking.delete()
    currentuser = request.user
    link = reverse('client:viewbookings')
    return redirect(link)


def cancelbooking_hostel(request,id):
    booking = Booking_Hostel.objects.get(id = id)
    booking.delete()
    currentuser = request.user
    link = reverse('client:viewbookings')
    return redirect(link)


@login_required(login_url='login')
def mybookings(request):
    bookings = Booking_House.objects.filter(user = request.user)
    bookings_hostel = Booking_Hostel.objects.filter(user = request.user)
    context = {'bookings':bookings,'hostel_bookings':bookings_hostel}
    return render(request, 'project/mybookings.html', context)


