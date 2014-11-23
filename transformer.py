import json

def get_json(path):
    f = open(path, "r")
    json_content = json.loads(f.read())
    return json_content

def get_transformer(path):
    f = open(path, "r")
    json_content = json.loads(f.read())
    return json_content

class Transformer():
    def __init__(self):
        self.functions = {}
        self.json = None
        self.jsont = None

    def transform(self):
        if self.json is None or self.jsont is None:
            return "must implement"

        returned_dict = {}
        for key in self.jsont: 
            value = None 
            if "source" in self.jsont.get(key):
                value = self.compute_resource(key)
            if "value" in self.jsont.get(key):
                value = self.jsont.get(key).get("value")
            if "type" in self.jsont.get(key):
                value = self.cast_object(value, self.jsont.get(key).get("type"))
            if "format" in self.jsont.get(key):
                function_name = self.jsont.get(key).get("format")
                function = self.get_function(function_name)
                value = function(value)
            returned_dict.update({key: value}) 
        print returned_dict

    def get_cast_function(self, type):
        return {"int": int,"float":float}[type]

    def cast_object(self, value, type):
        function = self.get_cast_function(type)
        return function(value)
    
    def compute_resource(self, key):
        source = self.jsont.get(key).get("source")
        splited_source = source.split(":")
        source_value = None 
        for json_k in splited_source:
            try:
                json_k = int(json_k)
            except:
                pass
            if type(json_k) is int:
                if source_value is None:
                    print "should not be here"
                else:
                    source_value = source_value[json_k]
            else:
                if source_value is None:
                    source_value = self.json.get(json_k)
                else:
                    source_value = source_value.get(json_k)
        return source_value

    def add_function(self, name, function):
        self.functions.update({name: function})

    def get_function(self, function_name): 
        return self.functions[function_name]
