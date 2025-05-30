import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="AI Disease Prediction Suite",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- HIDE STREAMLIT DEFAULTS ----
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stButton>button {background-color: #4F8BF9; color: white;}
    .result-card {background: #222; color: #fff; padding: 1em; border-radius: 10px; margin: 1em 0;}
    </style>
""", unsafe_allow_html=True)

# ---- BACKGROUND IMAGE ----
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.7);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- LOAD MODELS ----
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# ---- SIDEBAR MENU ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616494.png", width=80)
    st.title("AI Disease Suite")
    selected = option_menu(
        menu_title="Choose Prediction",
        options=[
            "Diabetes",
            "Heart Disease",
            "Parkinson's",
            "Lung Cancer",
            "Hypo-Thyroid"
        ],
        icons=["droplet-half", "heart-pulse", "person", "lungs", "activity"],
        menu_icon="hospital",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "icon": {"color": "#4F8BF9", "font-size": "22px"},
            "nav-link-selected": {"background-color": "#4F8BF9", "color": "white"},
        }
    )

def input_row(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1) if type == "number" else st.text_input(label, key=key, help=tooltip)

def show_result(message, success=True):
    color = "#27ae60" if success else "#c0392b"
    st.markdown(
        f'<div class="result-card" style="background:{color};color:white;">{message}</div>',
        unsafe_allow_html=True
    )

# ---- DIABETES ----
if selected == "Diabetes":
    st.header("🩸 Diabetes Prediction")
    st.info("Enter the following details to predict diabetes risk.")
    Pregnancies = input_row('Number of Pregnancies', 'Times pregnant', 'Pregnancies')
    Glucose = input_row('Glucose Level', 'Glucose level', 'Glucose')
    BloodPressure = input_row('Blood Pressure', 'Blood pressure', 'BloodPressure')
    SkinThickness = input_row('Skin Thickness', 'Skin thickness', 'SkinThickness')
    Insulin = input_row('Insulin Level', 'Insulin level', 'Insulin')
    BMI = input_row('BMI', 'Body Mass Index', 'BMI')
    DiabetesPedigreeFunction = input_row('Diabetes Pedigree Function', 'Genetic risk', 'DiabetesPedigreeFunction')
    Age = input_row('Age', 'Age', 'Age')
    if st.button('Predict Diabetes'):
        pred = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        msg = '🟢 The person is diabetic.' if pred[0] == 1 else '🟢 The person is not diabetic.'
        show_result(msg, pred[0] == 1)

# ---- HEART DISEASE ----
elif selected == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    st.info("Enter the following details to predict heart disease risk.")
    age = input_row('Age', 'Age', 'age')
    sex = input_row('Sex (1=male, 0=female)', 'Sex', 'sex')
    cp = input_row('Chest Pain Type (0-3)', 'Chest pain type', 'cp')
    trestbps = input_row('Resting BP', 'Resting blood pressure', 'trestbps')
    chol = input_row('Serum Cholesterol', 'Serum cholesterol', 'chol')
    fbs = input_row('Fasting Blood Sugar > 120mg/dl (1/0)', 'Fasting blood sugar', 'fbs')
    restecg = input_row('Resting ECG (0-2)', 'Resting ECG', 'restecg')
    thalach = input_row('Max Heart Rate', 'Maximum heart rate', 'thalach')
    exang = input_row('Exercise Induced Angina (1/0)', 'Exercise angina', 'exang')
    oldpeak = input_row('ST Depression', 'ST depression', 'oldpeak')
    slope = input_row('Slope (0-2)', 'Slope', 'slope')
    ca = input_row('Major Vessels (0-3)', 'Major vessels', 'ca')
    thal = input_row('Thal (0=normal, 1=fixed, 2=reversible)', 'Thal', 'thal')
    if st.button('Predict Heart Disease'):
        pred = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        msg = '🟢 The person has heart disease.' if pred[0] == 1 else '🟢 The person does not have heart disease.'
        show_result(msg, pred[0] == 1)

# ---- PARKINSON'S ----
elif selected == "Parkinson's":
    st.header("🧠 Parkinson's Disease Prediction")
    st.info("Enter the following details to predict Parkinson's disease risk.")
    fields = [
        ('MDVP:Fo(Hz)', 'fo'), ('MDVP:Fhi(Hz)', 'fhi'), ('MDVP:Flo(Hz)', 'flo'),
        ('MDVP:Jitter(%)', 'Jitter_percent'), ('MDVP:Jitter(Abs)', 'Jitter_Abs'),
        ('MDVP:RAP', 'RAP'), ('MDVP:PPQ', 'PPQ'), ('Jitter:DDP', 'DDP'),
        ('MDVP:Shimmer', 'Shimmer'), ('MDVP:Shimmer(dB)', 'Shimmer_dB'),
        ('Shimmer:APQ3', 'APQ3'), ('Shimmer:APQ5', 'APQ5'), ('MDVP:APQ', 'APQ'),
        ('Shimmer:DDA', 'DDA'), ('NHR', 'NHR'), ('HNR', 'HNR'),
        ('RPDE', 'RPDE'), ('DFA', 'DFA'), ('Spread1', 'spread1'),
        ('Spread2', 'spread2'), ('D2', 'D2'), ('PPE', 'PPE')
    ]
    inputs = [input_row(label, label, key) for label, key in fields]
    if st.button("Predict Parkinson's"):
        pred = models['parkinsons'].predict([inputs])
        msg = "🟢 The person has Parkinson's disease." if pred[0] == 1 else "🟢 The person does not have Parkinson's disease."
        show_result(msg, pred[0] == 1)

# ---- LUNG CANCER ----
elif selected == "Lung Cancer":
    st.header("🫁 Lung Cancer Prediction")
    st.info("Enter the following details to predict lung cancer risk.")
    GENDER = input_row('Gender (1=Male, 0=Female)', 'Gender', 'GENDER')
    AGE = input_row('Age', 'Age', 'AGE')
    SMOKING = input_row('Smoking (1=Yes, 0=No)', 'Smoking', 'SMOKING')
    YELLOW_FINGERS = input_row('Yellow Fingers (1=Yes, 0=No)', 'Yellow fingers', 'YELLOW_FINGERS')
    ANXIETY = input_row('Anxiety (1=Yes, 0=No)', 'Anxiety', 'ANXIETY')
    PEER_PRESSURE = input_row('Peer Pressure (1=Yes, 0=No)', 'Peer pressure', 'PEER_PRESSURE')
    CHRONIC_DISEASE = input_row('Chronic Disease (1=Yes, 0=No)', 'Chronic disease', 'CHRONIC_DISEASE')
    FATIGUE = input_row('Fatigue (1=Yes, 0=No)', 'Fatigue', 'FATIGUE')
    ALLERGY = input_row('Allergy (1=Yes, 0=No)', 'Allergy', 'ALLERGY')
    WHEEZING = input_row('Wheezing (1=Yes, 0=No)', 'Wheezing', 'WHEEZING')
    ALCOHOL_CONSUMING = input_row('Alcohol Consuming (1=Yes, 0=No)', 'Alcohol consuming', 'ALCOHOL_CONSUMING')
    COUGHING = input_row('Coughing (1=Yes, 0=No)', 'Coughing', 'COUGHING')
    SHORTNESS_OF_BREATH = input_row('Shortness Of Breath (1=Yes, 0=No)', 'Shortness of breath', 'SHORTNESS_OF_BREATH')
    SWALLOWING_DIFFICULTY = input_row('Swallowing Difficulty (1=Yes, 0=No)', 'Swallowing difficulty', 'SWALLOWING_DIFFICULTY')
    CHEST_PAIN = input_row('Chest Pain (1=Yes, 0=No)', 'Chest pain', 'CHEST_PAIN')
    if st.button("Predict Lung Cancer"):
        pred = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        msg = "🟢 The person has lung cancer." if pred[0] == 1 else "🟢 The person does not have lung cancer."
        show_result(msg, pred[0] == 1)

# ---- HYPOTHYROID ----
elif selected == "Hypo-Thyroid":
    st.header("🦋 Hypo-Thyroid Prediction")
    st.info("Enter the following details to predict hypo-thyroid risk.")
    age = input_row('Age', 'Age', 'age')
    sex = input_row('Sex (1=Male, 0=Female)', 'Sex', 'sex')
    on_thyroxine = input_row('On Thyroxine (1=Yes, 0=No)', 'On thyroxine', 'on_thyroxine')
    tsh = input_row('TSH Level', 'TSH level', 'tsh')
    t3_measured = input_row('T3 Measured (1=Yes, 0=No)', 'T3 measured', 't3_measured')
    t3 = input_row('T3 Level', 'T3 level', 't3')
    tt4 = input_row('TT4 Level', 'TT4 level', 'tt4')
    if st.button("Predict Hypo-Thyroid"):
        pred = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        msg = "🟢 The person has Hypo-Thyroid disease." if pred[0] == 1 else "🟢 The person does not have Hypo-Thyroid disease."
        show_result(msg, pred[0] == 1)

# ---- FOOTER ----
st.markdown(
    "<hr><center>⚕️ <b>AI Disease Prediction Suite</b> | Powered by Streamlit & scikit-learn</center>",
    unsafe_allow_html=True
)
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="AI Disease Prediction Suite",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- HIDE STREAMLIT DEFAULTS ----
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stButton>button {background-color: #4F8BF9; color: white;}
    .result-card {background: #222; color: #fff; padding: 1em; border-radius: 10px; margin: 1em 0;}
    </style>
""", unsafe_allow_html=True)

# ---- BACKGROUND IMAGE ----
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.7);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- LOAD MODELS ----
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# ---- SIDEBAR MENU ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616494.png", width=80)
    st.title("AI Disease Suite")
    selected = option_menu(
        menu_title="Choose Prediction",
        options=[
            "Diabetes",
            "Heart Disease",
            "Parkinson's",
            "Lung Cancer",
            "Hypo-Thyroid"
        ],
        icons=["droplet-half", "heart-pulse", "person", "lungs", "activity"],
        menu_icon="hospital",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "icon": {"color": "#4F8BF9", "font-size": "22px"},
            "nav-link-selected": {"background-color": "#4F8BF9", "color": "white"},
        }
    )

