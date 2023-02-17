"""
 responsible for getting the input from any user using a web page, using the 
 same input for generating predictions and then showing this prediction back 
 to the user using a web page.

  python manage.py runserver to run the server
"""
from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    import pickle
    model = pickle.load(open("/Users/joonghochoi/Desktop/Titanic_Survival_Prediction/Titanic_Survial_Prediction_Web/Titanic_Survial_Prediction_Web/titanic_survival_ml_model.sav", "rb"))
    scaled = pickle.load(open("/Users/joonghochoi/Desktop/Titanic_Survival_Prediction/Titanic_Survial_Prediction_Web/Titanic_Survial_Prediction_Web/scaler.sav", "rb"))
    prediction = model.predict(scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
        

# our result page view
def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'result.html', {'result':result})

    