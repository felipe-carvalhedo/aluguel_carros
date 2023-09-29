import psycopg2
import lista_de_carros

class Car:
    def __init__(self, id, marca, modelo, ano, preco_diaria, disponivel=True):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria
        self.disponivel = disponivel


class EmpresaAluguelCarros:

    def __init__(self):
        self.conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="mysecret",
            host="localhost",
            port="15432"
        )
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        self.popular_carros(lista_de_carros.carros)

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS carros (
                id SERIAL PRIMARY KEY NOT NULL,
                marca VARCHAR(255),
                modelo VARCHAR(255),
                ano INTEGER,
                placa VARCHAR(7) UNIQUE,
                preco_diaria NUMERIC(10, 2),
                disponivel BOOLEAN
            )
        """)
        self.conn.commit()

    def criar_carro(self, marca, modelo, ano, placa, preco_diaria, disponivel):
        try:
            ano = int(ano)
        except Exception:
            print(("Ano inválido, tente novamente!"))
            return
        try:
            preco_diaria = float(preco_diaria)
        except Exception:
            print(("Preço inválido, tente novamente!"))
            return
        query = "INSERT INTO carros (marca, modelo, ano, placa, preco_diaria, disponivel) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (marca, modelo, ano, placa, preco_diaria, disponivel)
        self.cursor.execute(query, values)
        self.conn.commit()

    def popular_carros(self, carros):
        query = "INSERT INTO carros (marca, modelo, ano, placa, preco_diaria, disponivel) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING"
        for carro in carros:
            values = (carro["marca"], carro["modelo"], carro["ano"], carro["placa"], carro["preco_diaria"], carro["disponivel"])
            self.cursor.execute(query, values)
            self.conn.commit()

    def listar_carros(self):
        query = "SELECT * FROM carros"
        self.cursor.execute(query)
        carros = self.cursor.fetchall()
        return carros

    def buscar_carro(self, placa):
        query = "SELECT * FROM carros WHERE placa = %s"
        value = (placa,)
        self.cursor.execute(query, value)
        carro = self.cursor.fetchone()
        print(carro)

    def atualizar_carro(self, id, marca, modelo, ano, placa, preco_diaria, disponivel):
        try:
            ano = int(ano)
        except Exception:
            print(("Ano inválido, tente novamente!"))
            return
        try:
            preco_diaria = float(preco_diaria)
        except Exception:
            print(("Preço inválido, tente novamente!"))
            return
        query = "UPDATE carros SET marca = %s, modelo = %s, ano = %s, placa = %s, preco_diaria = %s, disponivel = %s WHERE id = %s"
        values = (marca, modelo, ano, placa, preco_diaria, disponivel, id)
        self.cursor.execute(query, values)
        self.conn.commit()


    def deletar_carro(self, id):
        query = "DELETE FROM carros WHERE id = %s"
        value = (id,)
        self.cursor.execute(query, value)
        self.conn.commit()
