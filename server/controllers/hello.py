from models.hello import helloInput

def custom_hello(data: helloInput):
    greeting = " ".join([f"Hello, {data.name}" for _ in range(data.amount_times)]) 
    return greeting
