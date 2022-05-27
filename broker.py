import paho.mqtt.client as mqtt
import sys

from insert import insert_data
 
#definicoes: 
broker = "iot.maratona.dev"
port = 31666
username = "maratoners"
password = "btc-2021"
topic = "quanam"


#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))
 
    #faz subscribe automatico no topico
    client.subscribe(topic)
 
#Callback - mensagem recebida do broker
def on_message(client, userdata, msg):
    
    payload = msg.payload.decode()
    insert_data(payload)
 
 
def main_broker():
    try:
            print("[STATUS] Inicializando MQTT...")
            #inicializa MQTT:
            client = mqtt.Client()
            client.username_pw_set(username, password=password)
            client.on_connect = on_connect
            client.on_message = on_message

            client.connect(broker, port)
            client.loop_forever()

    except KeyboardInterrupt:
            print ("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
            #sys.exit(0)

