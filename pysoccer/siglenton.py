# Builder crear objetos de forma paso a paso de forma formulada
# Fachada: crear interfaces de usuario comodas y orgsanizadas para su uso
#Siglenton: que una clase solo deba tener una instancia
# Adapter: que dos modulos, sofware o lo que sea sean capaces de comunicarse entre si siendo incompatibles
#Prototype: Crear objetos a partir de instancias ya creadas, como el mismo nombre dice, protoype

# """ Se siglento se utliza para que una clase tenga una sola instancia, es conveniente en conexiones a bases de datos y etc, se hace con el metodo new, se crea una variable de clase que se llame instancia que contrenda la instancia,  despues se si no existe es variable o es none , se le asigna un super donde herede de todo de la clase y cls, despues se llama al metodo __new__ otra vez y se le pasa cls con parametro
# """

# Proxima implementacion de la musica para que no se pueda ser capaz de crear dos instancias de la musica

class SingletoMeta(type):

    _instancia={}
    
    
    def __call__(cls,*args, **kwargs) -> None:
        if cls not in cls._instancia:
            instancia = super().__call__(*args, **kwargs)
            cls._instancia[cls]= instancia
        return cls._instancia[cls]



class Sigleton(metaclass=SingletoMeta):
    def some(self):
        pass
    



s1=Sigleton()
s2=Sigleton()


if id(s1) == id(s2):
    print("same")
else:
    print("not same")