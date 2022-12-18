# CREATE TABLE `orderitem` (
#   `order_id` int(11) NOT NULL AUTO_INCREMENT,
#   `user_id` int(11)  NOT NULL,
#   `instrument` varchar(20)  NOT NULL,
#   `side` varchar(6) NOT NULL,
#   `price` float(11,2)  NOT NULL,
#   `volume` int(11) NOT NULL,
#   `remaining_volume` int(11) NOT NULL,
#   `status` varchar(10) NOT NULL,
#   PRIMARY KEY (`order_id`)
#   FOREIGN KEY (`User.id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=3513 DEFAULT CHARSET=utf8;

class OrderStatus:
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

class OrderAction:
    BUY = 'BUY'
    SELL = 'SELL'
    CANCEL = 'CANCEL'

class OrderItem:
    def __init__(self, order_id, user_id, instrument, side, price, volume, remaining_volume, status):
        assert price > 0
        assert volume > 0 
        assert remaining_volume >= 0 
        self.order_id = order_id
        self.user_id = user_id 
        self.instrument = instrument 
        self.side = side 
        self.price = price 
        self.volume = volume 
        self.remaining_volume = remaining_volume
        self.status = status 

class OrderRequest:
    def __init__(self, order_id, instrument, action : OrderAction, price, volume):
        self.order_id = order_id
        self.instrument = instrument 
        self.action = action 
        self.price = price 
        self.volume = volume 
        if self.action != OrderAction.CANCEL:
            assert price > 0
            assert volume > 0
 