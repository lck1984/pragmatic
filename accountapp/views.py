from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

    # if request.method == "POST":
    #     # temp변수는 POST 요청이 오면 html의 text를 가져온다.
    #     temp = request.POST.get('hello_world_input')
    #     # now_hello_world 변수를 model HelloWorld 변수로 만들어주고
    #     now_hello_world = HelloWorld()
    #     # .text 해서 temp 정보를 가져온뒤 .save 해서 저장한다.
    #     now_hello_world.text = temp
    #     now_hello_world.save()
    #     # HttpResponseRedirect해서 최종값이 계속 저장 되는것을 막고 reverse해서 ()안의 값으로 돌아간다.
    #     # 이때 중요한것은 urls.py 에 app_name을 저장하면 여기서 그 값을 쓸수있다.!
    #     return HttpResponseRedirect(reverse('accountapp:hello_world'))
    # else:
    #     hello_world_list = HelloWorld.objects.all()
    #     return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

