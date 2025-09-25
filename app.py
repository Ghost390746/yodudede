from fastapi import FastAPI
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq, pipeline
from datasets import load_dataset

app = FastAPI()

# Load AI Models
processor = AutoProcessor.from_pretrained("DanGalt/openai-finetuned-minds14")
model = AutoModelForSpeechSeq2Seq.from_pretrained("DanGalt/openai-finetuned-minds14")

# Example dataset: ChatGPT prompts
chat_prompts = load_dataset("fka/awesome-chatgpt-prompts")

# Example dataset: Bhagavad Gita
gita = load_dataset("JDhruv14/Bhagavad-Gita_Dataset")

@app.get("/")
def home():
    return {"message": "AI Backend Running!"}

@app.get("/prompts")
def get_prompts():
    return chat_prompts["train"][:5]

@app.get("/gita")
def get_gita():
    return gita["train"][:5]
