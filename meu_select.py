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
        print('conexão bem sucedida!')

        cursor = connection.cursor()
        query = 'SELECT * FROM aluno'

        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)

except mysql.connector.Error as e:
    print('erro ao conectar ou executar consulta:', e)

finally:

    if connection.is_connected():
        cursor.close()
        connection.close()
        print('conexão encerrada')