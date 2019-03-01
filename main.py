import pandas 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from flask import Flask,render_template,request
from flask import jsonify
import numpy as np

def getInfo(age,bmi,glucose,insulin,homa,leptin,adiponectin,resistin,mcp1):
    x=[]
    x.append(age)
    x.append(bmi)
    x.append(glucose)
    x.append(insulin)
    x.append(homa)
    x.append(leptin)
    x.append(adiponectin)
    x.append(resistin)
    x.append(mcp1)

    data = np.array(x)
    x = data.astype(np.float)

    dataset = pandas.read_csv("https://healthadvisor.blob.core.windows.net/geekdiva/dataset1.csv")#pandas.read_excel(r"D:\Users\poojitha.gangula\Desktop\dataset1.xls")
    Feature_names=['Age','BMI','Glucose','Insulin','HOMA','Leptin','Adiponectin','Resistin','MCP.1']
    x_feature=dataset[Feature_names]
    y = dataset['Classification']
    model = LinearDiscriminantAnalysis()
    model.fit(x_feature, y)
    x_test=[x,]
    prediction = model.predict(x_test)
    
    if prediction[0] != 1 :
        return "Positive"
    else :
        return "Negative"

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    data        = request.form
    age         = data.get("age")
    bmi         = data.get("bmi")
    glucose     = data.get("glucose")
    insulin     = data.get("insulin")
    homa        = data.get("homa")
    leptin      = data.get("leptin")
    adiponectin = data.get("adiponectin")
    resistin    = data.get("resistin")
    mcp1         = data.get("mcp1")

    response = getInfo(age,bmi,glucose,insulin,homa,leptin,adiponectin,resistin,mcp1)

    return jsonify(message=response)

@app.route('/causes')    
def causes():
    return render_template("causes.html")

@app.route('/govtschemes')    
def govtschemes():
    return render_template("causes.html")

if __name__=="__main__":
    app.run(debug=True)
