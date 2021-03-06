import joblib
from dataProj.Functions import getColumnTitles, Discretize
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
numOfBins=3
def sklearnNaiveBayes(test, train,structure):
    model=GaussianNB()
    le=preprocessing.LabelEncoder()

    train = Discretize(numOfBins, train, structure)
    test = Discretize(numOfBins, test, structure)

    target_train=train['class']
    inputs_train=train.drop('class',axis='columns')

    target_test=test['class']
    inputs_test=test.drop('class',axis='columns')

    def fit_transforms(table):
        columns = getColumnTitles(table)
        for col in columns:
            try:
               table[col] = le.fit_transform(table[col])
            except:
                continue
        return table

    inputs_train=fit_transforms(inputs_train)
    model.fit(inputs_train,target_train)

    #save model to file
    filename='NaiveBayesSKlearn_model.sav'
    joblib.dump(model,filename)


    inputs_test=fit_transforms(inputs_test)
    return model.score(inputs_test,target_test)