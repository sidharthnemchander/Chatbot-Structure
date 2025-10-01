from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain_community.vectorstores import FAISS as faiss
from langchain.text_splitter import TokenTextSplitter
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
import torch
import numpy as np

def Embeddings(blog_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 50
    )

    splits = text_splitter.split_documents(blog_docs)
    db = Chroma.from_documents(documents = splits  ,embeddings = OpenAIEmbeddings())

    return db



def Embeddings_Fixed(blog_docs):
    text_splitter = TokenTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    
    full_text = " ".join(blog_docs)
    splits = text_splitter.split_text(full_text)

    tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
    model = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")

    encoded_input = tokenizer(
        splits, 
        padding=True, 
        truncation=True, 
        return_tensors="pt"
    )
    
    with torch.no_grad():
        embeddings = model(**encoded_input).pooler_output

    embeddings_np = embeddings.cpu().numpy()

    dimension = embeddings_np.shape[1]
    
    db = faiss.IndexFlatIP(dimension)
    db.add(embeddings_np) 

    return db
