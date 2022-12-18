from type_def import *
import json 
class OrderManagement:
    def __init__(self):
        pass

    # handle request sent by from match engine
    def handle_request(self, request: OrderItem):
        pass
        

if __name__ == "__main__":

    def handle(orderitem):
        print('-------')
        print('request', json.dumps(orderitem.__dict__))
        ret = OrderManagement.handle_request(orderitem)
        # for update in ret['order_updates']:
        #     print('order_update', json.dumps(update.__dict__))
        # for trade in ret['trades']:
        #     print('trade', json.dumps(trade.__dict__))

    handle(OrderItem(1, OrderStatus.COMPLETED, 10, 100, 1))
    handle(OrderItem(2, OrderStatus.COMPLETED, 20, 80, 2))