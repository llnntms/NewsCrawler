import mailer
import crawler
import getpass

articleList = crawler.getArticleList()

ID = input("Google ID: ")
PW = getpass.getpass("Google PW: ")
To = input("To: ")

mailer.sendEmail(articleList, ID, PW, To, False)