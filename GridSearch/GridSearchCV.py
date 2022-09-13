from random import shuffle
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold
import numpy as np



kf=KFold(n_splits=5,shuffle=True)
param_grid={
    "alpha":np.arange(0.0001,1,10),
    "solver":["sag","lsqr"]
}

ridge=Ridge()
ridge_cv=GridSearchCV(ridge,param_grid,cv=kf)

print(ridge_cv.best_estimator_)