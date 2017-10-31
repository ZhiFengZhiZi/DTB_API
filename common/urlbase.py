

def UA_USER_url():

    #url=prelist()[1]
    url = sitlist()[1]

    return url

def UA_url():

    #url=prelist()[0]
    url = sitlist()[0]

    return url



def sitlist():

    url=['http://192.168.31.160:8004','http://192.168.31.160:8006']

    return url



def prelist():
    url = ['http://192.168.31.160:8005', 'http://192.168.31.160:8007']

    return url



if __name__ == '__main__':
    list()