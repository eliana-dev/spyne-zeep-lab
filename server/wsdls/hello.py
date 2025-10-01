from spyne import ServiceBase, rpc
from models.hello import helloInput, helloOutput
from controllers.hello import custom_hello


class helloService(ServiceBase):
    @rpc(helloInput, _returns=helloOutput)
    def custom_greeting(ctx, data) -> helloOutput:
        print("Tu saludo:")
        greeting = custom_hello(data)
        output = helloOutput()
        output.result = greeting
        return output
