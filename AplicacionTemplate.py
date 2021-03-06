import Aplicacion
from Menu import *
from Variable import *
from validador import *
#------------------------------------------------
#--------------- TODO ---------------------------
#------------------------------------------------
# 1) Lista de tareas pendientes a implementar.
# 2) Si no te gusta lo sacas :).
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------
class NombreAplicacion(Aplicacion.Aplicacion):

    """
    FILLME
    """

    #-----------------------
    #--- inicializacion ----
    #-----------------------
    def iniciar(self,**args):   
        #variables de programa
        self.variableNoModificablePorElUsuario1 = 420
        
        #variables de usuario   
        self.vars["variable1"] = Variable(5,self.modifGenerico,orden=0)
        self.vars["variable2"] = Variable(5.1,self.modifGenerico,minimo=0,maximo=8,flags={"algunNombreDeFlag":True},orden=1)
        self.vars["variable3"] = Variable("asd",self.modifAlgunParametro,orden=2)
        self.vars["variableConVariasPalabrasEnCamelCase"] = Variable(args["arg1"],self.modifValoresPosibles,valoresPosibles=["valor1","valor2"],orden=3)
        
        #Items del Menu
        self.agregarMenu(0,Leaf("FuncionJugosa","Si estas viendo esto es porque te apuraste y mandaste a probar asi nomas el programa",self.funcionJugosa))
        
        #Funciones que se ejecutan luego de llamar a Modificar.
        self.agregarPostFunciones(posFuncion1)
        
    #-----------------------
    #--- Funciones ---------
    #-----------------------
    def funcionJugosa(self):
        #POR FAVOR BORRA ESTO CUANDO LO USES.
        pass
    
    def posFuncion1(self):
        pass
        
    #-----------------------
    #--- modificadores -----
    #-----------------------
    # Crear todos los modificadores con esta estructura, y SIEMPRE respetando el encabezado (self,key,*params):     
    def modifAlgunParametro(self,key,*params):
        #Modificador de una variable de usuario, 
        if(len(params) == 0):
            #realizar accion de modificacion, ejecutada cuando se hace a traves de interfaz.
            pass
        else:
            #realizar accion de modificacion, cuando se invoca programaticamente al metodo.
            pass
            
    #-----------------------
    #--- otros -------------    
    #-----------------------    
    # Funcion opcional. Si se desea mostrar algun tipo de informacion ( o ejecutar algun comando)
    # en el menu principal( arriba del nombre de la aplicacion) hay que sobreescribir este metodo.
    def funcionDeInicioLoop(self):
        self.espaciador()
        print "FILLME OR KILLME"
        self.espaciador()
        
    # Este metodo muestra lo que quieras, la idea es que expliques como se usa el programa.
    def ayuda(self):
        print "-----------------------------------------------------------------"
        print "TEXTO DE AYUDA"
        print "-----------------------------------------------------------------"   
    
    # Texto personalizado de salida.    
    def salirPrint(self):
        print "--- \\m/ ---"

#esto siempre va.
# tenes que invocar a tu clase principal, los tres primeros parametros son el nombre, version y si es o no con pantalla grafica.
# despues tenes que pasarle todos los parametros que quieras, separados por comas.
if __name__ == '__main__':
    a = NombreAplicacion("NombreAplicacion","1.0.0",False,arg1="argumento1")
                    
    a.menuPrincipal()       