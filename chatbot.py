import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

class RAGChatbot:
    def __init__(self):
        # Initialize OpenAI model
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Define the system prompt
        template = """You are a helpful AI assistant. You aim to provide accurate and helpful responses while being direct and concise.

Current conversation:
{history}
Human: {input}
Assistant:"""
        
        # Set up conversation memory
        self.memory = ConversationBufferMemory(return_messages=True)
        
        # Create the conversation chain
        self.prompt = PromptTemplate(
            input_variables=["history", "input"], 
            template=template
        )
        
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt,
            verbose=False
        )

    def chat(self, user_input: str) -> str:
        """
        Process user input and return the chatbot's response
        """
        try:
            response = self.conversation.predict(input=user_input)
            return response.strip()
        except Exception as e:
            return f"Error: {str(e)}"
