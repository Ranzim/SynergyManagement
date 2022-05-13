from django.core.mail import EmailMessage
from synergy.settings import EMAIL_HOST_USER


def message_notification(sender,email,phone_number,branch,message_query):
	subject = f"Message Inquiry - {sender}" 

	message = f"Sender - {sender} \nEmail - {email} \nPhone - {phone_number} \nBranch - {branch} \n\nQuery: \n\n'{message_query}'"
	print(message)

	email = EmailMessage(
	    subject=subject,
	    body=message,
	    from_email=EMAIL_HOST_USER,
	    to=['beingbiplov@gmail.com'],
	)
	try:
		email.send()
	except:
		print('Email was not sent.')