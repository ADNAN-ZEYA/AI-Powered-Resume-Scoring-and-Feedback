# AI-Powered Resume Scoring and Feedback

A small project that scores resumes and returns feedback using a machine-learning model. The repository contains a Node.js front-end/server and Python code for training and serving the ML model.

**Project Structure**
- `package.json` - Node project metadata and scripts (if present).
- `server.js` - Node server / backend entrypoint.
- `public/` - Front-end static files (`index.html`, `app.js`, `style.css`).
- `app.js`, `index.html`, `style.css` - client-side app and styles.
- `ml_model/` - Python code and data for training and serving the model.
  - `AI_Resume_Screening.csv` - training dataset (example input data).
  - `train_model.py` - script to train the model.
  - `resume_api.py` - lightweight API to serve the trained model.
  - `model/` - folder where trained model artifacts are stored.
- `uploads/` - folder used to hold uploaded resumes (used by the server/app).

**Features**
- Score resumes using an ML model (scikit-learn or similar).
- Provide basic feedback and a normalized score.
- Web UI (static) to upload resumes and view results.
- Python scripts to train or retrain the model.

**Requirements**
- Node.js (14+ recommended) and `npm`.
- Python 3.8+ for ML scripts and API.
- Common Python packages: `pandas`, `scikit-learn`, `flask` (or `fastapi`/`uvicorn`) depending on `ml_model/resume_api.py` implementation.

Note: If a `requirements.txt` or `pyproject.toml` is present, install from it instead of the generic package list below.

**Quick Start — Node (frontend/server)**
1. Install Node dependencies:

```powershell
cd "e:\projects\AI-Powered Resume Scoring and Feedback"
npm install
```

2. Start the Node server (if `server.js` is the entrypoint):

```powershell
node server.js
```

3. Open the UI in your browser at `http://localhost:3000` (adjust port if `server.js` uses a different port). Check `server.js` for the actual port number and available routes.

**Quick Start — Python (model API & training)**
1. Create and activate a virtual environment (PowerShell):

```powershell
cd "e:\projects\AI-Powered Resume Scoring and Feedback\ml_model"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install Python packages (if `requirements.txt` exists):

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not present, install common deps:

```powershell
pip install pandas scikit-learn flask
```

3. Run the model API (serves predictions):

```powershell
python resume_api.py
```

4. Train or retrain the model:

```powershell
python train_model.py
```

Training reads `AI_Resume_Screening.csv` and should write artifacts into `model/` (see `train_model.py` for specifics).

**API / Integration**
- The repository may expose an HTTP endpoint for scoring resumes — check `server.js` and `ml_model/resume_api.py` to confirm exact endpoint paths and port numbers.
- Example (replace URL/endpoint with the real one from `server.js`):

```powershell
curl -X POST -F "resume=@C:\path\to\resume.pdf" http://localhost:3000/api/score
```

Or call the Python model API directly (if it exposes an endpoint on port 5000):

```powershell
curl -X POST -F "resume=@C:\path\to\resume.pdf" http://localhost:5000/score
```

**Configuration & Notes**
- Review `server.js` to see how the Node server invokes the Python model (if it does) and the expected payload.
- Ensure `uploads/` is writable by the server process.
- If the ML API uses a different server (e.g., FastAPI + Uvicorn), consult `ml_model/resume_api.py` for the correct run command.

**Adding a `requirements.txt` (recommended)**
If you plan to use the Python model commonly, create `ml_model/requirements.txt` with pinned versions, for example:

```
pandas==1.5.3
scikit-learn==1.2.2
flask==2.2.3
joblib==1.2.0
```

Then install with `pip install -r requirements.txt`.

**Development Tips**
- Use virtual environments for Python work to avoid dependency conflicts.
- Add `.gitignore` entries for `ml_model/.venv/`, `uploads/`, and trained model artifacts in `ml_model/model/` if not intended for version control.
- If you change the ML model/data, retrain using `train_model.py` and verify via `resume_api.py`.

**File map (summary)**
- `server.js` — Node server
- `package.json` — Node dependencies & scripts
- `public/` — Front-end static assets
- `ml_model/AI_Resume_Screening.csv` — training data
- `ml_model/train_model.py` — training script
- `ml_model/resume_api.py` — Python model server
- `ml_model/model/` — saved model artifacts
- `uploads/` — uploaded resumes

**Contributing**
- Fork and create a branch for your feature or fix.
- Add/adjust tests if applicable and update `README.md` with any new setup steps.
- Open a pull request with a clear description of changes.

**License**
This repository does not include a license file. If you want to make it open-source, consider adding an `MIT` license or another license that fits your needs.

**Contact / Author**
For questions or help, open an issue in this repository or contact the maintainer.
