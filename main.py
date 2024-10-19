from llama_index.llms.ollama import Ollama
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


class Character():
    def __init__(self,data_folder:str):
        self.index = self._get_index(data_folder)
        self.chat_engine = self._get_chat_engine()



    def _get_index(self,data_folder:str,embed_model='../NanoScience/embed_model;'):
           
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en",cache_folder=embed_model) # index from disk 
        data = SimpleDirectoryReader(input_dir=data_folder).load_data()
        print(data_folder)
        return VectorStoreIndex.from_documents(documents= data,embed_model=embed_model)
    
    def _get_chat_engine(self):
        llm = Ollama(model='llama3',request_timeout = 180,device='cuda') 

        return self.index.as_chat_engine(chat_mode = 'context',llm=llm,system_prompt="You are the character as specified in the given context and you will chat like that")

    def get_response(self,message:str):
        
        return self.chat_engine.chat(message)



if __name__ == "__main__":
    character1 = Character(data_folder="./character1")
    character2 = Character(data_folder="./character2")
    initial_message = "Hi"
    response1 = character1.get_response(f"your boyfriend is saying: {initial_message}")
    while True:
        print("Boyfriend"+"*"*90)   
        response2 = character2.get_response(f"your girlfriend is saying: {response1}" )
        print(response2)
        print("Girlfriend"+"*"*90)
        response1 = character1.get_response(f"your boyfriend is saying: {response2}")
        print(response1)





