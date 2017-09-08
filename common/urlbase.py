

def list():

    url=prelist()


    return url



def sitlist():

    url=['http://192.168.31.160:8004','http://192.168.31.160:8006']

    return url


def prelist():
    url = ['http://192.168.31.160:8005', 'http://192.168.31.160:8007']

    return url



def sit_emp():

    url = sit()

    return url

def sit_UaUser():

    url = sit_UaUser()

    return url


def pre_emp():

    url = pre()

    return url

def preUaUser():

    url = pre_UaUser()

    return url




def sit():
    url = 'http://192.168.31.160:8004'
    return url

def sit_UaUser():
    url = 'http://192.168.31.160:8006'
    return url

def sit_YbUser():
    url = 'http://eims.sit.datoubao.com/eims'
    return url

def pre():
    url='http://192.168.31.160:8005'
    return url

def pre_UaUser():
    url = 'http://192.168.31.160:8007'
    return url


def pre_admin():
    url = 'http://'
    return url



def prd():

    url='http://114.55.236.197'

    return url


if __name__ == '__main__':
    list()