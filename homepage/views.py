from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

def home(request):
    context = {'latest_question_list': 'test'}
    return render(request, 'home.html', context)


# multistep form
class ContactWizard(SessionWizardView):
    template_name = "register.html"
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return render(self.request, 'done.html', {'form_data': form_data})

def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    print(form_data)
    return form_data