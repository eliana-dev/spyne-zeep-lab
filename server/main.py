from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from werkzeug.serving import run_simple
from wsdls.hello import helloService

# app spyne
lista_servicios = [helloService]  ##aca cargas todos los servicios
app = Application(
    lista_servicios,
    tns="urn:miempresa:hello",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

wsgi_app = WsgiApplication(app)
run_simple("localhost", 8000, wsgi_app)