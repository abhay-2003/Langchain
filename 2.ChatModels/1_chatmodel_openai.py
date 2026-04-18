from langchain import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
chat = ChatOpenAI(model="gpt-4")
result =chat.invoke("What is the capital of France?")
print(result)