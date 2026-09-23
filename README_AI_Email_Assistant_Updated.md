# 🤖 AI Email Assistant

An AI-powered email writing assistant built with **Python, Streamlit, and Google Gemini**.

The application helps users improve, rewrite, summarize, or generate email content based on the selected **email purpose, tone, and length**.

---

## 📸 Application Preview

### Email Improvement

![Email Improvement](screenshots/01_email_improvement.png)

### Rewrite

![Rewrite Email](screenshots/02_email_rewrite.png)

### Generate Reply

![Generate Reply](screenshots/03_generate_reply.png)

> Screenshots demonstrate the local Streamlit application and its different email-generation workflows.

---

## 🚀 Project Overview

Writing professional emails can take time, especially when the user needs to adjust grammar, tone, structure, or level of detail.

This project provides a simple AI-powered interface where a user can:

- Enter an email or email-related instruction
- Select the purpose of the email
- Select the desired tone
- Select the preferred response length
- Choose an AI action
- Generate an improved or rewritten result

The application uses **Google Gemini** to generate the final email content.

---

## ✨ Key Features

### 📧 Multiple Email Purposes

- General
- Job Application
- Follow-up
- Meeting Request
- Leave Request
- Customer Support
- Complaint
- Business

### 🎯 Multiple Tones

- Professional
- Formal
- Friendly
- Casual
- Persuasive
- Apologetic

### 🛠️ Multiple AI Actions

- **Improve** — improves grammar, clarity, and structure
- **Rewrite** — rewrites the email while preserving its intended meaning
- **Generate Reply** — creates a suitable reply based on the provided content
- **Summarize** — creates a concise version of the provided email

### 📏 Response Length

- Short
- Medium
- Detailed

### 🔐 API Key Security

The Gemini API key is not stored in the source code.

The application reads credentials from environment variables or Streamlit secrets. The real `.streamlit/secrets.toml` file is excluded from Git using `.gitignore`.

### ✅ Input Validation

The project validates email input before sending it to the AI model and handles invalid or empty input gracefully.

### ⚠️ Error Handling

AI/API failures are handled through user-friendly error messages.

### 🧪 Automated Tests

Tests cover prompt generation and input validation.

---

## 🏗️ Project Architecture

```text
AI Email Assistant
│
├── Streamlit UI
│   └── app.py
│
├── Prompt Engineering
│   └── src/prompt_engine.py
│
├── Gemini API Client
│   └── src/gemini_client.py
│
├── Input Validation
│   └── src/utils.py
│
├── Automated Tests
│   └── tests/
│
├── Configuration
│   ├── .streamlit/secrets.toml.example
│   ├── requirements.txt
│   └── pytest.ini
│
└── Containerization
    ├── Dockerfile
    └── .dockerignore
```

---

## 📂 Project Structure

```text
AI_Email_Assistant/
│
├── app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── LICENSE
├── README.md
├── pytest.ini
├── requirements.txt
│
├── .streamlit/
│   └── secrets.toml.example
│
├── src/
│   ├── __init__.py
│   ├── gemini_client.py
│   ├── prompt_engine.py
│   └── utils.py
│
└── tests/
    ├── test_prompt_engine.py
    └── test_utils.py
```

---

## 🔄 Application Workflow

```text
User enters email
        │
        ▼
Select email purpose
        │
        ▼
Select tone
        │
        ▼
Select response length
        │
        ▼
Select AI action
        │
        ▼
Prompt Engine
        │
        ▼
Google Gemini
        │
        ▼
Generated Email
        │
        ▼
Display result in Streamlit
```

---

## 🧠 Prompt Engineering

The project uses a structured prompt instead of sending the user's input directly to Gemini.

The prompt incorporates:

- Email purpose
- Desired tone
- Desired length
- Selected action
- Original user input

It also includes safeguards to preserve the intended meaning and avoid unnecessarily inventing unsupported information.

Prompt construction is separated from the Streamlit UI, making the application easier to maintain and test.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| Google Gemini | Generative AI |
| `google-genai` | Gemini API integration |
| Pytest | Automated testing |
| Docker | Containerization |
| Git | Version control |
| GitHub | Source-code hosting |

---

## ⚙️ Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/sgsinghashka-del/Ai-Email-Asistant.git
cd Ai-Email-Asistant
```

### 2. Create a virtual environment

Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```cmd
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Do **not** commit this file to GitHub.

The repository contains:

```text
.streamlit/secrets.toml.example
```

as a safe configuration template.

### 5. Run the application

```cmd
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🧪 Run Tests

From the project root:

```cmd
pytest
```

You can also use:

```cmd
python -m pytest
```

The project includes tests for prompt construction and input validation.

---

## 🐳 Docker Support

The project includes a Dockerfile and is ready to be containerized.

Build the image:

```bash
docker build -t ai-email-assistant .
```

Run the container:

```bash
docker run -p 8501:8080 ai-email-assistant
```

For production deployment, provide the Gemini API key through the hosting platform's secret/environment-variable mechanism rather than putting the key into the image.

---

## ☁️ Deployment

The project is **Docker-ready and cloud-deployment ready**.

It can be deployed to a suitable cloud/container platform such as Google Cloud Run or another Docker-compatible hosting service.

> **Current status:** The application is developed and tested locally and uploaded to GitHub. A live cloud deployment is not currently claimed.

This keeps the repository accurate while retaining the Docker configuration required for future deployment.

---

## 🔐 Security Notes

Never commit:

```text
.env
.streamlit/secrets.toml
API keys
service-account JSON files
```

The repository's `.gitignore` excludes local secrets.

For deployment, use the hosting provider's secret-management or environment-variable facility.

If an API key is accidentally exposed publicly, revoke/rotate it immediately.

---

## 💡 Example Use Cases

### Job Application
Transform a basic job-related message into a professional application email.

### Leave Request
Generate a structured leave request with the selected tone and level of detail.

### Customer Support
Rewrite a customer message into a clearer and more professional response.

### Meeting Request
Create a concise meeting request with an appropriate professional tone.

### Business Communication
Improve business emails while preserving the original intent.

### Follow-up Email
Create a professional follow-up after an interview, meeting, or previous communication.

---

## 📈 What This Project Demonstrates

This project demonstrates practical skills in:

- Generative AI application development
- Gemini API integration
- Prompt engineering
- Streamlit application development
- Modular Python architecture
- Input validation
- Error handling
- Automated testing
- Secret management
- Docker containerization
- Git/GitHub workflow

---

## 🔮 Future Improvements

- Conversation/history support
- User authentication
- Copy-to-clipboard functionality
- Download generated emails as `.txt` or `.docx`
- Email provider integration
- Response quality evaluation
- Usage/token tracking
- Prompt versioning
- Model selection
- Production monitoring
- Cloud deployment
- Automated CI/CD with GitHub Actions

---

## 👨‍💻 Author

**Ashka Singh**

GitHub:  
https://github.com/sgsinghashka-del

---

## 📄 License

This project is licensed under the MIT License.
