from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        # temp변수는 POST 요청이 오면 html의 text를 가져온다.
        temp = request.POST.get('hello_world_input')
        # now_hello_world 변수를 model HelloWorld 변수로 만들어주고
        now_hello_world = HelloWorld()
        # .text 해서 temp 정보를 가져온뒤 .save 해서 저장한다.
        now_hello_world.text = temp
        now_hello_world.save()
        # HttpResponseRedirect해서 최종값이 계속 저장 되는것을 막고 reverse해서 ()안의 값으로 돌아간다.
        # 이때 중요한것은 urls.py 에 app_name을 저장하면 여기서 그 값을 쓸수있다.!
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'