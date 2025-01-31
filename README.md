# AI Resume Chatbot (Backend)

Live Demo: [https://bharat-resume-chat-bot-widget.onrender.com](https://bharat-resume-chat-bot-widget.onrender.com)

A Flask-based AI chatbot service that uses LangChain and OpenAI to provide intelligent responses about my professional experience, powered by my resume.

## Architecture

- **Framework**: Flask (Python)
- **AI Integration**:
  - LangChain for orchestrating the conversation flow
  - OpenAI's GPT models for natural language processing
  - PDF parsing for resume data ingestion
- **Deployment**: Render.com web service
- **API Endpoints**:
  - `/chat`: Main conversation endpoint
  - `/health`: Service health check

## Project Structure

```
resume_chatbot/
├── main.py           # Flask application entry
├── chatbot.py        # Core chatbot logic
├── system_prompt.txt # AI system instructions
└── resume.pdf        # Source resume document
```

## Local Development

1. **Environment Setup**

   ```bash
   # Install pipenv if not installed
   pip install pipenv

   # Install dependencies
   pipenv install

   # Copy environment template
   cp .env_template .env
   ```

2. **Configure Environment**

   ```
   OPENAI_API_KEY=your_key_here
   RESUME_NAME=resume.pdf
   FLASK_ENV=development
   ```

3. **Run the Server**
   ```bash
   pipenv run dev
   ```
   Server runs on http://localhost:5001

## Technology Stack

- **Python 3.11**: Core language
- **Flask**: Web framework
- **LangChain**: LLM framework
- **OpenAI GPT**: Language model
- **PyPDF2**: PDF processing
- **CORS**: Cross-origin support

## Workflow

1. Client sends chat message to `/chat` endpoint
2. Message is processed by LangChain pipeline
3. Context from resume is retrieved and formatted
4. OpenAI generates appropriate response
5. Response is returned to client

This service is designed to be highly responsive and scalable, with built-in error handling and rate limiting.
