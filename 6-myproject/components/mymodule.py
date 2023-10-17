class Club_de_sport():
    def __init__(self, nombre_de_salle, bloc_sanitaire, type_equipements, climatisation) -> None:
        self._type_equipements = type_equipements
        self._climatisation = climatisation
        self._nombre_de_salle = nombre_de_salle
        self._bloc_sanitaire = bloc_sanitaire
    
    @property
    def nombre_de_salle(self):
        return self._nombre_de_salle
    
    @nombre_de_salle.setter
    def nombre_de_salle(self, nombre_de_salle):
        self._nombre_de_salle = nombre_de_salle

    @property
    def bloc_sanitaire(self):
        return self._bloc_sanitaire
    
    @bloc_sanitaire.setter
    def bloc_sanitaire(self, bloc_sanitaire):
        self._bloc_sanitaire = bloc_sanitaire

    @property
    def type_equipements(self):
        return self._type_equipements
    
    @type_equipements.setter
    def type_equipements(self, type_equipements):
        self._type_equipements = type_equipements

    @property
    def climatisation(self):
        return self._climatisation
    
    @climatisation.setter
    def climatisation(self, climatisation):
        self._climatisation = climatisation
    
    def __str__(self) -> str:
        return f"La salle de sport comporte {self.nombre_de_salle} salles, un bloc sanitaire de type {self.bloc_sanitaire}, les équipements sont des {self.type_equipements} et le type de climatisation est {self.climatisation}"
    
class Salle_de_musculation(Club_de_sport):
    def __init__(self, nombre_de_salle, bloc_sanitaire, type_equipements="haltères et des tapis de courses", climatisation="air") -> None:
        super().__init__(nombre_de_salle, bloc_sanitaire, type_equipements, climatisation)
    def __str__(self) -> str:
        return super().__str__()
    