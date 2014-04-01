# Create your views here.
from django.shortcuts import render, redirect
from account.forms import SignUpForm, LoginForm
from django.contrib import messages
from django.views.generic.edit import FormView 
from django.contrib.auth import login, logout


class SignUpView(FormView):
    template_name = "sign_up.html"
    form_class = SignUpForm
    success_url = '/users/login'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, "You have signed up succesfully")
        return super(SignUpView, self).form_valid(form)

#def sign_up(request):
    # function based view
 #   template_name = "sign_up.html"
  #  form = SignUpForm()
   # if request.method == 'POST':
  
    #    form = SignUpForm(request.POST)
     #   if form.is_valid():
      #      form.save()
       #     messages.add_message(request, messages.INFO, "User")
        #    return redirect("/users")
    #return render(request, template_name, {'sign_up_form': form})

def home(request):
  template_name = "home.html"
  return render(request, template_name, {})


def userlogin(request):
  template_name = "login.html"
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = form.cleaned_data['user']
      login(request, user)
      return redirect("/")
  return render(request, template_name, {'form': form})
 







