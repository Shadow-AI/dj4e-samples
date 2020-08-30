from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from cats.models import Cat, Breed
from cats.forms import CatForm, BreedForm


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cl = Cat.objects.all()
        bc = Breed.objects.all().count()
        return render(request, 'cats/cat_list.html', {'cat_list': cl, 'breed_count': bc})


class CatCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = CatForm()
        return render(request, 'cats/cat_form.html', {'form': form})

    def post(self, request):
        form = CatForm(request.POST)
        if not form.is_valid():
            return render(request, 'cats/cat_form.html', {'form': form})
        form.save()
        return redirect('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(DeleteView, LoginRequiredMixin):
    model = Cat
    success_url = reverse_lazy('cats:all')


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)


class BreedCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = BreedForm()
        return render(request, 'cats/breed_form.html', {'form': form})

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            return render(request, 'cats/breed_form.html', {'form': form})

        form.save()
        return redirect('cats:all')


class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/breed_form.html'
    success = 'cats:all'

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST)
        ctx = {'form': form}
        if not form.is_valid():
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success)


class BreedDelete(LoginRequiredMixin, View):
    template = 'cats/breed_confirm_delete.html'
    model = Breed

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        ctx = {'breed': obj}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        obj.delete()
        return redirect('cats:all')
