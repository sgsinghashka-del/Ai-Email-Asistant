# ✉️ AI Email Assistant

A portfolio-ready GenAI application that uses Gemini and Streamlit to improve, rewrite, summarize, and generate email replies.

## Features

- Improve grammar and clarity
- Rewrite emails
- Generate replies
- Summarize emails
- Select email purpose
- Select tone
- Select output length
- Input validation
- API error handling
- Secure API-key management
- Modular prompt and Gemini client layers
- Unit tests

## Architecture

```text
User
  ↓
Streamlit UI
  ↓
Input Validation
  ↓
Prompt Engine
  ↓
Gemini Client
  ↓
Gemini API
  ↓
Generated Email
```

## Project Structure

```text
AI_Email_Assistant/
├── app.py
├── src/
│   ├── gemini_client.py
│   ├── prompt_engine.py
│   └── utils.py
├── tests/
│   ├── test_prompt_engine.py
│   └── test_utils.py
├── .streamlit/
│   └── secrets.toml.example
├── screenshots/
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup on Windows

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create the secrets file:

```cmd
copy .streamlit\secrets.toml.example .streamlit\secrets.toml
```

Open it:

```cmd
notepad .streamlit\secrets.toml
```

Add your NEW Gemini API key.

Run:

```cmd
streamlit run app.py
```

## Run Tests

```cmd
pytest
```

## Security

Never commit `.streamlit/secrets.toml` or API keys to GitHub.

If an API key has previously been exposed in source code or a public repository, revoke/rotate it and use a new key.

## Portfolio Improvements

Future extensions can include email subject generation, copy-to-clipboard support, response history, user authentication, analytics, model selection, and deployment monitoring.


## Deploy to Google Cloud Run

This project is containerized for Cloud Run. Google Cloud also supports deploying Streamlit from source, but the Dockerfile makes the runtime configuration explicit and reproducible. See the official Cloud Run Streamlit quickstart: https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-streamlit-service

### 1. Install and authenticate Google Cloud CLI

```cmd
gcloud auth login
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

Verify:

```cmd
gcloud config get-value project
```

### 2. Enable required services

```cmd
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com
```

### 3. Create a dedicated Cloud Run service account

```cmd
gcloud iam service-accounts create ai-email-run \
  --display-name="AI Email Assistant Cloud Run"
```

Grant it permission to read the Gemini API secret:

```cmd
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:ai-email-run@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

### 4. Create the Gemini API secret

Create a NEW Gemini API key. Do not reuse a key that was previously exposed in source code.

```cmd
gcloud secrets create gemini-api-key --replication-policy="automatic"
```

Add the key as a secret version:

```cmd
gcloud secrets versions add gemini-api-key --data-file="gemini_key.txt"
```

Delete the local key file after creating the secret:

```cmd
del gemini_key.txt
```

### 5. Deploy to Cloud Run

From the project root:

```cmd
gcloud run deploy ai-email-assistant \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --service-account ai-email-run@YOUR_PROJECT_ID.iam.gserviceaccount.com \
  --set-secrets GEMINI_API_KEY=gemini-api-key:1
```

Cloud Run will build and deploy the application and return a service URL.

### Security note

Google recommends Secret Manager for sensitive values such as API keys rather than storing them directly in source code or ordinary environment variables. Cloud Run can expose a Secret Manager secret to the container as an environment variable. Use a dedicated service account with `Secret Manager Secret Accessor` permission.

### GitHub deployment workflow

Recommended repository flow:

```text
Local project
    ↓
GitHub
    ↓
Google Cloud Run
    ↓
Public Streamlit URL
```

Do not commit:

```text
.streamlit/secrets.toml
.env
gemini_key.txt
```

The `.gitignore` and `.dockerignore` files are configured to exclude secrets and local development files.
