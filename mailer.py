import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta


def sendEmail(articleList, loginId, loginPw, To, debug):
	if not debug:	
		email = MIMEMultipart('alternative')
		email['Subject'] = "[ZDnet news] " + (datetime.now() - timedelta(days=1)).strftime("%Y%m%d") 

		contentHTML = "<h2>Yesterday's Articles from ZDnet Kor</h2></br></br>"
		for article in articleList:
			contentHTML = contentHTML + "<p><a href=" + article['link'] +">" + article['title'] + "</a></p>"
		email.attach(MIMEText(contentHTML,'html'))

		email['From'] = loginId + "@gmail.com"
		email['To'] = To

		s = smtplib.SMTP_SSL('smtp.gmail.com',465)
		s.login(loginId, loginPw)
		s.send_message(email)
		s.quit()
