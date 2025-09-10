import qrcode

#Taaking UPI ID As a input
upi_id = input("Enter your UPI ID =")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#definingthe payment URL based on the UPI ID and the payment app
#you can modify these URLS based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for each payment app
phonepe_url = qrcode.make(phonepe_url)
paytm_url = qrcode.make(paytm_url)
google_pay_url = qrcode.make(google_pay_url)

#save the QR code to image file (optinal)
phonepe_url.save('phonepe_qr.png')
paytm_url.save('paytm_qr.png')
google_pay_url.save('google_pay_url')

#Display the QR codes (you may need to install PIL/pillow library)
phonepe_url.show() 
paytm_url.show()
google_pay_url.show()