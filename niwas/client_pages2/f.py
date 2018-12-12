from django.forms import ModelForm
from django import forms
from client_pages2.models import detail
from hostupload.models import feedback
from django import forms
import datetime
from . import views


class detail_form(ModelForm):
    class Meta:
        model = detail
        fields = '__all__'

    def __init__(self, *args, request=None, **kwargs):
        super(detail_form, self).__init__(*args, **kwargs)
        single_a= request.session['single_a']
        single_wa = request.session['single_wa']
        double_a = request.session['double_a']
        double_wa = request.session['double_wa']
        triple_a = request.session['triple_a']
        triple_wa = request.session['triple_wa']

        ch= [(X, X) for X in range(0,single_a)]
        self.fields['singlerooms'].choices = ch

        ch2 = [(X, X) for X in range(0, single_wa)]
        self.fields['singlerooms_attached'].choices = ch2

        ch3 = [(X, X) for X in range(0,double_a)]
        self.fields['doublerooms'].choices = ch3

        ch4 = [(X, X) for X in range(0,double_wa)]
        self.fields['doublerooms_attached'].choices = ch4


        ch5 = [(X, X) for X in range(0, triple_a)]
        self.fields['triplerooms'].choices = ch5

        ch6 = [(X, X) for X in range(0, triple_wa)]
        self.fields['triplerooms_attached'].choices = ch6



class FeedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = ['feedback','rating']


  #  def __init__(self, *args, request=None, **kwargs):
   #     super(detail_form, self).__init__(*args, **kwargs)
    #    self.request = request  # perhaps you want to set the request in the Form
     #   if request is not None:
      #      checkout = request.session['checkin']
