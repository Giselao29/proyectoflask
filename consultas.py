#MODELO

class Consulta:

    CREATE='''
        CREATE TABLE clientes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50) NOT NULL,
            APELLIDO VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL
        )
    '''
    DELETE="DROP TABLE clientes"
    
    INSERT ="INSERT INTO clientes VALUES(NULL, ?,?,?)"
    
    SELECT="SELECT * FROM clientes"
    
    UPDATE="UPDATE clientes SET NOMBRE=?,APELLIDO=?,EMAIL=? WHERE ID=?"
    
    DELETE="DELETE from clientes WHERE ID=?"
    
    BUSCAR="SELECT * from clientes WHERE ID=?"
    
    