# AI-Based Exam Anxiety Detector

An intelligent mental-wellness support system designed to identify and categorize exam-related anxiety from student-generated text inputs.

## Project Architecture
- **Presentation Layer:** Streamlit Frontend (`frontend/app.py`)
- **Application Layer:** FastAPI Backend (`backend/main.py`), BERT Classifier
- **Data Layer:** Prepared Datasets, Preprocessing Scripts

## Setup Instructions

1. **Activate Virtual Environment:**
   ```bash
   # Windows
   .\venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Backend API:**
   ```bash
   uvicorn backend.main:app --reload --port 8000
   ```

4. **Run Frontend Application:**
   ```bash
   streamlit run frontend/app.py
   ```
