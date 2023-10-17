from components.mymodule import Club_de_sport, Salle_de_musculation
from tests.test import Test_Mymodule
sm = Salle_de_musculation(nombre_de_salle=3, bloc_sanitaire="douches")
print(sm)
test = Test_Mymodule()
test.test_salle_de_musculation()