def input_row(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1) if type == "number" else st.text_input(label, key=key, help=tooltip)

def show_result(message, success=True):
    color = "#27ae60" if success else "#c0392b"
    st.markdown(
        f'<div class="result-card" style="background:{color};color:white;">{message}</div>',
        unsafe_allow_html=True
    )

# ---- DIABETES ----
if selected == "Diabetes":
    st.header("🩸 Diabetes Prediction")
    st.info("Enter the following details to predict diabetes risk.")
    Pregnancies = input_row('Number of Pregnancies', 'Times pregnant', 'Pregnancies')
    Glucose = input_row('Glucose Level', 'Glucose level', 'Glucose')
    BloodPressure = input_row('Blood Pressure', 'Blood pressure', 'BloodPressure')
    SkinThickness = input_row('Skin Thickness', 'Skin thickness', 'SkinThickness')
    Insulin = input_row('Insulin Level', 'Insulin level', 'Insulin')
    BMI = input_row('BMI', 'Body Mass Index', 'BMI')
    DiabetesPedigreeFunction = input_row('Diabetes Pedigree Function', 'Genetic risk', 'DiabetesPedigreeFunction')
    Age = input_row('Age', 'Age', 'Age')
    if st.button('Predict Diabetes'):
        pred = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        msg = '🟢 The person is diabetic.' if pred[0] == 1 else '🟢 The person is not diabetic.'
        show_result(msg, pred[0] == 1)

