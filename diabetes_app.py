import pickle
import streamlit as st

# Load the saved model
with open('best_clf_pima_diabetics.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_diabetes(Pregnancies, Age, BMI, DiabetesPedigreeFunction, Insulin, Skinthickness, Bloodpressure, Glucose):
    features = [[Pregnancies, Age, BMI, DiabetesPedigreeFunction, Insulin, Skinthickness, Bloodpressure, Glucose]]
    prediction = model.predict(features)
    return prediction[0]

# Streamlit app
def main():
    st.title("Early detection of diabetes Prediction")

    # Input fields for user to enter features
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=0)
    age = st.number_input("Age", min_value=0, max_value=120, value=20)
    bmi = st.number_input("BMI", min_value=0.0, value=20.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.0)
    insulin = st.number_input("Insulin", min_value=0, value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=60)
    glucose = st.number_input("Glucose", min_value=0, value=60)

    # Make prediction when button is clicked
    if st.button("Predict"):
        result = predict_diabetes(pregnancies, age, bmi, diabetes_pedigree_function, insulin, skin_thickness, blood_pressure, glucose)
        st.success(f" Based on information provided, you are not at risk for Diabetes because the prediction outcome is: {result}")

# Run the app
if __name__ == "__main__":
    main()
    