#import required libraries

import numpy as np
from sklearn import datasets,metrics
from sklearn.preprocessing import StandardScaler
from numpy.linalg import inv,pinv,LinAlgError

X,y = datasets.load_boston(return_X_y=True)  # load bostan dataset

# Add a dummy column
#Train data
Xtrain_new=X[0:400,:]
Xtrain=np.zeros((Xtrain_new.shape[0],Xtrain_new.shape[1]+1))
Xtrain[:,0]=np.ones((Xtrain_new.shape[0]))
Xtrain[:,1:]=Xtrain_new

print('Type of training data is: ',type(Xtrain))
print('Shape of training data is: ',Xtrain.shape)

Ytrain=y[0:400]

#Test data
Xtest_new=X[400:506,:]
Xtest=np.zeros((Xtest_new.shape[0],Xtest_new.shape[1]+1))
Xtest[:,0]=np.ones((Xtest_new.shape[0]))
Xtest[:,1:]=Xtest_new

print('Type of test data is: ',type(Xtest))
print('Shape of test data is: ',Xtest.shape)

Ytest=y[400:506]

scalerinstance=StandardScaler()
scalerinstance.fit(Xtrain[:,1:])
Xtrain[:,1:]=scalerinstance.transform(Xtrain[:,1:])
Xtest[:,1:]=scalerinstance.transform(Xtest[:,1:])

print(Xtest)

theta=np.random.uniform(0,1,size=(Xtrain.shape[1]))  # Create Theta
print("shape ",theta.shape)

iterations=1000
alpha=0.05
m=Xtrain.shape[0]  #Training data of the model
n=Xtrain.shape[1]  #Features of the model 

print('Value of theta is: ',theta)

for i in range(iterations):
    updatetheta=np.zeros(Xtrain.shape[1])
    yprediction=np.dot(Xtrain,theta)
    error=yprediction-Ytrain
    
    for j in range(n):
        updatetheta[j]=np.sum(error*(Xtrain.T)[j])
    theta=theta-(1/m)*(alpha)*updatetheta    # Update theta

    
print('Value of theta is: ',theta)
print('Shape of theta is: ',theta.shape)

# Prediction on test data.

predictions=np.dot(Xtest,theta)
print('Mean_absolute_error: ',metrics.mean_absolute_error(y_true=Ytest,y_pred=predictions))
print('Mean_squared_error: ',metrics.mean_squared_error(y_true=Ytest,y_pred=predictions))
