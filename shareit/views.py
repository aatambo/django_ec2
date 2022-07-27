import os

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from .dynamo import insert_into_dynamo_table
from .emails import invoke_lambda
from .forms import EmailFormset, FileForm


class FileUploadView(LoginRequiredMixin, View):
    """create new products"""

    template_name = "shareit/upload_file.html"

    def get(self, request, *args, **kwargs):
        """handle HTTP GET"""
        form = FileForm()
        formset = EmailFormset()
        context = {
            "form": form,
            "formset": formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """handle HTTP POST"""
        form = FileForm(request.POST, request.FILES)
        formset = EmailFormset(request.POST)
        context = {
            "form": form,
            "formset": formset,
        }

        if form.is_valid() and formset.is_valid():
            upload = form.save(commit=False)
            upload.save()
            filename = os.path.basename(upload.file.name)
            emails = []

            for form in formset:
                if form.cleaned_data:
                    emails.append(form.cleaned_data["email"])

            # dynamo call
            insert_into_dynamo_table(filename, upload.file.url, upload.file.size)
            # lambda call
            invoke_lambda(request.user.username, upload.file.url, emails)
            messages.success(
                request,
                f"File {filename} has been uploaded successfully and Email sent to recipients.",
            )
            return redirect("shareit:upload")
        return render(request, self.template_name, context)


class AboutView(View):
    """create new products"""

    template_name = "shareit/about.html"

    def get(self, request, *args, **kwargs):
        """handle HTTP GET"""
        return render(request, self.template_name)
