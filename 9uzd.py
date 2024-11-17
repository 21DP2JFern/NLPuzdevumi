from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
text = "Reiz kādā tālā zemē..."
generated_text = generator(text, max_length=50, num_return_sequences=1)
print(generated_text[0]['generated_text'])