# ---- HEART DISEASE ----
elif selected == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    st.info("Enter the following details to predict heart disease risk.")
    age = input_row('Age', 'Age', 'age')
    sex = input_row('Sex (1=male, 0=female)', 'Sex', 'sex')
    cp = input_row('Chest Pain Type (0-3)', 'Chest pain type', 'cp')
    trestbps = input_row('Resting BP', 'Resting blood pressure', 'trestbps')
    chol = input_row('Serum Cholesterol', 'Serum cholesterol', 'chol')
    fbs = input_row('Fasting Blood Sugar > 120mg/dl (1/0)', 'Fasting blood sugar', 'fbs')
    restecg = input_row('Resting ECG (0-2)', 'Resting ECG', 'restecg')
    thalach = input_row('Max Heart Rate', 'Maximum heart rate', 'thalach')
    exang = input_row('Exercise Induced Angina (1/0)', 'Exercise angina', 'exang')
    oldpeak = input_row('ST Depression', 'ST depression', 'oldpeak')
    slope = input_row('Slope (0-2)', 'Slope', 'slope')
    ca = input_row('Major Vessels (0-3)', 'Major vessels', 'ca')
    thal = input_row('Thal (0=normal, 1=fixed, 2=reversible)', 'Thal', 'thal')
    if st.button('Predict Heart Disease'):
        pred = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        msg = '🟢 The person has heart disease.' if pred[0] == 1 else '🟢 The person does not have heart disease.'
        show_result(msg, pred[0] == 1)

