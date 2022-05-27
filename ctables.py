import sqlite3

conn = sqlite3.connect('sensor.sqlite')
cur = conn.cursor()

def create_tables():

    cur.executescript('''

    CREATE TABLE IF NOT EXISTS Regiao (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name        TEXT UNIQUE
    );


    CREATE TABLE IF NOT EXISTS Solo (
        id                      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        tipo                    TEXT UNIQUE,
        fertilidade             INTEGER 
    );

    CREATE TABLE IF NOT EXISTS Talhao (
        id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name            TEXT UNIQUE,
        area            REAL,
        regiao_id       INTEGER,

        CONSTRAINT fk_regiao FOREIGN KEY(regiao_id) REFERENCES Regiao(id) ON DELETE CASCADE
    );

        CREATE TABLE IF NOT EXISTS SoloTalhao(
        solo_id             INTEGER,
        talhao_id           INTEGER,
        min_retencao_agua   REAL,
        max_retencao_agua   REAL,

        CONSTRAINT fk_solo FOREIGN KEY(solo_id) REFERENCES Solo(id) ON DELETE CASCADE,
        CONSTRAINT fk_talhao FOREIGN KEY(talhao_id) REFERENCES Talhao(id) ON DELETE CASCADE,

        PRIMARY KEY(solo_id, talhao_id)

    );

    CREATE TABLE IF NOT EXISTS MicroClimaSensores (
        id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        temperature     REAL,
        precipitacao    REAL,
        rad_solar       REAL,
        umidade         REAL,
        data_medicao    REAL,
        talhao_id       INTEGER,

        CONSTRAINT fk_talhao FOREIGN KEY(talhao_id) REFERENCES Talhao(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS Topografia (
        id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        altitude        REAL,
        declividade     REAL,
        talhao_id       INTEGER,
        CONSTRAINT fk_talhao FOREIGN KEY(talhao_id) REFERENCES Talhao(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS Ciclo (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        talhao_id           INTEGER,
        data_plantio        TEXT,
        descricao           TEXT,

        CONSTRAINT fk_talhao FOREIGN KEY(talhao_id) REFERENCES Talhao(id) ON DELETE CASCADE

    );

    ''')


    #Valores Iniciais

    #Região
    cur.execute('''INSERT OR IGNORE INTO Regiao (name) 
        VALUES ( ? )''', ( 'Jacareí', ))
    cur.execute('''INSERT OR IGNORE INTO Regiao (name) 
        VALUES ( ? )''', ( 'São Caetano', ))
    cur.execute('''INSERT OR IGNORE INTO Regiao (name) 
        VALUES ( ? )''', ( 'Campinas', ))

    #Solo
    cur.execute('''INSERT OR IGNORE INTO Solo (tipo, fertilidade) 
        VALUES ( ?, ? )''', ( 'arenoso', 0))
    cur.execute('''INSERT OR IGNORE INTO Solo (tipo, fertilidade) 
        VALUES ( ?, ? )''', ( 'humoso', 1))
    cur.execute('''INSERT OR IGNORE INTO Solo (tipo, fertilidade) 
        VALUES ( ?, ? )''', ( 'argiloso', 0))

    #Talhão
    cur.execute('''INSERT OR IGNORE INTO Talhao (name, area, regiao_id) 
        VALUES ( ?, ?, ? )''', ( 'J1', 1200, 1))
    cur.execute('''INSERT OR IGNORE INTO Talhao (name, area, regiao_id) 
        VALUES ( ?, ?, ? )''', ( 'J2', 1200, 1))
    cur.execute('''INSERT OR IGNORE INTO Talhao (name, area, regiao_id) 
        VALUES ( ?, ?, ? )''', ( 'SC1', 900, 2))
    cur.execute('''INSERT OR IGNORE INTO Talhao (name, area, regiao_id) 
        VALUES ( ?, ?, ? )''', ( 'CAMP1', 700, 3))

    #SoloTalhao
    cur.execute('''INSERT OR IGNORE INTO SoloTalhao (solo_id, talhao_id, min_retencao_agua, max_retencao_agua) 
        VALUES ( ?, ?, ? , ?)''', ( 1, 1, 0.3, 0.8))
    cur.execute('''INSERT OR IGNORE INTO SoloTalhao (solo_id, talhao_id, min_retencao_agua, max_retencao_agua) 
        VALUES ( ?, ?, ? , ?)''', ( 2, 2, 0.4, 0.9))


    #Topografia
    cur.execute('''INSERT OR IGNORE INTO Topografia (altitude, declividade, talhao_id) 
        VALUES ( ?, ? , ?)''', ( 5, 0.1, 1))
    cur.execute('''INSERT OR IGNORE INTO Topografia (altitude, declividade, talhao_id) 
        VALUES ( ?, ? , ?)''', ( 3, 0.05, 3))

    #Ciclo
    cur.execute('''INSERT OR IGNORE INTO Ciclo (talhao_id, data_plantio, descricao) 
        VALUES ( ?, ? , ?)''', ( 1, '05/22', 'teste 1'))
    cur.execute('''INSERT OR IGNORE INTO Ciclo (talhao_id, data_plantio, descricao) 
        VALUES ( ?, ? , ?)''', ( 2, '04/22', 'teste 2'))


    conn.commit()

