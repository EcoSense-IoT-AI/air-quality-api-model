# Air Quality Prediction API 🌍💨

This project provides a REST API built with **FastAPI** to predict air quality status (Good/Poor) using a **Random Forest Classifier**. It processes environmental data such as CO2 levels, PM2.5, temperature, and humidity.

## 🚀 Key Features

- **Machine Learning Integration**: Uses a Scikit-learn Random Forest model trained on environmental sensor data.
- **RESTful API**: Fast and modern API powered by FastAPI.
- **Data Validation**: Robust request validation using Pydantic.
- **Containerized**: Ready-to-deploy Docker configuration.
- **Auto-Documentation**: Interactive API docs available via Swagger UI.

---

## 🛠 Technology Stack

- **Language**: Python 3.10+
- **API Framework**: FastAPI
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Server**: Uvicorn
- **Containerization**: Docker

---

## 📂 Project Structure

```text
air-quality-api-model/
├── main.py                # FastAPI application & endpoints
├── train_model.py         # Script to generate/train the ML model
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
├── model_air_quality.joblib # Trained model (generated after training)
└── .gitignore             # Files to ignore in Git
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd air-quality-api-model
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model 🧠
This step is **mandatory** before running the API, as it generates the `.joblib` model file.
```bash
python train_model.py
```
*You should see a message: `Modèle entraîné et sauvegardé ✅`*

---

## 🚦 How to Run

### Locally with Uvicorn
```bash
uvicorn main:app --reload --port 8000
```
Open your browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the interactive Swagger documentation.

---

## 🐳 Docker Deployment

To run the application inside a Docker container:

### 1. Build the Image
```bash
docker build -t air-quality-api .
```

### 2. Run the Container
```bash
docker run -p 7860:7860 air-quality-api
```
The API will be accessible at `http://localhost:7860`.

---

## 🧪 Usage Example

### Request
You can test the prediction endpoint by sending a POST request to `/predict`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "co2": 450,
  "pm25": 12,
  "temp": 22,
  "hum": 40
}'
```

### Response
```json
{
  "prediction": 0,
  "probability": [0.98, 0.02]
}
```
*Note: `0` typically represents "Good Air Quality" and `1` represents "Poor Air Quality" based on the training logic.*


