from pdfjinja import PdfJinja


mypdf = PdfJinja('sydjango3.pdf')
pdfout = mypdf({'name': 'yoongie', 'sydney': True, 'address': 'test address', 'language': 'javascript'})
with open('filled.pdf', 'wb') as f:
    pdfout.write(f)
