# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="sismetanin/rubert-toxic-pikabu-2ch")

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("sismetanin/rubert-toxic-pikabu-2ch")
model = AutoModelForSequenceClassification.from_pretrained("sismetanin/rubert-toxic-pikabu-2ch")

# Example usage:
comment = "Только идиот мог такое придумать"  # Replace with your comment
prediction = pipe(comment)

print(prediction)  # Output: [{'label': 'toxic', 'score': 0.98}]