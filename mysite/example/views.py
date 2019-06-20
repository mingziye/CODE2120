from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import sys, os

# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s:%s " %("Mindy", "died"),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_codse.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			jsob = {"demo":"32","var":"The count is "}
			data = request.POST["data"]

			received = json.loads(str(data))

			jsob.update(received)

			index= 0
			for i in jsob["demo"]:
				index += 1

			m = int(jsob['n1']) * int(jsob['n2'])
			s = int(jsob['n1']) + int(jsob['n2'])

			results = {"sum": s, "mult":m}
			return JsonResponse(results)
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("it works")



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