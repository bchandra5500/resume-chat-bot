# AI-Powered Resume Chatbot

An intelligent chatbot that provides precise, technical insights about your resume. Built with LangChain and OpenAI, it analyzes PDF resumes and responds to queries with focused, impact-driven answers highlighting technical expertise and achievements.

## Features

- **PDF Resume Processing**: Automatically extracts and processes content from PDF resumes
- **Context-Aware Responses**: Provides technically focused answers emphasizing:
  - Engineering expertise and system design decisions
  - Performance metrics and scalability achievements
  - Technical leadership and innovation
  - Quantifiable business impact
- **Intelligent Memory**: Maintains conversation context for natural follow-up questions
- **Professional Tone**: Delivers sharp, technical responses focused on engineering excellence

## Prerequisites

- Python 3.10+
- OpenAI API key
- PDF resume file
- Basic understanding of markdown (for customizing system prompt)

## Required Files

1. **Resume PDF**

   - Your resume in PDF format
   - Recommended: Clear formatting for better text extraction
   - Place in project root directory

2. **system_prompt.txt**
   - Controls chatbot's personality and response style
   - Written in markdown format
   - Default prompt optimized for technical responses
   - Sections:
     - Role: Defines chatbot's persona
     - Task: Specifies response objectives
     - Specifics: Detailed response guidelines
     - Examples: Good/bad response examples
     - Notes: Additional response criteria

## Setup

1. Install pipenv if not already installed:

```bash
pip install pipenv
```

2. Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd resume_chatbot
pipenv install
```

3. Configure environment variables:

```bash
cp .env_template .env
```

4. Edit `.env` file with your settings:

```
OPENAI_API_KEY=your_api_key_here
RESUME_NAME=your_resume.pdf  # Name of your PDF resume file
```

5. Set up required files:

   a. Add your resume:

   - Place your resume PDF file in the project directory
   - Update RESUME_NAME in .env to match your PDF filename

   b. Configure system prompt:

   - Ensure `system_prompt.txt` exists in the project directory
   - This file defines the chatbot's behavior and response style
   - Default prompt is optimized for technical, impact-driven responses
   - You can customize the prompt to change the chatbot's response style

## Usage

1. Start the chatbot:

```bash
pipenv run python main.py
```

2. Ask questions about the resume, for example:

- "What is the technical stack and expertise?"
- "Describe the most impactful engineering projects"
- "What are the key achievements at Capital One?"

3. Type 'quit' or 'exit' to end the session

## Example Interactions

```
Q: "What is the technical expertise?"
A: "Expert in high-performance data engineering: Built mission-critical ETL pipelines
with Python/PySpark, achieving 40% faster processing. Architected scalable cloud
solutions using AWS Lambda/EMR, handling 1000+ daily requests with 99.9% uptime."

Q: "Describe the most significant project impact"
A: "Led development of a third-party SaaS catalog serving 1000+ daily requests,
centralizing cybersecurity operations through automated approvals and metadata
management. Engineered with Python/AWS Lambda, ensuring 99.9% availability through
cross-region failover."
```

## Technical Implementation

- **Framework**: LangChain for conversation management and LLM integration
- **PDF Processing**: PyPDF2 for resume content extraction
- **Language Model**: OpenAI GPT-3.5 Turbo
- **Conversation Management**: Implements memory for context-aware responses
- **System Prompts**: Engineered for technical precision and impact focus

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
