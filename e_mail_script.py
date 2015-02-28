import smtplib

# Send E-mail With Snow Report
def send_snow(val):
	username = '@gmail.com'
	password = 
	destination = '@gmail.com'
	msg = ("It Snowed! This much: get up there kid!")
	#msg['Subject'] = 'Eldora Snow Report'
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	#try:
        server.login(username,password)
        server.sendmail(username,destination,msg)  
        server.quit()      
        print "Successfully sent email"
	#except:
	   #print "Error: unable to send email"	

send_snow(2.0)
