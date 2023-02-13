from flask import Flask, jsonify, request, render_template
from project_data.utils import MedicalInsurance

app = Flask(__name__)

##########################################################################################
################################ Homepage API ########################################
##########################################################################################

@app.route('/')
def homepage():
    print('Medical Insurance Project')
    return render_template('index.html')

##########################################################################################
################################ Prediction API ########################################
##########################################################################################

@app.route('/predict_charges',methods = ['POST'])
def get_insurance_charges():
    
    print('We are in POST Method') 
    data = request.form
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    # print(f'age >> {age}, sex >> {sex}, bmi >> {bmi}, children >> {children}, smoker >> {smoker}, region >> {region} ')
    med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)    
    Charges = med_ins.get_predicted_charges()
    return render_template ('after.html',Charges = med_ins.get_predicted_charges())


    
if __name__ == "__main__":         
    app.run(host='0.0.0.0', port=8080, debug=True)