import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
'''SMTP (Simple Mail Transfer Protocol) is used in sending and receiving email'''
ob.ehlo()
ob.starttls()
ob.login('syedhuzaifaahmed01@gmail.com','urgpxushlwpubeci')
subject="ISSB Aarif Chaudhry"
body="You are requested to join meeting from this link https://meet.google.com/gjm-xcgv-xna"
message="subject:{}\n\n{}".format(subject,body)
listadd=["syedhuzaifaahmed6@gmail.com"]
ob.sendmail('Syed Huzaifa Ahmed',listadd,message)
print("Send Mail")
ob.quit()