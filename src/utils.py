##LAS FUNCIONES PEQUEÑAS 
##VAN AQUÍ 

#Mostrar los encabezados con su índice. Es una función de guía para el desarrollo de este proyecto.
def encabezados_con_indice(df):
    return [(index, col) for index, col in enumerate(df.columns)]
    
#Mostrar los encabezados sin su índice. Es una función de guía para el desarrollo de este proyecto.
def encabezados_sin_indice(df):
    return [col for col in df.columns]

#Obtiene una lista con los nombres de los colaboradores. Se utiliza de forma dinámica para generar los diferentes reportes.
def generar_lista_de_colaboradores(df):
    return df.columns.get_level_values(1)[16:35+1].to_list()
