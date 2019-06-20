from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

import json
import urllib3
from PIL import Image
import cv2
from sklearn.cluster import KMeans
from .models import *
import sys, os

# Create your views here.
@csrf_exempt
def fib(request):
	log = []
	jsob = {"startNumber": 0,"length":10}
	if request.method == "POST":
		try:
			
			data = request.POST["data"]

			received = json.loads(str(data))

			jsob.update(received)

			#custom below

			startNumber = int(jsob["startNumber"])
			length 		= int(jsob["length"])
			loop		= range(length)

			numarray	= []

			fibno		= startNumber
			addno		= 1

			for l in loop:
				numarray.append(fibno)
				fibno = fibno+addno
				addno = fibno-addno


			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)


@csrf_exempt
def multification(request):
	log = []
	jsob = {"n1": 0,"n2": 0}
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(str(data))
			jsob.update(received)

			#start writing code here:
			#for i in jsob['n1']:
			#	index += 1

			m = int(jsob['n1']) * int(jsob['n2'])
			s = int(jsob['n1']) + int(jsob['n2'])
			d =	int(jsob['n1']) / int(jsob['n2'])
			results = {"sum": s, "mult":m, "division":d}
			return JsonResponse(results)
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("Only return post request")
	
@csrf_exempt

def picker(request):
	log = []
	if request.method == "POST":
		try: 
			data = request.POST["data"]
			im 	 = Image.open(data)
			width, height = im.size
			size = {"width":width,"height":height}
			return JsonResponse(size)
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("Only return post request")

def DominantColors(request):

			
    log = []
    jsob = {"clusters": 3,"path": 0}
    if request.method == "POST":
        try: 
                data = request.POST["data"]
                received = json.loads(str(data))
                jsob.update(received)

                im  = cv2.imread(jsob.get("path"))
                im  = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                #reshape the image to a list of pixels.
                im = im.reshape((im.shape[0] * im.shape[1], 3))
                

                kmeans = KMeans(n_clusters = int(jsob.get("clusters")))
                kmeans.fit(im)
                
                COLORS = kmeans.cluster_centers_
                LABELS = kmeans.labels_
                clusters = int(jsob.get("clusters"))
                dc = DominantColors(im, clusters) 
                colors = dc.dominantColors()

                red = int(colors[0])
                green = int(colors[1])
                blue = int(colors[2])
                results = {"r":red,"g":green,"b":blue}

                return JsonResponse(results)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
    	 return HttpResponse("see, you can't make any change to gh, so silly")

        


