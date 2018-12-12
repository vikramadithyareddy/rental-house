from django.shortcuts import render
from django.http import HttpResponse
from hostupload.models import *


def map(request):
    p=[]
    print(k)
    for i in k:
        x = k
        print(x)
        s=','
        address=[]
        address.append(i.address.street)
        address.append(i.address.city)
        address.append(i.address.state)
        addres=s.join(address)
        p.append(addres)
    print(p)
    sel={
    "selected":p
    }
    return render(request,'client_page1/maps.html',context=sel)

def priceh(h,home):
    if h==1:
        price=home.price.single_a+home.price.single_wa+home.price.double_a+home.price.double_wa+home.price.triple_a+home.price.triple_wa+home.price.floorbed+home.price.cleaning+home.price.security+home.price.extra
    if h==2:
        price=home.price.single_a+home.price.single_wa+home.price.double_a+home.price.double_wa+home.price.triple_a+home.price.triple_wa+home.price.four_a+home.price.four_wa+home.price.cab+home.price.food+home.price.cleaning+home.price.security+home.price.extra
    print(price)
    return price


def block(request):
    gallery = []
    avgrating = []
    l = []
    house = House.objects.all()
    hostel = Hostel.objects.all()
    for housei in house:
        rating = House.objects.get(pr=housei.pr)
        avgrating.append(rating.avg_rating)
        l.append(housei.pr)
    for hosteli in hostel:
        rating = Hostel.objects.get(pr=hosteli.pr)
        avgrating.append(rating.avg_rating)
        l.append(hosteli.pr)
    print(l)
    for home in l:
        slide = Gallery.objects.filter(pr=home)
        print(slide)
        gallery.append(slide[0].img)
    global k
    k = l
    mylist = zip(l, gallery, avgrating)
    sel = {"selected": mylist}
    return render(request, 'client_page1/block.html', context=sel)

def home(request):
    global k
    place=request.session['place']
    checkin=request.session['checkin']
    checkout = request.session['checkout']
    guest=request.session['guests']
    print(guest)
    if place:
        addressh=Address.objects.filter(city = place)
        house =[]
        hostel=[]
        gallery=[]
        l=[]
        avgrating=[]
        print(addressh)
        for address in addressh:
            houses=House.objects.filter(pr=Property_Upload.objects.get(address=address))
            if houses:
                house.append(houses[0])
            hostels=Hostel.objects.filter(pr=Property_Upload.objects.get(address=address))
            if hostels:
                hostel.append(hostels[0])
    else:
        hostel = Hostel.objects.all()
        house=House.objects.all()
    if request.method=="POST":
        low=500
        medium=1000
        high=15000
        housetype = request.POST.get('housetype')
        pricerange = request.POST.get('pricerange')
        checkinf=request.POST.get("checkin")
        checkoutf=request.POST.get("checkout")
        checkin=checkinf
        checkout=checkoutf
        request.session['checkin'] = checkin
        request.session['checkout'] = checkout
        if pricerange != "none":
            phouse = []
            phostel = []
            for house in house:
                price = priceh(1, house)
                print(price)
                if pricerange == "low" and 0 < price < 5000:
                    phouse.append(house)
                if pricerange == "meadium" and 5000 < price < 10000:
                    phouse.append(house)
                if pricerange == "high" and 10000 < price:
                    phouse.append(house)
            for hostel in hostel:
                price = priceh(2, hostel)
                if pricerange == "low" and 0 < price < 5000:
                    phouse.append(hostel)
                if pricerange == "meadium" and 5000 < price < 10000:
                    phouse.append(hostel)
                if pricerange == "high" and 10000 < price:
                    phouse.append(hostel)
            house = phouse
            hostel = phostel
            print(house)
            print(hostel)
        if housetype!="none" :
            if housetype=="house":
                for housei in house:
                    nsingle,nsinglew,ndouble,ndoublew,ntriple,ntriplew=fil(housei,checkin,checkout,guest)
                    total=nsingle+nsinglew+2*ndouble+2*ndoublew+3*ntriple+3*ntriplew
                    print(total)
                    if total >= guest:
                        l.append(housei.pr)
                k=l
                print(checkin)
                print(checkout)
                for i in l:
                    slide=Gallery.objects.get(id=i.id)
                    gallery.append(slide.img)
                    rating=House.objects.get(pr=i)
                    avgrating.append(rating.avg_rating)
                print(gallery)
                mylist = zip(l , gallery,avgrating)
                sel={"selected" : mylist,"checkin":checkin,"checkout":checkout}
                return render(request,'client_page1/home.html',context=sel)
            if housetype=="hostel":
                for hosteli in hostel:
                    nsingle,nsinglew,ndouble,ndoublew,ntriple,ntriplew=fil1(hosteli,checkin,checkout,guest)
                    total=nsingle+nsinglew+2*ndouble+2*ndoublew+3*ntriple+3*ntriplew
                    print(total)
                    if total >= guest:
                        l.append(hosteli.pr)
                k=l
                print(checkin)
                print(checkout)
                for i in l:
                    slide=Gallery.objects.get(id=i.id)
                    gallery.append(slide.img)
                    rating=Hostel.objects.get(pr=i)
                    avgrating.append(rating.avg_rating)
                print(gallery)
                mylist = zip(l , gallery,avgrating)
                sel={"selected" : mylist,"checkin":checkin,"checkout":checkout}
                return render(request,'client_page1/home.html',context=sel)
    # housel=fil(house,checkin,checkout,guest)
    for housei in house:
        nsingle,nsinglew,ndouble,ndoublew,ntriple,ntriplew=fil(housei,checkin,checkout,guest)
        total=nsingle+nsinglew+2*ndouble+2*ndoublew+3*ntriple+3*ntriplew
        print(total)
        if total >= guest:
            l.append(housei.pr)
            avgrating.append(housei.avg_rating)
    for hosteli in hostel:
        nsingle,nsinglew,ndouble,ndoublew,ntriple,ntriplew=fil1(hosteli,checkin,checkout,guest)
        total=nsingle+nsinglew+2*ndouble+2*ndoublew+3*ntriple+3*ntriplew
        print(total)
        if total >= guest:
            l.append(hosteli.pr)
            avgrating.append(hosteli.avg_rating)
    k=l
    print(checkin)
    print(checkout)
    print(l)
    for i in l:
        print(i.id)
        slide=Gallery.objects.get(id=i.id)
        gallery.append(slide.img)
    print(gallery)
    mylist = zip(l,gallery,avgrating)
    sel={"selected": mylist,"checkin":checkin,"checkout":checkout}
    return render(request,'client_page1/home.html',context=sel)

