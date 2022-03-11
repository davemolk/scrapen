two ways to instantiate the mail sender:
1) 

from scrapy.mail import MailSender
mailer = MailSender()


2)
mailer.MailSender.from_settings(settings) 

mailer.send(to=["someone@example.com"], subject="Some subject", body="Some body", cc=["another@example.com"])



# import module
from scrapy.mail import MailSender
  
# setup mailer
mailer = MailSender(mailfrom="Something@gmail.com",
                    smtphost="smtp.gmail.com", smtpport=465, smtppass="MySecretPassword")
  
# send mail
mailer.send(to=["abc@gmail.com"], subject="Scrapy Mail",
            body="Hi ! GeeksForGeeks", cc=["another@example.com"])