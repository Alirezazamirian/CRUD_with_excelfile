from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import TakeExcelFile, UpdatePeopleForm, CreatePeopleForm
import openpyxl
from .models import Passenger
import os


def invalid_url(request):
    return render(request, 'crud/404.html')

def upload_excel(request):
    if request.method == 'POST':
        form = TakeExcelFile(request.POST, request.FILES)
        if form.is_valid():
            if Passenger.objects.exists():
                Passenger.objects.all().delete()
            excel_file = request.FILES['excel']
            file_path = os.path.join('uploads', excel_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in excel_file.chunks():
                    destination.write(chunk)
            work_book = openpyxl.load_workbook(excel_file)
            wb = work_book.active
            for row in wb.iter_rows(values_only=True, min_row=2):
                age = row[5] if row[5] else None
                Passenger.objects.create(id=row[0], survived=row[1], pclass=row[2], name=row[3], sex=row[4], age=age,
                                         sibsp=row[6], parch=row[7], ticket=row[8], fare=row[9], cabin=row[10],
                                         embarked=row[11])
            return HttpResponseRedirect(reverse('post_list'))
    else:
        form = TakeExcelFile()
    return render(request, 'crud/crud.html', {'form': form})


class PostListView(ListView):
    model = Passenger
    template_name = 'crud/titanic_people.html'
    paginate_by = 50
    context_object_name = 'people'


class PostCreateView(CreateView):
    model = Passenger
    template_name = 'crud/create_people.html'
    form_class = CreatePeopleForm
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Passenger
    template_name = 'crud/update_form.html'
    success_url = reverse_lazy('post_list')
    form_class = UpdatePeopleForm




class PostDeleteView(DeleteView):
    model = Passenger
    success_url = reverse_lazy('post_list')
    template_name = 'crud/delete_people.html'
