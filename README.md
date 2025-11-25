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
- Python packages: `pandas`, `scikit-learn`, `fastapi`, `uvicorn`, `joblib`, `numpy`, `matplotlib` (see `ml_model/requirements.txt`).

Note: Always install from `ml_model/requirements.txt` to ensure all dependencies are properly pinned.

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

2. Install Python packages:

```powershell
pip install -r requirements.txt
```

3. Run the model API using Uvicorn (serves predictions on port 8000):

```powershell
uvicorn resume_api:app --reload
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for interactive API documentation.

4. Train or retrain the model:

```powershell
python train_model.py
```

Training reads `AI_Resume_Screening.csv` and saves artifacts into `model/`.

5. (Optional) Run comprehensive model evaluation and testing:

```powershell
python test.py
```

This generates evaluation metrics (`model_metrics.json`), feature importances (`top_feature_importances.csv`), and residual plots (`model_residuals.png`).

**API / Integration**
The Node.js server on `localhost:3000` calls the Python FastAPI model server running on `localhost:8000`.

**FastAPI Model Server** (runs on port 8000):
- Root: `GET http://localhost:8000/` — health check
- Predict: `POST http://localhost:8000/predict` — score a resume

Example request to FastAPI:
```powershell
$body = @{
    skills = "Python, React, AWS"
    experience = 5
    education = "B.Tech"
    certifications = "AWS Certified"
    projects = 8
    salary = 80000
} | ConvertTo-Json

curl -X POST http://localhost:8000/predict `
  -H "Content-Type: application/json" `
  -d $body
```

Or visit `http://localhost:8000/docs` for interactive Swagger UI documentation.

**Configuration & Notes**
- The Node server (`server.js`) expects the FastAPI model server to be running at `http://localhost:5000/predict`.
- Ensure `uploads/` is writable by the server process.
- The ML model uses FastAPI + Uvicorn for async request handling and automatic API documentation.
- Model is trained using scikit-learn's RandomForestRegressor with a ColumnTransformer pipeline.

**Python Dependencies** (`ml_model/requirements.txt`)
All Python dependencies are pinned to specific versions:
- `numpy==1.26.4` — numerical computing
- `pandas==2.0.3` — data manipulation
- `scikit-learn==1.2.2` — ML algorithms
- `joblib==1.3.2` — model serialization
- `matplotlib==3.8.0` — visualization
- `fastapi==0.110.0` — API framework
- `uvicorn==0.29.0` — ASGI server

**Development Tips**
- Use virtual environments for Python work to avoid dependency conflicts.
- Add `.gitignore` entries for `ml_model/.venv/`, `uploads/`, and trained model artifacts in `ml_model/model/` if not intended for version control.
- If you change the ML model/data, retrain using `train_model.py` and verify via `resume_api.py`.

**File map (summary)**
- `server.js` — Node.js server (port 3000)
- `package.json` — Node.js dependencies & scripts
- `public/` — Front-end static assets (HTML, CSS, JS)
- `ml_model/` — Python ML module
  - `AI_Resume_Screening.csv` — training dataset
  - `train_model.py` — model training script
  - `resume_api.py` — FastAPI model server (port 8000)
  - `test.py` — comprehensive model evaluation & testing
  - `requirements.txt` — Python dependencies
  - `model/` — saved model artifacts
  - `model_metrics.json` — evaluation metrics (generated by test.py)
  - `model_residuals.png` — residual plot (generated by test.py)
  - `top_feature_importances.csv` — feature importances (generated by test.py)
- `uploads/` — uploaded resumes (server-generated)

**Contributing**
- Fork and create a branch for your feature or fix.
- Add/adjust tests if applicable and update `README.md` with any new setup steps.
- Open a pull request with a clear description of changes.

**License**
This repository does not include a license file. If you want to make it open-source, consider adding an `MIT` license or another license that fits your needs.

**Contact / Author**
For questions or help, open an issue in this repository or contact the maintainer.
