import pdfkit
#pdfkit.from_url('http://www.google.com', 'micro.pdf')
options = {
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0.2in',
    'margin-left': '0in',
   'footer-center': '[page] of [topage]'
}
pdfkit.from_file('report.html', 'report.pdf', options=options)
pdfkit.from_file('reportSummary.html', 'reportSummary.pdf', options=options)