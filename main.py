from transformer import Transformer, get_transformer, get_json

def fn(a):
    return a.lower()

class TransformerImplementation(Transformer):
#    def transform(self):
#        super(TransformerImplementation, self).transform()
    pass


t = TransformerImplementation()
t.add_function("fn", fn)
t.jsont= get_transformer("jsont.json")
t.json = get_json("json_to_transform.json")

t.transform()
