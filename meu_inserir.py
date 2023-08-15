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
        query = 'INSERT INTO aluno(nome, cpf) VALUES(%s,%s)'

        data_to_insert = ('chico', '456')

        cursor.execute(query, data_to_insert)
        connection.commit()

        print('dados inseridos com sucesso.')


except mysql.connector.Error as e:
    if connection.is_connected():
        connection.rollback
        print('Erro ao inserir dados', e)


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('conexão errada')