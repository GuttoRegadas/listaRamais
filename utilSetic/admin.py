from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import path
from .models import Ramais, Pessoa
from django.urls import reverse
from django import forms
from django.shortcuts import render
import csv

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

@admin.register(Ramais)
class RamisAdmin(admin.ModelAdmin):
    list_display = ('colaborador','ramal','area','sala','andarBloco',)
    fields = ['colaborador','ramal','area','sala','andarBloco',]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Tipo de arquivo errado!')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data[0:]:
                fields = x.split(";")
                created = Ramais.objects.update_or_create(
                    colaborador = fields[0],
                    ramal = fields[1],
                    area = fields[2],
                    sala = fields[3],
                    andarBloco = fields[4],


                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('pessoa',)
    fields = ['pessoa',]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Tipo de arquivo errado!')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data[1:]:
                fields = x.split(";")
                print(type(fields))
                print(fields)
                created = Pessoa.objects.update_or_create(
                    pessoa = fields[0],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)