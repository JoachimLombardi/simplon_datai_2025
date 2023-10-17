# Try to import the module "mymodule"
try:
    from ..components import mymodule
except ImportError:
    mymodule = None

# test functions of "mymodule"
import os, sys
parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
target_folder = os.path.join(parent_dir, "components")
sys.path.append(target_folder)
from mymodule import Club_de_sport, Salle_de_musculation
class Test_Mymodule():
    def test_salle_de_musculation(self):
        sm = Salle_de_musculation(nombre_de_salle=3, bloc_sanitaire="douches")
        assert sm.nombre_de_salle == 3 , "Le nombre de salle doit etre 3"
        assert sm.bloc_sanitaire == "douches" , "Le bloc sanitaire doit etre douches"
        assert sm.type_equipements == "haltères et des tapis de courses" , "Les equipements doivent etre haltères et des tapis de courses"
        assert sm.climatisation == "air conditionnée" , "La climatisation doit etre air conditionnée"
        assert sm.__str__() == "La salle de sport comporte 3 salles, un bloc sanitaire de type douches, les équipements sont des haltères et des tapis de courses et le type de climatisation est air conditionnée" , "Le __str__ doit etre correct"

