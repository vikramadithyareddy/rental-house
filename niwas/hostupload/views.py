from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from hostupload.forms import AddressForm,Pricing_HostelForm,Pricing_HouseForm,UploadForm,HostelForm,HouseForm
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from hostupload.models import Property_Upload,Hostel,Amenities,Gallery
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory

def UploadHostelview(request):
    ImageFormset = modelformset_factory(Gallery, fields=('img',), extra=3 , max_num=8)


    if request.method=='POST':
        hostel = HostelForm(data=request.POST)
        price = Pricing_HostelForm(data=request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        pid = request.session.get('property')
        Property_Uplo = Property_Upload.objects.get(id=pid)

        if hostel.is_valid() and price.is_valid() and formset.is_valid():

            for file in formset:
                if file.cleaned_data:
                    try:

                        photo = Gallery(pr=Property_Uplo, img=file.cleaned_data.get('img'))

                        photo.save()
                    except Exception as e:
                        break

            hostelinstance = hostel.save(commit=False)
            hostelinstance.pr = Property_Uplo
            priceinstance = price.save(commit=False)
            priceinstance.pr = Property_Uplo
            priceinstance.save()
            price.save()
            hostelinstance.price = priceinstance
            hostel_instance=hostel.save()
            for amenity in hostel_instance.amenities.all():
                hostel_instance.amenities.add(amenity)
                hostel_instance.save()

            return render(request,'hostupload/done.html')

    else:
        hostel = HostelForm()
        price = Pricing_HostelForm()
        ImageFormset = ImageFormset(queryset=Gallery.objects.none())

        return render(request,'hostupload/hostel.html',{'hostel':hostel,'price':price,'image':ImageFormset, })

def UploadHouseview(request):
    ImageFormset = modelformset_factory(Gallery, fields=('img',), extra=3 , max_num=8)

    if request.method=='POST':
        house = HouseForm(data=request.POST)
        price = Pricing_HouseForm(data=request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)

        pid =  request.session.get('property')
        Property_Uplo = Property_Upload.objects.get(id=pid)

        if house.is_valid() and price.is_valid() and formset.is_valid():

            for file in formset:
                if file.cleaned_data:
                    try:

                        photo = Gallery(pr=Property_Uplo, img=file.cleaned_data.get('img'))

                        photo.save()
                    except Exception as e:
                        break


            houseinstance = house.save(commit=False)
            houseinstance.pr = Property_Uplo
            priceinstance = price.save(commit=False)
            priceinstance.pr = Property_Uplo
            priceinstance.save()
            price.save()
            houseinstance.price = priceinstance
            house_instance=house.save()
            for amenity in house_instance.amenities.all():
                house_instance.amenities.add(amenity)
                house_instance.save()

            return render(request,'hostupload/done.html')

    else:
        house = HouseForm()
        price = Pricing_HouseForm()
        ImageFormset = ImageFormset(queryset=Gallery.objects.none())

        return render(request,'hostupload/house.html',{'house':house,'price':price,'image':ImageFormset})


@login_required(login_url='login')
def UploadFormview(request):

    if request.method=='POST':
        upload = UploadForm(data=request.POST)
        address = AddressForm(data=request.POST)

        if upload.is_valid() and address.is_valid() :
            form = upload.save(commit=False)
            form.pr_type = upload.cleaned_data['pr_type']
            form.user = request.user
            add = address.save()
            form.address = add
            form.save()
            request.session['property'] = form.id
            if upload.cleaned_data['pr_type']=='1':
                return redirect('hostupload:hostel')
            else:
                return redirect('hostupload:house')

        else:
            print(upload.errors,address.errors)
    else:

        upload = UploadForm()
        address = AddressForm()

    return render(request,'hostupload/main-upload.html',{'upload':upload,'address':address})
