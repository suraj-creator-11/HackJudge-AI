# HackJudge AI

**AI-powered hackathon evaluation with customizable judging rubrics, GitHub repository analysis, and human review.**

HackJudge AI helps hackathon organizers evaluate projects consistently using organizer-defined criteria, repository evidence, AI-assisted assessments, and transparent weighted scoring.

## 1. What We Built

HackJudge AI is a web application where organizers define judging criteria and evaluators submit a project's GitHub repository URL, with an optional live-demo URL.

The application aims to collect project evidence, assess it against the rubric, calculate a weighted score, and support human review.

### Key Features

- Customizable judging criteria and weights
- GitHub repository URL submission
- Optional live-demo URL
- Repository evidence inspection
- AI-assisted criterion-level assessments
- Weighted scoring
- Human score overrides with reasons, where supported
- Evaluation dashboard and leaderboard

## 2. Gemma 4 Integration

**Model:** `gemma-4-26b-a4b-it`

**API:** Google Gemini API  
**API base URL:** `https://generativelanguage.googleapis.com/v1beta/openai`

HackJudge AI is designed to use Google's Gemma 4 model through the Gemini API's OpenAI-compatible endpoint.

### How Gemma 4 Is Used

1. An evaluator submits a public GitHub repository URL.
2. HackJudge AI collects available repository evidence, such as README content, source files, tests, dependencies, CI configuration, and license information.
3. The configured Gemma 4 model assesses the available evidence against the organizer's judging criteria.
4. The application presents criterion-level assessments and calculates a weighted score.
5. Human judges review the results and can override scores with a reason where supported.

Gemma 4 is intended to perform meaningful evaluation work rather than act as a decorative chatbot. Human judges remain responsible for final decisions.

**Important:** The model identifier and API configuration must be verified against the actual working integration. Do not claim a successful live Gemma 4 call until it has been tested.

## 3. Tech Stack

- Backend: Python and Flask
- Frontend: HTML, CSS, and JavaScript
- AI: Google Gemini API with the configured Gemma 4 model
- Testing: pytest

See `requirements.txt` for dependencies.

## 4. Installation and Setup

### Requirements

- Python 3.10 or newer recommended
- Git
- Internet connection
- Gemini API key for live AI assessment

### Step 1: Clone the Repository

```bash
git clone https://github.com/suraj-creator-11/HackJudge-AI.git
cd HackJudge-AI
```

### Step 2: Create a Virtual Environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure the Gemini API

Copy `.env.example` to `.env`.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
notepad .env
```

Configure the appropriate environment variables:

```env
AI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai
AI_API_KEY=YOUR_GEMINI_API_KEY
AI_MODEL=gemma-4-26b-a4b-it
```

Use the exact variable names expected by the application's configuration and `.env.example`.

Never publish your real API key. Keep `.env` private.

### Step 5: Run the Application

On Windows PowerShell:

```powershell
.\start.ps1
```

Alternatively, run the Flask application using the startup command specified by the project configuration.

Open the local address printed by the application.

## 5. How to Use HackJudge AI

1. Open the application.
2. Create or select a hackathon event.
3. Configure judging criteria and their weights.
4. Submit a public GitHub repository URL.
5. Add a live-demo URL if available.
6. Run the evaluation.
7. Review the collected evidence and AI assessment.
8. Inspect the final weighted score.
9. Use the human-review workflow where available.

## 6. Hackathon Submission — Best Use of Gemma 4

**Intended track: Best Use of Gemma 4**

HackJudge AI is intended for this track because Gemma 4 supports the core project-evaluation workflow by assessing repository evidence against customizable judging criteria.

### Four Steps Before Submission

**01 — Wire Up Gemma 4**

Configure the Gemini API and verify a real model call that performs meaningful rubric-based project assessment.

**02 — Write the README**

Explain what was built, how to run it, and explicitly name the Gemma model used. This README documents those details.

**03 — Submit Once for the Team**

One teammate submits through the event's OrganizerHQ Challenges page before the deadline and selects **Best Use of Gemma 4**. Follow the event instructions to submit to one track only.

**04 — Demo on the Floor**

Show the integration, not just the output. Be prepared to explain which model was called, what evidence it received, and what work it performed.

Check the organizer's latest instructions for the submission deadline and requirements.

## 7. Suggested Live Demo

1. Create an event and configure custom judging criteria.
2. Submit a public GitHub repository URL.
3. Show the repository evidence collected by the application.
4. Trigger the Gemma 4 assessment.
5. Show the criterion-level results.
6. Explain how the final weighted score is calculated.
7. Demonstrate human review and a justified score override, if available.

### Demo Checklist

- [ ] The application starts successfully.
- [ ] Organizers can configure judging criteria.
- [ ] Evaluators can submit a GitHub repository.
- [ ] Repository evidence is displayed.
- [ ] A real Gemini API request reaches the configured Gemma 4 model.
- [ ] The model returns a meaningful assessment.
- [ ] Weighted scoring works correctly.
- [ ] Human review works as described.
- [ ] No API key or secret is exposed.

Do not present mock output or fallback results as a successful live Gemma 4 integration.

## 8. Testing

Run the project's tests with:

```bash
pytest
```

A passing test suite does not, by itself, prove that the live Gemini API integration works. Test the actual model call separately.

## 9. Security and Responsible Evaluation

- Never commit `.env` or API keys.
- Keep `.env.example` free of real credentials.
- Treat repository content as untrusted input.
- Missing repository files should not automatically be treated as proof of poor project quality.
- Keep human judges responsible for final decisions.
- Follow the applicable terms for models, APIs, and dependencies.

## 10. Project Structure

```text
HackJudge-AI/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── start.ps1
├── LICENSE
├── README.md
├── static/
│   ├── app.js
│   └── styles.css
├── templates/
│   └── index.html
└── tests/
    └── test_app.py
```

The local SQLite database should not be committed to the public repository.

## 11. License

This project is distributed under the MIT License. See the `LICENSE` file.

## 12. GitHub Repository

https://github.com/suraj-creator-11/HackJudge-AI
