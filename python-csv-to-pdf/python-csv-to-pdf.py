#https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
import pdfkit
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_file(r'C:\Users\hidek\Downloads\Manserv\asdasd.html',r'C:\Users\hidek\Downloads\Manserv\asdasd.pdf', configuration=config)
