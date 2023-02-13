from flask import Flask, jsonify, request, render_template
from project_data.utils import MedicalInsurance

app = Flask(__name__)

##########################################################################################
  ################################ Homepage API ########################################
##########################################################################################

@app.route('/')
def homepage():
    print('Medical Insurance Project')
    return render_template('page1.html')

##########################################################################################
################################ Prediction API ########################################
##########################################################################################

@app.route('/predict_charges',methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']

        # print(f'age >> {age}, sex >> {sex}, bmi >> {bmi}, children >> {children}, smoker >> {smoker}, region >> {region} ')
        med_ins = MedicalInsurance(age, sex, bmi, children,smoker, region)    
        Charges = med_ins.get_predicted_charges()
        return jsonify({'Reult': f'Predicted Medical Insurance Charges are:  RS.{Charges} '})

    else:
        print('We are in GET Method')
        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')

        # print(f'age >> {age}, sex >> {sex}, bmi >> {bmi}, children >> {children}, smoker >> {smoker}, region >> {region} ')
        med_ins1 = MedicalInsurance(age, sex, bmi, children,smoker, region)    
        Charges1 = med_ins.get_predicted_charges()
        return jsonify({'Reult': f'Predicted Medical Insurance Charges are:  RS.{Charges1} '})
        
app.run()