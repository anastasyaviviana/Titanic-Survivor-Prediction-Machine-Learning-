from flask import Flask,jsonify,request,json,render_template
import joblib

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil',methods=['POST','GET'])
def hasil():
    sex=request.form['sex']
    if sex=='Female':
        sex_female=1
        sex_male=0
    else:
        sex_female=0
        sex_male=1
    age=int(request.form['age'])
    town=request.form['town']
    if town=='Cherbourg':
        mbark_town_C=1
        mbark_town_Q=0
        mbark_town_S=0
    elif town=='Queenstown':
        mbark_town_C=0
        mbark_town_Q=1
        mbark_town_S=0
    else:
        mbark_town_C=0
        mbark_town_Q=0
        mbark_town_S=1
    pclass=request.form['class']
    if pclass=='Economy':
        pclass=0
    elif pclass=='Business':
        pclass=1
    else:
        pclass=2
    sibsp=int(request.form['sibsp'])
    parch=int(request.form['parch'])
    fare=float(request.form['fare'])
    if age<=15:
        who_child=1
        who_man=0
        who_woman=0
        adult_male=0
    else:
        if sex=='Female':
            who_child=0
            who_man=0
            who_woman=1
            adult_male=0
        else:
            who_child=0
            who_man=1
            who_woman=0
            adult_male=1
    if who_child==1:
        who="Child"
    elif who_man==1:
        who="Man"
    else:
        who="Woman"
    
    if adult_male==1:
        adultmale="True"
    else:
        adultmale="False"
    predict=model.predict([[sex_female,sex_male,who_child,who_man,who_woman,mbark_town_C,mbark_town_Q,mbark_town_S,pclass,age,sibsp,parch,fare,adult_male]])
    predict=predict[0]
    if predict==0:
        predict='Died'
    else:
        predict='Survived'
    return render_template('predict.html',predict=predict,sex=sex,age=age,town=town,pclass=pclass,sibling=sibsp,parent=parch,fare=fare,who=who,adultmale=adultmale)

if __name__=='__main__':
    model=joblib.load('modeltitanic')
    app.run(debug=True) #maksimal port 65536