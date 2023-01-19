from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.

class LoginView(FormView):
    template_name = 'auth/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context
