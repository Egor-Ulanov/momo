from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'main/index.html')

from transformers import pipeline

# Define the pipeline outside the function for efficiency (load model once)
pipe = pipeline("text-classification", model="sismetanin/rubert-toxic-pikabu-2ch")

from django.http import JsonResponse
from django.shortcuts import render
from transformers import pipeline

def cluster_text(text):
    # Load the clustering pipeline
    cluster_pipe = pipeline("cluster", model="facebook/bart-base")

    # Cluster the text
    clusters = cluster_pipe(text)

    # Extract and return cluster labels for each sentence
    sentence_clusters = []
    for cluster in clusters:
        sentence_clusters.extend(cluster["labels"])

    return sentence_clusters


def classify_comment(request):
  if request.method == 'GET':
    text = request.GET.get('text')
    if text:
      # Use the pre-defined pipeline for classification
      prediction = pipe(text)

      # Extract the label and score from the prediction
      label = prediction[0]['label']  # Assuming the first element contains the label
      score = prediction[0]['score']  # Assuming the first element contains the score

      # Prepare the response data (you can customize this)
      response_data = {
          'label': label,
          'score': score
      }

      return JsonResponse(response_data)  # Return JSON response for AJAX
    else:
      return JsonResponse({'error': 'No text provided'})  # JSON error response
  else:
    return JsonResponse({'error': 'Invalid request method'})  # JSON error response