def fil(house,checkin,checkout,guest):
    # a=int(checkin[0:4])
    # a1=int(checkin[5:7])
    # a2=int(checkin[8:10])
    # b=int(checkout[0:4])
    # b1=int(checkout[5:7])
    # b2=int(checkout[8:10])
    bhouse=Booking_House.objects.filter(pr = house.pr)
    single=house.single_a
    singlew=house.single_wa
    double=house.double_a
    doublew=house.double_wa
    triple=house.triple_a
    triplew=house.triple_wa
    bsingle=0
    bsinglew=0
    bdouble=0
    bdoublew=0
    btriple=0
    btriplew=0
    if len(bhouse) != 0:
        for bhouse in bhouse:
            bcheckind=bhouse.check_in
            bcheckoutd=bhouse.check_out
            bcheckin = bcheckind.isoformat()
            bcheckout = bcheckoutd.isoformat()
            c=int(bcheckin[0:4])
            c1=int(bcheckin[5:7])
            c2=int(bcheckin[8:10])
            d=int(bcheckout[0:4])
            d1=int(bcheckout[5:7])
            d2=int(bcheckout[8:10])
            if checkin<bcheckin and checkout<bcheckout:
            # if a2<c2 and a1<=c1 and a<=c:
            #     if b2<d2 and b1<=d1 and b<=d:
                bsingle+=bhouse.single_a
                bsinglew+=bhouse.single_wa
                bdouble+=bhouse.double_a
                bdoublew+=bhouse.double_wa
                btriple+=bhouse.triple_a
                btriplew+=bhouse.triple_wa
            if checkin>bcheckin and checkout<bcheckout:
            # if a2>c2 and a1>=c1 and a>=c:
            #     if b2<d2 and b1<=d1 and b<=d:
                bsingle+=bhouse.single_a
                bsinglew+=bhouse.single_wa
                bdouble+=bhouse.double_a
                bdoublew+=bhouse.double_wa
                btriple+=bhouse.triple_a
                btriplew+=bhouse.triple_wa
            if checkin>bcheckin and checkout>bcheckout:
            # if a2>c2 and a1>=c1 and a>=c:
            #     if b2>d2 and b1>=d1 and b>=d:
                bsingle+=bhouse.single_a
                bsinglew+=bhouse.single_wa
                bdouble+=bhouse.double_a
                bdoublew+=bhouse.double_wa
                btriple+=bhouse.triple_a
                btriplew+=bhouse.triple_wa
            if checkin==bcheckin and checkout==bcheckout:
            # if a2<=c2 and a1<=c1 and a<=c:
            #     if b2<=d2 and b1<=d1 and b<=d:
                bsingle=bsingle+bhouse.single_a
                bsinglew+=bhouse.single_wa
                bdouble+=bhouse.double_a
                bdoublew+=bhouse.double_wa
                btriple+=bhouse.triple_a
                btriplew+=bhouse.triple_wa
    nsingle=single-bsingle
    nsinglew=singlew-bsinglew
    ndouble=double-bdouble
    ndoublew=doublew-bdoublew
    ntriple=triple-btriple
    ntriplew=triplew-btriplew
    return nsingle,nsinglew,ndouble,ndoublew,ntriple,ntriplew
