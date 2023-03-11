import numpy as np
import xgboost
import joblib
from flask import Flask, request, render_template
app = Flask(__name__)


def pp_Gender(CODE_GENDER):
    CODE_GENDER_F = 0
    if CODE_GENDER == 'Female':
        CODE_GENDER_F = 1
    elif CODE_GENDER == 'Male':
        CODE_GENDER_F = 0
    return CODE_GENDER_F

def pp_car(FLAG_OWN_CAR):
    FLAG_OWN_CAR_N = 0
    if FLAG_OWN_CAR == 'Y':
        FLAG_OWN_CAR_N = 0
    elif FLAG_OWN_CAR == 'N':
        FLAG_OWN_CAR_N = 1
    return FLAG_OWN_CAR_N


loaded_model = joblib.load('C:\\Users\\HP\\homecredit\\xgboost_mantap.pkl')


@app.route('/', methods=['GET', 'POST'])
def home():
    
    str_prediction = ''
    
    if request.method == 'POST':
        AMT_CREDIT = float(request.form["AMT_CREDIT"])
        DAYS_ID_PUBLISH = float(request.form["DAYS_ID_PUBLISH"])
        DAYS_BIRTH = float(request.form["DAYS_BIRTH"])
        AMT_GOODS_PRICE =float(request.form["AMT_GOODS_PRICE"])
        AMT_ANNUITY = float(request.form["AMT_ANNUITY"])
        DAYS_EMPLOYED = float(request.form["DAYS_EMPLOYED"])
        AMT_CREDIT = float(request.form["AMT_CREDIT"])
        DAYS_LAST_PHONE_CHANGE = float(request.form['DAYS_LAST_PHONE_CHANGE'])
        CODE_GENDER_F = pp_Gender(str(request.form['CODE_GENDER']))
        AMT_INCOME_TOTAL = float(request.form['AMT_INCOME_TOTAL'])
        OWN_CAR_AGE = float(request.form['OWN_CAR_AGE'])
        FLAG_OWN_CAR = pp_car(str(request.form['FLAG_OWN_CAR']))

        final_features = [AMT_CREDIT,DAYS_ID_PUBLISH,DAYS_BIRTH,AMT_GOODS_PRICE, AMT_ANNUITY, DAYS_EMPLOYED, DAYS_LAST_PHONE_CHANGE, CODE_GENDER_F, AMT_INCOME_TOTAL, OWN_CAR_AGE, FLAG_OWN_CAR]

        prediction = loaded_model.predict([final_features])
        prediction = prediction[0]

        if prediction == 1:
            str_prediction = 'Sorry, You are not eligible to get the credit'
        elif prediction == 0:
            str_prediction = 'Congratulations, you are eligible to get the credit!'
    
    return render_template('index.html', str_prediction=str_prediction)
