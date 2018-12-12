from hostupload.models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.db import models





class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class Pricing_HostelForm(ModelForm):
    class Meta:
        model = Pricing_Hostel
        fields = ['single_a','single_wa','double_a','double_wa','triple_a','triple_wa','four_a','four_wa','cleaning','security','cab','food','extra']


class Pricing_HouseForm(ModelForm):
    class Meta:
        model = Pricing_House
        fields = ['single_a','single_wa','double_a','double_wa','triple_a','triple_wa','floorbed','cleaning','security','extra']


# class AmenitiesForm(ModelForm):
#     # AMEN_CHOICES=(
#     # ('1','A.C'),
#     # ('2','Freeze'),
#     # ('3','Cooler'),
#     # )
#     #
#     # model_categories = forms.MultipleChoiceField(
#     #             widget = forms.CheckboxSelectMultiple,
#     #             choices = AMEN_CHOICES
#     #     )
#     # class Meta:
#     #     model = Amenities
#     #     fields = ['model_categories']
#      amenities = forms.ModelMultipleChoiceField(queryset=Amenities.objects.all(),
#      widget=forms.CheckboxSelectMultiple)
#      class Meta:
#         model=Amenities
#         fields=["amenities"]

class UploadForm(ModelForm):
    class Meta:
        model = Property_Upload
        fields = ['shareable','pr_is_personal','for_business','pr_type']

class HostelForm(ModelForm):
    class Meta:
        model = Hostel
        fields = ['single_a','single_wa','double_a','double_wa','triple_a','triple_wa','four_a','four_wa','amenities','description']



class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['single_a','single_wa','double_a','double_wa','triple_a','triple_wa','floorbed','amenities','description']
