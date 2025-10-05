# 💰 Loan Default Prediction App

A simple Streamlit web app to predict whether a loan will default based on applicant details using a trained machine learning model.

---

## 📝 Project Description

This app allows users to input loan-related data like **Applicant Income, Loan Amount, and Term** and predicts if the loan will default. It also shows the **default probability**.

The app is built using **Python, Streamlit, Pandas, and scikit-learn**.

---

## 📺 Demo

**Run the app locally**:  
Open a terminal and run:

```bash
streamlit run app.py
After running, you will see:

Local URL: http://localhost:8501

Network URL: http://<your-network-ip>:8501

Click the Local URL to open the app in your browser.

Example:

yaml
Copy code
Applicant Income: 80000
Loan Amount: 50000
Term: 12
Prediction: ✅ Loan will NOT Default
⚙️ Features
Input applicant details (Income, Loan Amount, Term)

Predict loan default (Yes/No)

Show default probability

User-friendly interface

🛠 Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/loan-default-prediction.git
Navigate to the project folder:

bash
Copy code
cd loan-default-prediction
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the environment:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/Mac:

bash
Copy code
source venv/bin/activate
Install required libraries:

bash
Copy code
pip install -r requirements.txt
🚀 How to Run
bash
Copy code
streamlit run app.py
Then open the Local URL displayed in your terminal.

💻 Technologies Used
Python 3.x

Streamlit

Pandas

scikit-learn

joblib

