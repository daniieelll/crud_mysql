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
        print("conexão bem-sucedida!")
except mysql.connector.Error as e:
    print("erro ao conectar:", e)


try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('conexão bem sucedida!')

    cursor = connection.cursor()
    query = 'select * FROM alunos'
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
        



try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():

        cursor = connection.cursor()
        query = ('DELETE from aluno WHERE = "RHAT"')


except mysql.connector.Error as e:
    if connection.is_connected():
        connection.rollback
        print('Erro ao deletar dados dados', e)



finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('forma de deletação incorreta')
        

