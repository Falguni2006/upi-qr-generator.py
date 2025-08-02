import qrcode

#Taking upi Id as a input
upi_id = input ("entre your UPI ID")

#upi://pay?pa=UPI_IDpn=NAME&am=account&cu=CURRENCY&tn=MESSAGE

#defining the pyment url based on the upi id and the pyment app
#you can modity these urls based on the pyment apps you wnat to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cm=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cm=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cm=1234'

#create or code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr to image file(optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#display the qr codes (you may need to install pil/pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()