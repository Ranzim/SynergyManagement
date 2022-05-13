from django.urls import path
from website.views import (
		index,
		about_us,
		accountingServices,
		financialConsultancy,
		bankingDocumentation,
		projectReporting,
		investmentManagement,
		taxReturns,
		businessSupport,
		
		locations,
		contact_us,
		documentList, 
		
	)

urlpatterns = [
    path('', index, name='index'),
    path('about-us', about_us, name='about_us'),
    # path('our-services', services, name='services'),
	path('accountigServices',accountingServices, name='accountingServices'),
	path('financialConsultancy',financialConsultancy, name='financialConsultancy'),
	path('bankingDocumentation',bankingDocumentation, name='bankingDocumentation'),
	path('projectReporting',projectReporting, name='projectReporting'),
	path('investmentManagement',investmentManagement, name='investmentManagement'),
	path('taxReturns',taxReturns, name='taxReturns'),
	path('businessSupport',businessSupport, name='businessSupport'),
    path('our-locations', locations, name='locations'),
    path('contact-us', contact_us, name='contact_us'),
    path('documents', documentList, name='documents'),
]