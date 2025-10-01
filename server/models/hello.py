from spyne import ComplexModel, Unicode, Integer

class helloInput(ComplexModel):
     name = Unicode(min_len=1, max_len=50, nullable=False)
     amount_times = Integer(min=1)

class helloOutput(ComplexModel):
    result = Unicode()