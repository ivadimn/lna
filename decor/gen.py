from database.metadata import OrgsTable

class O:
    meta = OrgsTable
    fields = {key : val for key, val in OrgsTable.Columns.__dict__.items() if not key.startswith("__") }
    f1: str
    fr: str

print(O.meta.__dict__)
print(O.fields)
