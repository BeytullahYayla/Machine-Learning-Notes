from random import shuffle
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold
import numpy as np



kf=KFold(n_splits=5,shuffle=True)
param_grid={
    "alpha":np.arange(0.0001,1,10),
    "solver":["sag","lsqr"]
}

ridge=Ridge()
ridge_cv=RandomizedSearchCV(ridge,param_grid,cv=kf)
ridge_cv.fit(X_train,y_train)

print(ridge_cv.best_estimator_,ridge_cv.best_params_)