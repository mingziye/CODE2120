from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import urllib
import requests
from PIL import Image
from colorthief import ColorThief
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

class DominantColors:

	CLUSTERS = None
	IMAGE = None
	COLORS = None
	LABELS = None
	
	def __init__(self, image, clusters=3):
		self.CLUSTERS = clusters
		self.IMAGE = image
		
	def dominantColors(self):
	
		#read image
		img = cv2.imread(self.IMAGE)
		
		#convert to rgb from bgr
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				
		#reshaping to a list of pixels
		img = img.reshape((img.shape[0] * img.shape[1], 3))
		
		#save image after operations
		self.IMAGE = img
		
		#using k-means to cluster pixels
		kmeans = KMeans(n_clusters = self.CLUSTERS)
		kmeans.fit(img)
		
		#the cluster centers are our dominant colors.
		self.COLORS = kmeans.cluster_centers_
		
		#save labels
		self.LABELS = kmeans.labels_
		
		#returning after converting to integer from float
		return self.COLORS.astype(int)


@csrf_exempt
def domcol(request):
			
	log = []
	jsob = {"clusters": 3,"path": 0}
	if request.method == "POST":
		try: 
			data = request.POST["data"]
			print(data)
			received = json.loads(str(data))
			jsob.update(received)
			path = jsob.get("path")
			clusters = int(jsob.get("clusters"))
			dc = DominantColors(path, clusters) 
			colors = dc.dominantColors().tolist()
			print(colors)
			print(type(colors))


			
			results = {"colors":colors}

			return JsonResponse(results)
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		 	return HttpResponse("lkafewa;gjkreagfne")




@csrf_exempt
def domcoll(request,var_c):
			
	log = []
	jsob = {"clusters": 5,"path": 0}
	if request.method == "POST":
		try: 

			data = request.POST["data"]
			print(data)
			received = json.loads(str(data))
			jsob.update(received)
			path = jsob.get("path")
			clusters = jsob.get("clusters")
			tmp_file = 'tmp.jpg'
			urllib.request.urlretrieve(path,filename=tmp_file)
			color_thief = ColorThief(tmp_file)
			dominant_color = color_thief.get_color(quality=1) #one colour
			palette = color_thief.get_palette(color_count=int(clusters)) #multiple
			print(dominant_color)
			print(palette)

			results = {"colors":palette}

			return JsonResponse(results)
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		 	return HttpResponse("やっとできた、めっちゃ信じられない")
