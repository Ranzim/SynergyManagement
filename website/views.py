from django.shortcuts import render
from django.views.generic import CreateView
from website.models import Message, Document
from django.core.exceptions import ValidationError
from django.contrib import messages
from .send_emails import message_notification


def index(request):
	return render(request, 'website/index.html')


def about_us(request):
	return render(request, 'website/about_us.html')


def accountingServices(request):
	return render(request, 'website/accountingServices.html')

def financialConsultancy(request):
    return render(request, 'website/FinancialConsultancy.html')

def bankingDocumentation(request):
    return render(request, 'website/bankingDocumentation.html')

def projectReporting(request):
    return render(request, 'website/projectReporting.html')

def investmentManagement(request):
    return render(request, 'website/investmentManagement.html')

def taxReturns(request):
    return render(request, 'website/taxReturns.html')

def businessSupport(request):
    return render(request, 'website/businessSupport.html')


def locations(request):
	return render(request, 'website/locations.html')


def contact_us(request):
	if request.method == 'POST':
		form_data = request.POST
		full_name = form_data.get('name')
		email = form_data.get('email')
		phone_number = form_data.get('phone')
		branch = form_data.get('branch')
		message_query = form_data.get('message')

		message = Message(full_name=full_name,email=email, phone_number=phone_number,branch=branch, message_query=message_query)
		message.save()
		
		message_notification(full_name,email,phone_number, branch, message_query)
		
		messages.success(request, 'Thank you for sending us your query. We will get back to you as soon as possible.')


	return render(request, 'website/contact_us.html')


def documentList(request):
	documents = Document.objects.all()

	context = {
		'documents' : documents
	}

	return render(request, 'website/document_list.html', context)


