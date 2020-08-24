import pdfkit
#pdfkit.from_url('http://www.google.com', 'micro.pdf')
options = {
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0.2in',
    'margin-left': '0in',
    'footer-center': '[page] of [topage]',
    'enable-local-file-access':''
}
#pdfkit.from_file('report.html', 'report.pdf', options=options)
#pdfkit.from_file('reportSummary.html', 'reportSummary.pdf', options=options)
#pdfkit.from_file('fullReport.html', 'reportSummary.pdf', options=options)
#pdfkit.from_file('reportDynamic.html', 'reportDynamic.pdf', options=options)
#pdfkit.from_url('http://localhost:4996/report?project_id=3e44a57fb1d5497c94da7e2533663594', 'reportDynamic.pdf', options=options)
#file:///Users/faher/Desktop/Projects.html
pdfkit.from_url('demo2.html', 'report.pdf', options=options)
