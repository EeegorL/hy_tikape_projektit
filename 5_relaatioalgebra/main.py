class Relation:
    def __init__(self, fields):
        self.fields = fields;
        self.rows = [];

    def __str__(self):
        return str({tuple(x.values()) for x in self.rows});

    def add_tuple(self, tup):
        if(len(self.fields)) == 1:
            self.rows.append({self.fields: tup});
        else:
            self.rows.append({self.fields[i]: tup[i] for i in range(0, len(self.fields))})

def projection(dict, keysTup):
    if(isinstance(dict, Relation)): dict = dict.rows; # is an instance of Relation-class
    return {tuple([row[key] for key in row.keys() if(key in keysTup)]) for row in dict};

def restriction(dict, key, val):
    if(isinstance(dict, Relation)): dict = dict.rows; # is an instance of Relation-class
    return tuple([x for x in dict if(x[key] == val)]);
 
if(__name__ == "__main__"):
    products = Relation(("id", "name", "price"))

    products.add_tuple((1, "retiisi", 7))
    products.add_tuple((2, "porkkana", 5))
    products.add_tuple((3, "nauris", 4))
    products.add_tuple((4, "lanttu", 8))
    products.add_tuple((5, "selleri", 4))

    print(products)

    print(projection(products, ("name")))
    print(projection(products, ("price")))
    print(projection(products, ("name", "price")))

    print(restriction(products, "name", "porkkana"))
    print(restriction(products, "price", 4))

    print(projection(restriction(products, "price", 4), ("name")))