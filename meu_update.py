import mysql.connector

config = {
    
    "user": "root",
    "password": "aluno",
    "host": "localhost",
    "database": "aluno"
}

try:

    connection = mysql.connector.connect(**config)
    if connection.is_connected():

        cursor = connection.cursor()
        query = ('UPDATE aluno SET PRICE = WHERE = "RHAT"')



except mysql.connector.Error as e:
    if connection.is_connected():
        connection.rollback
        print('Erro ao utilizar dados', e)


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('atualização errada')
        