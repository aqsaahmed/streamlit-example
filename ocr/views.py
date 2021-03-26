from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from PIL import Image as Processor
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def index(request):
	if request.method == "POST":
		img_processor = request.FILES["img"]
		if img_processor:
			objct = Image(image = img_processor)
			objct.save()
			processed_image = Processor.open(str(objct.image.url[1:]))
			text = pytesseract.image_to_string(processed_image)
			res = text.split()
			key = []
			value = []

			length = int(len(res)/2)
			for i in range(0,length):
				key.append(res[i])
				value.append(res[i+length])

			dictionary = dict(zip(key, value))
			print(dictionary)
			return render(request, "home.html", {'dictionary': dictionary})
		else:
			print("error")
			return HttpResponse("No image")
	else:
		return render(request, "home.html")