# ---- PARKINSON'S ----
elif selected == "Parkinson's":
    st.header("🧠 Parkinson's Disease Prediction")
    st.info("Enter the following details to predict Parkinson's disease risk.")
    fields = [
        ('MDVP:Fo(Hz)', 'fo'), ('MDVP:Fhi(Hz)', 'fhi'), ('MDVP:Flo(Hz)', 'flo'),
        ('MDVP:Jitter(%)', 'Jitter_percent'), ('MDVP:Jitter(Abs)', 'Jitter_Abs'),
        ('MDVP:RAP', 'RAP'), ('MDVP:PPQ', 'PPQ'), ('Jitter:DDP', 'DDP'),
        ('MDVP:Shimmer', 'Shimmer'), ('MDVP:Shimmer(dB)', 'Shimmer_dB'),
        ('Shimmer:APQ3', 'APQ3'), ('Shimmer:APQ5', 'APQ5'), ('MDVP:APQ', 'APQ'),
        ('Shimmer:DDA', 'DDA'), ('NHR', 'NHR'), ('HNR', 'HNR'),
        ('RPDE', 'RPDE'), ('DFA', 'DFA'), ('Spread1', 'spread1'),
        ('Spread2', 'spread2'), ('D2', 'D2'), ('PPE', 'PPE')
    ]
    inputs = [input_row(label, label, key) for label, key in fields]
    if st.button("Predict Parkinson's"):
        pred = models['parkinsons'].predict([inputs])
        msg = "🟢 The person has Parkinson's disease." if pred[0] == 1 else "🟢 The person does not have Parkinson's disease."
        show_result(msg, pred[0] == 1)

