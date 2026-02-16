# Load document from Text File

from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the text file
with open("./docs/mlk.txt", "rt") as f:
    content = f.read() 

text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=500,
      chunk_overlap=50)

chunks = text_splitter.split_text(content)

print('Chunks Count :', len(chunks))
