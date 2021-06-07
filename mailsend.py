import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login('arpitchauhan988@gmail.com','9329223487')
subject = "hello Arpit"
body = "how are you"
message = "subject:{}\n\n{}".format(subject,body)
listofaddress = ['arpitchauhan1216@gmail.com']
ob.sendmail('arpitchauhan988',listofaddress,message)
print("send email sucessfully")
ob.quit()