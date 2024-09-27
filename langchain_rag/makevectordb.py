from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import LanceDB
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

INPUT = "out.json"
OUTPUT = "vectorsdb"

def main():
    print("loading docs")
    docs = JSONLoader(INPUT, ".[].rawtext").load()
    docs = sorted(docs, key=lambda d: len(d.page_content))

    print("loading splits")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10, separator="")
    splits = text_splitter.split_documents(docs)

    print(f"{len(docs)} docs -> {len(splits)} splits")

    print("loading model")
    embed_model = HuggingFaceEmbeddings(model_name="dangvantuan/sentence-camembert-large", show_progress=True)

    print("making db")
    db = LanceDB.from_documents(splits, embed_model, uri=OUTPUT)
    
if __name__ == "__main__":
    main()
