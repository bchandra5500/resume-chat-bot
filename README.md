# Resume Chatbot Backend

A Flask-based backend service that powers the AI resume chatbot.

## Deployment Instructions (Render.com)

1. Create a Render account at https://render.com

2. Connect your GitHub repository to Render:

   - Go to Dashboard
   - Click "New +"
   - Select "Web Service"
   - Choose your repository
   - Select the branch to deploy

3. Configure the service:

   - Name: `resume-chatbot-api` (or your preferred name)
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Add environment variables:
     - `RESUME_NAME`: `resume.pdf`
     - `FLASK_ENV`: `production`

4. Click "Create Web Service"

Your API will be available at `https://your-service-name.onrender.com`

## Environment Variables

Copy `.env_template` to `.env` and fill in the required values:

```
RESUME_NAME=resume.pdf
FLASK_ENV=development  # or production
```

## Local Development

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python main.py
```

The server will run on http://localhost:5001
