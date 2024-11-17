import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"


cleaned_text = re.sub(r'http\S+|@\S+|#\S+|[^a-zA-Zāčēģīķļņōŗšūž\s]', '', text.lower())
print(cleaned_text.strip())