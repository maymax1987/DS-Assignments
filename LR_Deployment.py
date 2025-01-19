import pickle
import streamlit as st
st.title('Survived prediction : bar chart:')

load = open('model.pkl', 'rb')
model = pickle.load(load)



def predict(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    prediction = model.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
    return prediction



def main():
    st.markdown('for prediction of Survived : chart:')
    Pclass = st.selectbox('Pclass', [1, 2, 3])
    Sex = st.selectbox('Sex', [0, 1])
    Age = st.number_input('Age', min_value = 0, max_value = 100)
    SibSp = st.selectbox('SibSp', [0, 1, 2])
    Parch = st.selectbox('Parch', [1, 2, 3])
    Fare = st.number_input('Fare')
    Embarked = st.selectbox('Embarked', [0, 1, 2])
    if st.button('Predict'):
        result = predict(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
        st.success('the Survived is : {}', format(result))
    
    
if __name__ == '__main__':
    main()    
