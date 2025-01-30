import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

class RAGChatbot:
    def __init__(self, resume_path: str):
        """
        Initialize the chatbot with a path to a resume PDF file.
        
        Args:
            resume_path (str): Path to the resume PDF file
        """
        if not os.path.exists(resume_path):
            raise FileNotFoundError(f"Resume file not found: {resume_path}")
            
        # Load and process the resume PDF
        self.resume_content = self._load_resume(resume_path)
        
        # Initialize OpenAI model
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY", "")
        )
        
        # Create the chat prompt
        system_message = self._get_system_prompt(os.getenv("SYSTEM_PROMPT_PATH", ""))

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        
        # Set up memory
        self.memory = ConversationBufferMemory(
            return_messages=True
        )
        
        # Create the chain
        self.chain = self.prompt | self.llm
    
    def _get_system_prompt(self, system_prompt_path: str) -> str: 
        if not os.path.exists(system_prompt_path):
            raise FileNotFoundError(f"System prompt file not found: {system_prompt_path}")

        with open(system_prompt_path, "r") as file:
            system_prompt_template = file.read().strip()
        
        # Format the template with resume content
        return system_prompt_template.format(resume_content=self.resume_content)
        
    def _load_resume(self, pdf_path: str) -> str:
        """
        Load and extract text from a PDF resume file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text content from the PDF
        """
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error loading PDF: {str(e)}")

    def chat(self, user_input: str) -> str:
        """
        Process user input and return the chatbot's response
        
        Args:
            user_input (str): User's question about the resume
            
        Returns:
            str: Chatbot's response based on resume content
        """
        try:
            # Get chat history
            history = self.memory.load_memory_variables({})["history"]
            
            # Generate response
            response = self.chain.invoke({
                "history": history,
                "input": user_input
            })
            
            # Save interaction to memory
            self.memory.save_context(
                {"input": user_input},
                {"output": response.content}
            )
            
            return response.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"
