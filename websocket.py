import json
import websocket
import psycopg2
from psycopg2 import sql
 
symbol = 'btcusdt'
socket = f'wss://stream.binance.com:9443/ws/{symbol}@trade'
 
# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="binance",
    user="postgres",
    password="",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
 
# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        event_type TEXT,
        event_time BIGINT,
        symbol TEXT,
        trade_id BIGINT,
        price NUMERIC,
        quantity NUMERIC,
        buyer_order_id BIGINT,
        seller_order_id BIGINT,
        trade_time BIGINT,
        is_market BOOLEAN,
        is_maker BOOLEAN
    );
""")
conn.commit()
 
def on_message(ws, message):
    data = json.loads(message)
    event_type = data.get('e', '')
    event_time = data.get('E', 0)
    symbol = data.get('s', '')
    trade_id = data.get('t', 0)
    price = data.get('p', '0.0')
    quantity = data.get('q', '0.0')
    buyer_order_id = data.get('b', 0)
    seller_order_id = data.get('a', 0)
    trade_time = data.get('T', 0)
    is_market = data.get('m', False)
    is_maker = data.get('M', False)
 
    # Insert data into PostgreSQL
    cur.execute(sql.SQL("""
        INSERT INTO trades
        (event_type, event_time, symbol, trade_id, price, quantity, buyer_order_id, seller_order_id, trade_time, is_market, is_maker)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """), (event_type, event_time, symbol, trade_id, price, quantity, buyer_order_id, seller_order_id, trade_time, is_market, is_maker))
    conn.commit()
 
def on_error(ws, error):
    print(error)
 
def on_close(ws, close_status_code, close_msg):
    print("### closed ###")
    cur.close()
    conn.close()
 
def on_open(ws):
    print("Opened connection")
 
ws = websocket.WebSocketApp(socket,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
 
ws.run_forever()
 
has context menu
