import pdfkit
#pdfkit.from_url('http://www.google.com', 'micro.pdf')
options = {
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
}
pdfkit.from_file('report.html', 'report.pdf', options=options)