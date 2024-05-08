import psycopg2
from configparser import ConfigParser

class DataBase:
    __filename='backend\\database\\database.ini'
    __section='postgresql'

    def __init__(self) -> None:
        parser = ConfigParser()
        parser.read(self.__filename)

        # get section, default to postgresql
        config = {}
        if parser.has_section(self.__section):
            params = parser.items(self.__section)

            for param in params:
                config[param[0]] = param[1]
            
            # connecting to the PostgreSQL server
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')
                self.cursor = conn.cursor()
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.__section, self.__filename))
        
        # with psycopg2.connect(**config) as conn:
        #     print('Connected to the PostgreSQL server.')
        #     connection = conn
        

    # def __load_config(filename='backend\\database\\database.ini', section='postgresql'):
        # parser = ConfigParser()
        # parser.read(filename)
        
        # # get section, default to postgresql
        # config = {}
        # if parser.has_section(section):
        #     params = parser.items(section)
        #     for param in params:
        #         config[param[0]] = param[1]
        # else:
        #     raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        # print(config)
        # return config

    # def __connect(self):
        """ Connect to the PostgreSQL database server """
        # try:
        #     config: dict = self.__load_config()
        #     # connecting to the PostgreSQL server
        #     with psycopg2.connect(**config) as conn:
        #         print('Connected to the PostgreSQL server.')
        #         return conn
        # except (psycopg2.DatabaseError, Exception) as error:
        #     print(error)
        


if __name__ == '__main__':
    database: DataBase = DataBase()
    database.cursor.execute(
        """
        SELECT * FROM carro;
        """
    )
    print(database.cursor.fetchall())
