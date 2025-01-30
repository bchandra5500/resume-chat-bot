import os
from chatbot import RAGChatbot

def main():
    resume_path = os.path.join(os.path.dirname(__file__), os.getenv("RESUME_NAME"))
    
    print("Resume ChatBot Initialized. Type 'quit' to exit.")
    print(f"Using resume: {resume_path}")
    print("-" * 50)
    
    try:
        chatbot = RAGChatbot(resume_path)
        
        while True:
            user_input = input("\nType Your Question Here: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nGoodbye!")
                break
            if user_input:
                response = chatbot.chat(user_input)
                print("\nResume ChatBot Response:", response)
                
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
