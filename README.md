# HackJudge AI

**Evidence-led hackathon judging with custom rubrics, GitHub repository inspection, optional demo checks, AI assessments, a leaderboard, and auditable human overrides.**

This is a deliberately compact MVP for a short hackathon build. It uses one Flask service, a SQLite database, and a static frontend—no Node build, Docker, Clerk, or separate microservices required.

## What works

- Create multiple hackathons with a track, description, custom criteria and percentage weights that must total exactly 100%.
- Add mandatory requirements; assessment reports whether each was verified, not verified, or not met when AI is configured.
- Submit team/project name, a GitHub repository URL, optional live demo URL, and notes.
- Collect GitHub repository metadata, README, tracked file paths, a bounded set of source/manifests/tests/CI/deployment files, license metadata, and latest commit metadata.
- Inspect a public demo's HTTP reachability and limited visible text. This does **not** verify interactive functionality.
- Use an OpenAI-compatible chat-completions endpoint for criterion-by-criterion evaluation when configured.
- Validate model criterion names and scores; calculate the weighted final score on the server, not by trusting a model-provided total.
- If no model is configured, use a clearly labelled **structural baseline**. It is not represented as AI judgement and must not be treated as a competition verdict.
- Dashboard/leaderboard, evidence details, risks/missing evidence, and human score overrides with a required reason and audit log.
- SQLite persistence. Repository code is read as data and is never executed.

## Run on Windows PowerShell

Open PowerShell in the extracted `HackJudge-AI` folder.

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python app.py
```

If PowerShell blocks virtual-environment activation, you can skip activation and use the venv's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open **http://127.0.0.1:5000**. You can also run `./start.ps1` from PowerShell; it creates the environment and installs dependencies before starting the app.

Run the local unit tests with `python -m unittest discover -s tests -v` after installing dependencies.

## Configure AI assessment

The app expects an **OpenAI-compatible chat completions API**. Providers differ in endpoint, model availability, authentication and request format; use the exact endpoint and model identifier supported by the provider you choose.

Edit `.env`:

```dotenv
AI_BASE_URL=https://YOUR-PROVIDER-BASE-URL/v1
AI_API_KEY=your_key_here
AI_MODEL=your_provider_model_id
```

The app appends `/chat/completions` unless that suffix is already present. Restart the Flask server after changing `.env`. Do not put provider keys in frontend JavaScript or commit `.env` to GitHub. **Do not assume a model name works without checking the provider's current model list and making a test request.**

Optional GitHub token (use only a token with the minimum required access):

```dotenv
GITHUB_TOKEN=your_github_token
```

Unauthenticated public GitHub API access is rate-limited. A token helps with rate limits and can access private repositories only if the token is actually authorised for them. Keep tokens secret.

## Suggested 8-hour build/demo plan

1. **Hour 1:** install, launch, create a hackathon and validate the rubric.
2. **Hours 2–3:** submit 2–3 public repositories; confirm collected files and evidence.
3. **Hour 4:** configure and test the selected AI provider; verify JSON response handling and weighted scoring.
4. **Hour 5:** inspect criterion rationales, missing evidence and optional demo results.
5. **Hour 6:** test score override and audit history; compare leaderboard rankings.
6. **Hour 7:** test failure cases (invalid repo, private repo without token, unreachable demo, missing AI configuration).
7. **Hour 8:** prepare a short demo and explain limitations honestly.

## API overview

- `GET /api/health` — app and AI configuration status
- `GET /api/hackathons` — list programs
- `POST /api/hackathons` — create hackathon
- `GET /api/hackathons/<id>` — hackathon and rubric
- `GET /api/hackathons/<id>/submissions` — leaderboard submissions
- `POST /api/submissions` — collect evidence and assess
- `GET /api/submissions/<id>` — evidence, assessment and audit trail
- `POST /api/submissions/<id>/override` — set final score (0–100), reason required

## Security and limitations

- Never execute participant code or install dependencies from a submission.
- GitHub evidence is bounded by file count and content length. Large monorepos and unusual project layouts may have incomplete inspection.
- GitHub repository metadata and file contents are untrusted. Model instructions explicitly treat repo contents as evidence, not instructions, but prompt injection cannot be eliminated completely.
- Demo checks block non-public DNS/IP destinations, reject nonstandard ports, and do not follow redirects. For production use, perform URL fetching in a hardened egress-restricted service to further mitigate DNS rebinding and network edge cases.
- This MVP has no login/role-based access control. Run locally for a hackathon demo; do not expose it to the public internet with real submissions without adding authentication, authorisation, rate limiting, stronger isolation, and privacy controls.
- The optional AI API call may send submitted notes and collected public repository text to the configured model provider. Disclose this to participants and check the provider's data policies.
- Scores are decision support, not objective truth. Keep human judges in control and document rubric calibration.
- If the AI call fails, the submission remains visible as `ASSESSMENT_ERROR` and receives no fabricated score.

## License

This fresh implementation is provided under the MIT License; see `LICENSE`.
