from components.mymodule import Salle_de_musculation
from components.create_model import test_model, X_train, X_test, y_train, y_test, models, param_grid_model
 
sm = Salle_de_musculation(nombre_de_salle=3, bloc_sanitaire="douches")
print(sm)

test_model(X_train, X_test, y_train, y_test, models, param_grid_model)



