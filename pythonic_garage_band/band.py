from abc import abstractmethod, ABC

class Band:
    """this class takes a name and members list as arguments and create object of the band and also store that object and return the band name and put the play solo content in solos list"""
    instances=[]
    def __init__(self, name, members):
        self.name=name
        self.members=members
        Band.instances.append(self)

    def play_solos(self):
        solos=[]
        for i in self.members:
             solos.append(i.play_solo())
        return solos
    
    def __str__(self):
        return f'{self.name} band'
    def __repr__(self):
        return f"Name = {self.name}"

    @classmethod
    def to_list(cls) :
        return cls.instances   


class Musician(ABC):
        """This class is the father class for Guitarist,Drummer and Bassist and will return a name and instrument for each one of them """
        def __init__(self, name):
            self.name = name
            
        def play_solos(self):
            return 
        def get_instrument(self):
            return 
        def __str__(self):
            return f"My name is {self.name} and I play {self.get_instrument()}"
        def __repr__(self):
            return f"{self.__class__.__name__} instance. Name = {self.name}"
        def play_solo(self):
            return self.play_solos()

            


class Guitarist(Musician):
    """this class will set the Guitarist information and ins a child of musician class"""
    def __init__(self, name):
        super().__init__(name)
         
    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod
    def play_solo():
        return "face melting guitar solo"  


class Drummer(Musician):
    """this class will set the Drummer information and ins a child of musician class"""

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "drums"
    @staticmethod
    def play_solo():
        return "rattle boom crash"
    
class Bassist(Musician):
    """this class will set the Bassist information and ins a child of musician class"""

    def __init__(self,name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "bass"
    @staticmethod
    def play_solo():
        return "bom bom buh bom"