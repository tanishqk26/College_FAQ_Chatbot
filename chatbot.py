import json
from transformers import pipeline

# Load the question-answering model
model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Load FAQ data
with open("faq_data.json", "r") as file:
    faq_data = json.load(file)

def get_answer(question):
    # Combine all answers into a single context for simplicity
    context = " ".join([item["answer"] for item in faq_data])
    
    # Get the answer from the model
    result = model(question=question, context=context)
    return result["answer"]

# Test the function
if __name__ == "__main__":
    user_question = input("Ask a question: ")
    print("Answer:", get_answer(user_question))
