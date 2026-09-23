# ✉️ AI Email Assistant

An AI-powered Streamlit application that helps users improve, rewrite, summarize, and generate replies to email content with Google Gemini. Choose the email purpose, tone, response length, and action, then review the generated result beside the original message.

## 📸 Application preview

The screenshots below reflect the current Streamlit interface and the repository's available workflows.

### Rewrite email

![AI Email Assistant — rewrite workflow](screenshot/Email%20improver%20Rewrite.png)

### Generate a reply

![AI Email Assistant — generate reply workflow](screenshot/generate%20reply%20email%20improver.png)

### Summarize email

![AI Email Assistant — summarize workflow](screenshot/summaise%20email%20improver.png)

> Screenshots are stored in [`screenshot/`](screenshot/) and show the local application UI. Run the app locally to create a fresh screenshot with your own Gemini response.

## ✨ Features

- **Four AI actions:** Improve, Rewrite, Generate Reply, and Summarize
- **Eight email purposes:** General, Job Application, Follow-up, Meeting Request, Leave Request, Customer Support, Complaint, and Business
- **Six tones:** Professional, Formal, Friendly, Casual, Persuasive, and Apologetic
- **Three response lengths:** Short, Medium, and Detailed
- **Side-by-side workflow:** Enter the original email on the left and view the generated result on the right
- **Structured prompting:** The prompt engine preserves the user's intended meaning and tells Gemini not to invent names, dates, companies, promises, credentials, or other facts
- **Input validation:** Empty, very short, and over-sized inputs are rejected before an API request is made
- **Friendly error handling:** Missing credentials, API failures, and empty model responses are surfaced in the Streamlit UI
- **Secret-safe configuration:** Credentials are loaded from `GEMINI_API_KEY` or Streamlit secrets and are excluded from Git
- **Automated tests:** Pytest coverage for prompt construction and validation behavior
- **Docker support:** The included image serves Streamlit on port `8080`

## 🏗️ Architecture and request flow

```text
User input and controls
          │
          ▼
      app.py (Streamlit UI)
          │
          ├── validate_email(...) ── reject invalid input
          │
          └── build_prompt(...) ──── assemble guarded prompt
                                      │
                                      ▼
                           improve_email(...) in
                           src/gemini_client.py
                                      │
                                      ▼
                              Google Gemini API
                                      │
                                      ▼
                              Generated result
```

The UI entry point is [`app.py`](app.py). It collects the email text and user controls, validates the input, builds a structured prompt through [`src/prompt_engine.py`](src/prompt_engine.py), and calls the cached Gemini client in [`src/gemini_client.py`](src/gemini_client.py). Validation rules live in [`src/utils.py`](src/utils.py), keeping the UI, prompt construction, API integration, and tests separated.

## 📂 Project structure

```text
.
├── app.py                         # Streamlit application entry point
├── src/
│   ├── gemini_client.py           # Gemini client and model call
│   ├── prompt_engine.py           # Action, tone, length, and safety prompt
│   └── utils.py                   # Input validation
├── tests/
│   ├── test_prompt_engine.py      # Prompt behavior tests
│   └── test_utils.py              # Validation tests
├── screenshot/                    # Current UI screenshots
├── .streamlit/
│   └── secrets.toml.example       # Local secret configuration template
├── Architecture Diagram           # Text architecture reference
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configuration
├── Dockerfile                      # Container image definition
└── README.md
```

## 🛠️ Tech stack

| Technology | Role |
| --- | --- |
| Python 3.13 | Application runtime |
| Streamlit | Web UI and secret management |
| `google-genai` | Google Gemini API client |
| Gemini `gemini-3.6-flash` | Text generation model configured by the app |
| Pytest | Automated tests |
| Docker | Containerized deployment |

## 🚀 Run locally

### 1. Clone and install

```bash
git clone https://github.com/sgsinghashka-del/Ai-Email-Asistant.git
cd Ai-Email-Asistant
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### 2. Configure Gemini

Copy the template:

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Then set a valid key in `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

The application also accepts `GEMINI_API_KEY` as an environment variable, which is the preferred approach for hosted deployments. Never commit the real secrets file or an API key.

### 3. Start Streamlit

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

## 🧪 Run tests

```bash
pytest
```

The test suite verifies that:

- prompts include the selected purpose, tone, length, and input;
- prompts include the no-invented-facts instruction;
- empty and overly short inputs are rejected;
- inputs over 12,000 characters are rejected; and
- valid input passes validation.

## 🐳 Run with Docker

Build the image:

```bash
docker build -t ai-email-assistant .
```

Run it on local port `8501`:

```bash
docker run --rm -p 8501:8080 \\
  -e GEMINI_API_KEY="YOUR_GEMINI_API_KEY" \\
  ai-email-assistant
```

Then open [http://localhost:8501](http://localhost:8501). The Docker image runs `streamlit run app.py` on `0.0.0.0:8080`. For production, inject the key through the hosting provider's secret manager rather than baking it into the image.

## 🔐 Security notes

- Keep `.streamlit/secrets.toml`, `.env` files, API keys, and service-account JSON files out of version control.
- Rotate a key immediately if it is exposed.
- Treat generated email text as model output and review it before sending.
- The prompt explicitly asks Gemini to preserve meaning and avoid fabricating unsupported facts, but users should still verify the final result.

## 📌 Current scope and future improvements

The repository currently provides a local, Docker-ready Streamlit application; it does not claim a live hosted deployment. Potential next steps include conversation history, authentication, copy/download actions, email-provider integration, model selection, usage tracking, response-quality evaluation, monitoring, and CI/CD.

## 👤 Author

**Ashka Singh** — [@sgsinghashka-del](https://github.com/sgsinghashka-del)

## 📄 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).
