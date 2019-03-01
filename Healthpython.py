import pandas 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from azureml import Workspace
#function
def getInfo(age,bmi,glucose,insulin,homa,leptin,adiponectin,Resistin,mcp):
    x=[]
    x.append(age)
    x.append(bmi)
    x.append(glucose)
    x.append(insulin)
    x.append(homa)
    x.append(leptin)
    x.append(adiponectin)
    x.append(Resistin)
    x.append(mcp)
    return calculatePredictionValue(x)
    
#uploading data folder
def calculatePredictionValue(x):
             ws = Workspace()
             dataset = pandas.read_csv("https://healthadvisor.blob.core.windows.net/geekdiva/dataset1.csv")
             Feature_names=['Age','BMI','Glucose','Insulin','HOMA','Leptin','Adiponectin','Resistin','MCP.1']
             x_feature=dataset[Feature_names]
             y = dataset['Classification']
             model = LinearDiscriminantAnalysis()
             model.fit(x_feature, y)
             prediction = model.predict(x)
             return prediction[0]