def fil1(hostel,checkin,checkout,guest):
    # a=int(checkin[0:4])
    # a1=int(checkin[5:7])
    # a2=int(checkin[8:10])
    # b=int(checkout[0:4])
    # b1=int(checkout[5:7])
    # b2=int(checkout[8:10])
    # l=[]
    bhostel=Booking_Hostel.objects.filter(pr = hostel.pr)
    single=hostel.single_a
    singlew=hostel.single_wa
    double=hostel.double_a
    doublew=hostel.double_wa
    triple=hostel.triple_a
    triplew=hostel.triple_wa
    bsingle=0
    bsinglew=0
    bdouble=0
    bdoublew=0
    btriple=0
    btriplew=0
    if len(bhostel) != 0:
        for bhostel in bhostel:
            bcheckind=bhostel.check_in
            bcheckoutd=bhostel.check_out
            bcheckin = bcheckind.isoformat()
            bcheckout = bcheckoutd.isoformat()
            c=int(bcheckin[0:4])
            c1=int(bcheckin[5:7])
            c2=int(bcheckin[8:10])
            d=int(bcheckout[0:4])
            d1=int(bcheckout[5:7])
            d2=int(bcheckout[8:10])
            if checkin<bcheckin and checkout<bcheckout:
            # if a2<c2 and a1<=c1 and a<=c:
            #     if b2<d2 and b1<=d1 and b<=d:
                bsingle+=bhostel.single_a
                bsinglew+=bhostel.single_wa
                bdouble+=bhostel.double_a
                bdoublew+=bhostel.double_wa
                btriple+=bhostel.triple_a
                btriplew+=bhostel.triple_wa
            if checkin>bcheckin and checkout<bcheckout:
            # if a2>c2 and a1>=c1 and a>=c:
            #     if b2<d2 and b1<=d1 and b<=d:
                bsingle+=bhostel.single_a
                bsinglew+=bhostel.single_wa
                bdouble+=bhostel.double_a
                bdoublew+=bhostel.double_wa
                btriple+=bhostel.triple_a
                btriplew+=bhostel.triple_wa
            if checkin>bcheckin and checkout>bcheckout:
            # if a2>c2 and a1>=c1 and a>=c:
            #     if b2>d2 and b1>=d1 and b>=d:
                bsingle+=bhostel.single_a
                bsinglew+=bhostel.single_wa
                bdouble+=bhostel.double_a
                bdoublew+=bhostel.double_wa
                btriple+=bhostel.triple_a
                btriplew+=bhostel.triple_wa
            if checkin==bcheckin and checkout==bcheckout:
            # if a2<=c2 and a1<=c1 and a<=c:
            #     if b2<=d2 and b1<=d1 and b<=d:
                bsingle+=bhostel.single_a
                bsinglew+=bhostel.single_wa
                bdouble+=bhostel.double_a
                bdoublew+=bhostel.double_wa
                btriple+=bhostel.triple_a
                btriplew+=bhostel.triple_wa
    nsingle=single-bsingle
    nsinglew=singlew-bsinglew
    ndouble=double-bdouble
    ndoublew=doublew-bdoublew
    ntriple=triple-btriple
    ntriplew=triplew-btriplew
    return nsingle,nsinglew,ndouble,ndoublew,ntriple,ntriplew