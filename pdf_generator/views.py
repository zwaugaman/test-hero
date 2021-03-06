from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.core.files import File
from os import remove
from django_boto.s3 import upload


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    response.write(pdf)
    buffer.close()

    with open('/tmp/hello.world', 'w') as f:
        myfile = File(f)
        myfile.write('Hello World')
        upload(myfile, "test")



    return response



class button_view(TemplateView):
    template_name = 'pdf_generator/form.html'

