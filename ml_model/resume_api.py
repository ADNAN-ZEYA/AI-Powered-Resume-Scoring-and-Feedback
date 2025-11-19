from flask import Flask, request, jsonify
import joblib
import traceback

app = Flask(__name__)

# Load the model
model = joblib.load("model/resume_score_model.pkl")

@app.route('/')
def home():
    return "Resume Score API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Create input as DataFrame
        input_data = {
            "Skills": [data["skills"]],
            "Experience (Years)": [data["experience"]],
            "Education": [data["education"]],
            "Certifications": [data["certifications"]],
            "Projects Count": [data["projects"]],
            "Salary Expectation ($)": [data["salary"]]
        }

        import pandas as pd
        input_df = pd.DataFrame.from_dict(input_data)

        # Predict score
        score = model.predict(input_df)[0]

        return jsonify({
            "score": round(score, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
