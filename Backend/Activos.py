class Activo:
    def __init__(self,Cod_Activo,Nombre,SerieProducto,FechaIngreso,Precio,Usuario):
        self.Cod_Activo = Cod_Activo
        self.Nombre = Nombre
        self.SerieProducto = SerieProducto
        self.FechaIngreso = FechaIngreso
        self.Precio = Precio
        self.Usuario = Usuario

    def toDBCollection(self):
        return{
            'Cod_Activo': self.Cod_Activo,
            'Nombre': self.Nombre,
            'SerieProducto': self.SerieProducto,
            'FechaIngreso': self.FechaIngreso,
            'Precio': self.Precio,
            'Usuario': self.Usuario
        }
    
