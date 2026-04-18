from langchain_huggingface import ChatHuggingFaceEndpoint
from dotenv import load_dotenv      
load_dotenv()
llm = ChatHuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/gpt2",
    headers={"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_ACCESS_TOKEN')}"}
)          
response = llm.invoke("What is the capital of France?")
print(response.content) 