from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Database:
    def __init__(self, user:str, password:str, database:str, host:str='localhost', port:str='3306'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
        self.connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        

    def connect(self) -> None:
        try:
            self.engine = engine = create_engine(self.connection, echo=False)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as e:
            print(f'Erro ao conectar com o banco de dados: {e}')
            
    
    def base(self) -> None:
        self.Base = declarative_base()