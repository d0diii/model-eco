import json
import sqlite3

#Simulação de dados de entrada do sensor

conn = sqlite3.connect('sensor.sqlite')
cur = conn.cursor()

def insert_data(payload):
	
	df = json.loads(payload)
	temperature = df['TEMP']
	umidade		= df['HUMID']
	rad_solar	= df['ILLUM']
	#MicroClimaSensores
	cur.execute('''INSERT OR IGNORE INTO MicroClimaSensores (temperature, precipitacao, rad_solar, umidade, data_medicao, talhao_id) 
		VALUES ( ?, ?, ? , ?, ?, ?)''', ( temperature, 1000, rad_solar, umidade, '05/22', 1))

	conn.commit()