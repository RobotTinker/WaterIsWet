from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pandas as pd


#def Load_Data(file_name):
    #data = csv.reader(file_name, delimiter=',')# skiprows=1, converters={0: lambda s: str(s)})
    #return data.tolist()

Base = declarative_base()

class Data(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
	__tablename__ = 'Aquastat'
	__table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
	id = Column(Integer, primary_key=True, nullable=False) 
	country = Column(VARCHAR)
	mid_year = Column(Integer)
	year_bucker = Column(VARCHAR)
	area = Column(Float)
	perc_cultivated = Column(Float)
	total_pop = Column(Float)
	rural_pop = Column(Float)
	urban_pop = Column(Float)
	pop_density = Column(Float)
	gdp_per_cap = Column(Float)
	hdi = Column(Float)
	gii = Column(Float)
	perc_undernourish = Column(Float)
	nri = Column(Float)
	dependency_ratio = Column(Float)
	renew_water_per_cap = Column(Float)
	water_stress = Column(Float)
	flood = Column(Float)
	perc_safe_water = Column(Float)
	code = Column(Integer)
	cn_name = Column(VARCHAR)





engine = create_engine('sqlite:///../data/Aquastat.sqlite')
Base.metadata.create_all(engine)
df_data = pd.read_csv('../data/Data_Final.csv')
df_code = pd.read_csv('../data/countries.csv')
df = df_data.merge(df_code, left_on='country', right_on='cn_name', how='left')
df.to_sql(con=engine, index_label='id', name=Data.__tablename__, if_exists='replace')

	