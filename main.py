import mailer
import crawler
import getpass

import sys

articleList = crawler.getArticleList()

smtpLoginID = sys.argv[1]
smtpLoginPW = sys.argv[2]

sendTo = sys.argv[3]

mailer.sendEmail(articleList, smtpLoginID, smtpLoginPW, sendTo, False)
