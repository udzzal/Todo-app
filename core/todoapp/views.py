from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo_task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from django.contrib.auth.models import AnonymousUser


from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('mylogin')


class Login_user(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('todo_home')
    
    
class Register_view(FormView):
    template_name='registration.html'
    redirect_authenticated_user=True
    form_class=UserCreationForm
    success_url=reverse_lazy('todo_home')
    
    def form_valid(self,form):
        #response = super().form_valid(form)
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo_home')
        return super().get(*args,**kwargs)
        

class Todo_home(ListView):  
    model=Todo_task
    template_name='hellow.html'
    context_object_name='tasks'
    
    def get_queryset(self):
        if isinstance(self.request.user,AnonymousUser):
            return Todo_task.objects.none()
        else:
            # Filter the queryset based on the current user
            return Todo_task.objects.filter(user=self.request.user)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        #context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        sarch_input=self.request.GET.get('sarch-area') or ''
        if sarch_input:
            context['tasks']=context['tasks'].filter(titel__startswith=sarch_input)
        
        context['sarch_input']=sarch_input    
        
        return context
    

class View_todo(LoginRequiredMixin,DetailView):
    model=Todo_task
    template_name='todo_datils.html'
    context_object_name='details'
    
    
class Create_todo(LoginRequiredMixin,CreateView):
    model=Todo_task
    fields=['titel','description','complete']
    success_url=reverse_lazy("todo_home")
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    


class Update_todo(LoginRequiredMixin,UpdateView):
    model=Todo_task 
    fields=['titel','description','complete']
    success_url=reverse_lazy("todo_home")  


class Delete_todo(LoginRequiredMixin,DeleteView):
    model=Todo_task
    template_name='todoapp/todo_task_delete.html'
    context_object_name='tasks'
    success_url=reverse_lazy("todo_home")