# ---- LUNG CANCER ----
elif selected == "Lung Cancer":
    st.header("🫁 Lung Cancer Prediction")
    st.info("Enter the following details to predict lung cancer risk.")
    GENDER = input_row('Gender (1=Male, 0=Female)', 'Gender', 'GENDER')
    AGE = input_row('Age', 'Age', 'AGE')
    SMOKING = input_row('Smoking (1=Yes, 0=No)', 'Smoking', 'SMOKING')
    YELLOW_FINGERS = input_row('Yellow Fingers (1=Yes, 0=No)', 'Yellow fingers', 'YELLOW_FINGERS')
    ANXIETY = input_row('Anxiety (1=Yes, 0=No)', 'Anxiety', 'ANXIETY')
    PEER_PRESSURE = input_row('Peer Pressure (1=Yes, 0=No)', 'Peer pressure', 'PEER_PRESSURE')
    CHRONIC_DISEASE = input_row('Chronic Disease (1=Yes, 0=No)', 'Chronic disease', 'CHRONIC_DISEASE')
    FATIGUE = input_row('Fatigue (1=Yes, 0=No)', 'Fatigue', 'FATIGUE')
    ALLERGY = input_row('Allergy (1=Yes, 0=No)', 'Allergy', 'ALLERGY')
    WHEEZING = input_row('Wheezing (1=Yes, 0=No)', 'Wheezing', 'WHEEZING')
    ALCOHOL_CONSUMING = input_row('Alcohol Consuming (1=Yes, 0=No)', 'Alcohol consuming', 'ALCOHOL_CONSUMING')
    COUGHING = input_row('Coughing (1=Yes, 0=No)', 'Coughing', 'COUGHING')
    SHORTNESS_OF_BREATH = input_row('Shortness Of Breath (1=Yes, 0=No)', 'Shortness of breath', 'SHORTNESS_OF_BREATH')
    SWALLOWING_DIFFICULTY = input_row('Swallowing Difficulty (1=Yes, 0=No)', 'Swallowing difficulty', 'SWALLOWING_DIFFICULTY')
    CHEST_PAIN = input_row('Chest Pain (1=Yes, 0=No)', 'Chest pain', 'CHEST_PAIN')
    if st.button("Predict Lung Cancer"):
        pred = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        msg = "🟢 The person has lung cancer." if pred[0] == 1 else "🟢 The person does not have lung cancer."
        show_result(msg, pred[0] == 1)

# ---- HYPOTHYROID ----
elif selected == "Hypo-Thyroid":
    st.header("🦋 Hypo-Thyroid Prediction")
    st.info("Enter the following details to predict hypo-thyroid risk.")
    age = input_row('Age', 'Age', 'age')
    sex = input_row('Sex (1=Male, 0=Female)', 'Sex', 'sex')
    on_thyroxine = input_row('On Thyroxine (1=Yes, 0=No)', 'On thyroxine', 'on_thyroxine')
    tsh = input_row('TSH Level', 'TSH level', 'tsh')
    t3_measured = input_row('T3 Measured (1=Yes, 0=No)', 'T3 measured', 't3_measured')
    t3 = input_row('T3 Level', 'T3 level', 't3')
    tt4 = input_row('TT4 Level', 'TT4 level', 'tt4')
    if st.button("Predict Hypo-Thyroid"):
        pred = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        msg = "🟢 The person has Hypo-Thyroid disease." if pred[0] == 1 else "🟢 The person does not have Hypo-Thyroid disease."
        show_result(msg, pred[0] == 1)

