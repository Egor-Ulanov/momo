from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .stable_difussion import generate



def main(request):
    return render(request, 'main/index.html')


def run_neural_network(request):
    generate()
    return JsonResponse({'success': True})
    # return render(request, 'main/index.html')



