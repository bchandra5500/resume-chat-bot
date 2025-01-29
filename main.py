from chatbot import RAGChatbot

def main():
    print("Resume ChatBot Initialized. Type 'quit' to exit.")
    print("-" * 50)
    
    chatbot = RAGChatbot()
    
    while True:
        user_input = input("\nType Your Question Here: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("\nGoodbye!")
            break
            
        if user_input:
            response = chatbot.chat(user_input)
            print("\nResume ChatBot Response:", response)

if __name__ == "__main__":
    main()
