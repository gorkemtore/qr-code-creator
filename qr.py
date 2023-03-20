import urllib.parse
import urllib.request

size = "500"
data = "google.com"

datas = {

    'size': size + "x" + size,
    'data' : data

}

parameters = urllib.parse.urlencode(datas)
api_link = "https://api.qrserver.com/v1/create-qr-code/?" + parameters
urllib.request.urlretrieve(api_link, "qr-code.png")