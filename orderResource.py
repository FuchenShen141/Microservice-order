import pymysql

import os


class Resource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        #usr = os.environ.get("DBUSER")
        usr ="admin"
        #pw = os.environ.get("DBPW")
        pw = "shenfuchen8888"
        #h = os.environ.get("DBHOST")
        h = "e6156.ckryvlzgg4gw.us-east-1.rds.amazonaws.com"
        db="orders"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            database=db,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    # Getting all the active orders;
    @staticmethod
    def get_active_orders():

        sql = "SELECT * FROM orderitem WHERE status='ACTIVE'";
        conn = Resource._get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        return result
    
    #Adding raw order to the database 
    @staticmethod
    def addOrder(raw_order):
        #process the raw order first
        raw_order['remaining_volume'] = raw_order['volume']
        raw_order['status'] = 'ACTIVE'
        placeholder = ",".join(["%s"] * len(raw_order))
        sql = "INSERT INTO orderitem ({columns}) VALUES ({VALUES});".format(
            columns = ",".join(raw_order.keys()),
            values=placeholder)
        conn = Resource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, list(raw_order.values()))

        return res
    
    #Update order to the database
    @staticmethod
    def updateOrder(matched_order):
        # remove the last trade_id item in the request format
        del matched_order['trade_id']
        sql = "UPDATE orderitem SET status={status}, volume={volume}, remaining_volume={remain} WHERE order_id={orderid};".format(
              remain = matched_order['remaining_volume'],
              volume = matched_order['order_volume'],
              status = matched_order['status'],
              orderid = str(matched_order['order_id'])
        )
        conn = Resource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)

        return res
    
    #Get order by user (might not be used anyways)
    @staticmethod
    def get_order_by_user(user_id):
        
        sql = "SELECT * FROM orderitem WHERE user_id=%s"
        conn = Resource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=user_id)
        result = cur.fetchall()

        return result
        
    






