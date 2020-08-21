from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from autos.forms import MakeForm, AutoForm
from autos.models import Make, Auto


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        count = Make.objects.all().count()
        alist = Auto.objects.all()
        context = {'auto_list': alist, 'make_count': count}
        return render(request, 'autos/auto_list.html', context)


class MakeView(View, LoginRequiredMixin):
    def get(self, request):
        mlist = Make.objects.all()
        return render(request, 'autos/make_list.html', {'make_list': mlist})


class MakeCreate(View, LoginRequiredMixin):
    template = 'autos/make_form.html'

    def get(self, request):
        form = MakeForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, {'form': form})
        form.save()
        return redirect(reverse_lazy('autos:all'))


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = 'autos/make_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm()
        return render(request, self.template, {'form': form})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, {'form': form})
        form.save()
        return redirect('autos:all')


class MakeDelete(View, LoginRequiredMixin):
    model = Make
    template = 'autos/make_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        return render(request, self.template, {'make': make})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect('autos:all')


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'

    def get(self, request, pk):
        get_object_or_404(Auto, pk=pk)
        form = AutoForm()
        return render(request, self.template, {'form': form})

    def post(self, request, pk):
        auto = get_object_or_404(Auto, pk=pk)
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, {'form': form})
        form.save()
        return redirect('autos:all')


class AutoDelete(View, LoginRequiredMixin):
    template = 'autos/auto_confirm_delete.html'

    def get(self, request, pk):
        get_object_or_404(Auto, pk=pk)
        return render(request, self.template, {'form': MakeForm()})

    def post(self, request, pk):
        make = get_object_or_404(Auto, pk=pk)
        make.delete()
        return redirect('autos:all')
