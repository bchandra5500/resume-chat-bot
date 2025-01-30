# Resume Chatbot Backend

A Flask-based backend service that powers the AI resume chatbot.

## Deployment Instructions (Railway)

1. Create a Railway account at https://railway.app

2. Install Railway CLI:

```bash
npm i -g @railway/cli
```

3. Login to Railway:

```bash
railway login
```

4. Initialize Railway project:

```bash
railway init
```

5. Add environment variables in Railway dashboard:

- `RESUME_NAME`: Your resume file name (e.g. resume.pdf)
- `FLASK_ENV`: Set to "production"
- Upload your resume file to the project directory

6. Deploy to Railway:

```bash
railway up
```

7. Get your deployment URL from Railway dashboard. You'll need this URL for the frontend configuration.

## Environment Variables

Copy `.env_template` to `.env` and fill in the required values:

```
RESUME_NAME=your-resume.pdf
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
