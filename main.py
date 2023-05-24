import qrcode
 
# Title
print("\nQr Code Generator!\n")
 
# Generate
link = input("Paste your link here: ")
qr_code = qrcode.make(link)
qr_code.show()
print("Done!")
 