# ---- FOOTER ----
st.markdown(
    "<hr><center>⚕️ <b>AI Disease Prediction Suite</b> | Powered by Streamlit & scikit-learn</center>",
    unsafe_allow_html=True
)
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="AI Disease Prediction Suite",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- HIDE STREAMLIT DEFAULTS ----
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stButton>button {background-color: #4F8BF9; color: white;}
    .result-card {background: #222; color: #fff; padding: 1em; border-radius: 10px; margin: 1em 0;}
    </style>
""", unsafe_allow_html=True)

# ---- BACKGROUND IMAGE ----
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.7);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- LOAD MODELS ----
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# ---- SIDEBAR MENU ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616494.png", width=80)
    st.title("AI Disease Suite")
    selected = option_menu(
        menu_title="Choose Prediction",
        options=[
            "Diabetes",
            "Heart Disease",
            "Parkinson's",
            "Lung Cancer",
            "Hypo-Thyroid"
        ],
        icons=["droplet-half", "heart-pulse", "person", "lungs", "activity"],
        menu_icon="hospital",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "icon": {"color": "#4F8BF9", "font-size": "22px"},
            "nav-link-selected": {"background-color": "#4F8BF9", "color": "white"},
        }
    )

def input_row(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1) if type == "number" else st.text_input(label, key=key, help=tooltip)

def show_result(message, success=True):
    color = "#27ae60" if success else "#c0392b"
    st.markdown(
        f'<div class="result-card" style="background:{color};color:white;">{message}</div>',
        unsafe_allow_html=True
    )

# ---- DIABETES ----
if selected == "Diabetes":
    st.header("🩸 Diabetes Prediction")
    st.info("Enter the following details to predict diabetes risk.")
    Pregnancies = input_row('Number of Pregnancies', 'Times pregnant', 'Pregnancies')
    Glucose = input_row('Glucose Level', 'Glucose level', 'Glucose')
    BloodPressure = input_row('Blood Pressure', 'Blood pressure', 'BloodPressure')
    SkinThickness = input_row('Skin Thickness', 'Skin thickness', 'SkinThickness')
    Insulin = input_row('Insulin Level', 'Insulin level', 'Insulin')
    BMI = input_row('BMI', 'Body Mass Index', 'BMI')
    DiabetesPedigreeFunction = input_row('Diabetes Pedigree Function', 'Genetic risk', 'DiabetesPedigreeFunction')
    Age = input_row('Age', 'Age', 'Age')
    if st.button('Predict Diabetes'):
        pred = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        msg = '🟢 The person is diabetic.' if pred[0] == 1 else '🟢 The person is not diabetic.'
        show_result(msg, pred[0] == 1)

# ---- HEART DISEASE ----
elif selected == "Heart Disease":
    st.header("❤️ Heart Disease Prediction")
    st.info("Enter the following details to predict heart disease risk.")
    age = input_row('Age', 'Age', 'age')
    sex = input_row('Sex (1=male, 0=female)', 'Sex', 'sex')
    cp = input_row('Chest Pain Type (0-3)', 'Chest pain type', 'cp')
    trestbps = input_row('Resting BP', 'Resting blood pressure', 'trestbps')
    chol = input_row('Serum Cholesterol', 'Serum cholesterol', 'chol')
    fbs = input_row('Fasting Blood Sugar > 120mg/dl (1/0)', 'Fasting blood sugar', 'fbs')
    restecg = input_row('Resting ECG (0-2)', 'Resting ECG', 'restecg')
    thalach = input_row('Max Heart Rate', 'Maximum heart rate', 'thalach')
    exang = input_row('Exercise Induced Angina (1/0)', 'Exercise angina', 'exang')
    oldpeak = input_row('ST Depression', 'ST depression', 'oldpeak')
    slope = input_row('Slope (0-2)', 'Slope', 'slope')
    ca = input_row('Major Vessels (0-3)', 'Major vessels', 'ca')
    thal = input_row('Thal (0=normal, 1=fixed, 2=reversible)', 'Thal', 'thal')
    if st.button('Predict Heart Disease'):
        pred = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        msg = '🟢 The person has heart disease.' if pred[0] == 1 else '🟢 The person does not have heart disease.'
        show_result(msg, pred[0] == 1)

# ---- PARKINSON'S ----
elif selected == "Parkinson's":
    st.header("🧠 Parkinson's Disease Prediction")
    st.info("Enter the following details to predict Parkinson's disease risk.")
    fields = [
        ('MDVP:Fo(Hz)', 'fo'), ('MDVP:Fhi(Hz)', 'fhi'), ('MDVP:Flo(Hz)', 'flo'),
        ('MDVP:Jitter(%)', 'Jitter_percent'), ('MDVP:Jitter(Abs)', 'Jitter_Abs'),
        ('MDVP:RAP', 'RAP'), ('MDVP:PPQ', 'PPQ'), ('Jitter:DDP', 'DDP'),
        ('MDVP:Shimmer', 'Shimmer'), ('MDVP:Shimmer(dB)', 'Shimmer_dB'),
        ('Shimmer:APQ3', 'APQ3'), ('Shimmer:APQ5', 'APQ5'), ('MDVP:APQ', 'APQ'),
        ('Shimmer:DDA', 'DDA'), ('NHR', 'NHR'), ('HNR', 'HNR'),
        ('RPDE', 'RPDE'), ('DFA', 'DFA'), ('Spread1', 'spread1'),
        ('Spread2', 'spread2'), ('D2', 'D2'), ('PPE', 'PPE')
    ]
    inputs = [input_row(label, label, key) for label, key in fields]
    if st.button("Predict Parkinson's"):
        pred = models['parkinsons'].predict([inputs])
        msg = "🟢 The person has Parkinson's disease." if pred[0] == 1 else "🟢 The person does not have Parkinson's disease."
        show_result(msg, pred[0] == 1)

# ---- LUNG CANCER ----
elif selected == "Lung Cancer":
    st.header("🫁 Lung Cancer Prediction")
    st.info("Enter the following details to predict lung cancer risk.")
    GENDER = input_row('Gender (1=Male, 0=Female)', 'Gender', 'GENDER')
    AGE = input_row('Age', 'Age', 'AGE')
    SMOKING = input_row('Smoking (1=Yes, 0=No)', 'Smoking', 'SMOKING')
    YELLOW_FINGERS = input_row('Yellow Fingers (1=Yes, 0=No)', 'Yellow fingers', 'YELLOW_FINGERS')
    ANXIETY = input_row('Anxiety (1=Yes, 0=No)', 'Anxiety', 'ANXIETY')
    PEER_PRESSURE = input_row('Peer Pressure (1=Yes, 0=No)', 'Peer pressure', 'PEER_PRESSURE')
    CHRONIC_DISEASE = input_row('Chronic Disease (1=Yes, 0=No)', 'Chronic disease', 'CHRONIC_DISEASE')
    FATIGUE = input_row('Fatigue (1=Yes, 0=No)', 'Fatigue', 'FATIGUE')
    ALLERGY = input_row('Allergy (1=Yes, 0=No)', 'Allergy', 'ALLERGY')
    WHEEZING = input_row('Wheezing (1=Yes, 0=No)', 'Wheezing', 'WHEEZING')
    ALCOHOL_CONSUMING = input_row('Alcohol Consuming (1=Yes, 0=No)', 'Alcohol consuming', 'ALCOHOL_CONSUMING')
    COUGHING = input_row('Coughing (1=Yes, 0=No)', 'Coughing', 'COUGHING')
    SHORTNESS_OF_BREATH = input_row('Shortness Of Breath (1=Yes, 0=No)', 'Shortness of breath', 'SHORTNESS_OF_BREATH')
    SWALLOWING_DIFFICULTY = input_row('Swallowing Difficulty (1=Yes, 0=No)', 'Swallowing difficulty', 'SWALLOWING_DIFFICULTY')
    CHEST_PAIN = input_row('Chest Pain (1=Yes, 0=No)', 'Chest pain', 'CHEST_PAIN')
    if st.button("Predict Lung Cancer"):
        pred = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        msg = "🟢 The person has lung cancer." if pred[0] == 1 else "🟢 The person does not have lung cancer."
        show_result(msg, pred[0] == 1)

# ---- HYPOTHYROID ----
elif selected == "Hypo-Thyroid":
    st.header("🦋 Hypo-Thyroid Prediction")
    st.info("Enter the following details to predict hypo-thyroid risk.")
    age = input_row('Age', 'Age', 'age')
    sex = input_row('Sex (1=Male, 0=Female)', 'Sex', 'sex')
    on_thyroxine = input_row('On Thyroxine (1=Yes, 0=No)', 'On thyroxine', 'on_thyroxine')
    tsh = input_row('TSH Level', 'TSH level', 'tsh')
    t3_measured = input_row('T3 Measured (1=Yes, 0=No)', 'T3 measured', 't3_measured')
    t3 = input_row('T3 Level', 'T3 level', 't3')
    tt4 = input_row('TT4 Level', 'TT4 level', 'tt4')
    if st.button("Predict Hypo-Thyroid"):
        pred = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        msg = "🟢 The person has Hypo-Thyroid disease." if pred[0] == 1 else "🟢 The person does not have Hypo-Thyroid disease."
        show_result(msg, pred[0] == 1)

# ---- FOOTER ----
st.markdown(
    "<hr><center>⚕️ <b>AI Disease Prediction Suite</b> | Powered by Streamlit & scikit-learn</center>",
    unsafe_allow_html=True
)
