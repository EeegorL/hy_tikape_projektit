class Relation:
    def __init__(self, fields):
        self.fields = fields;
        self.rows = [];

    def __str__(self):
        return str({x for x in self.rows});

    def add_tuple(self, tup):
        self.rows.append(tup);

def projection(rel, tup):
    indexes = [(rel.fields.index(tup))] if isinstance(tup, str) else [rel.fields.index(x) for x in tup];

    return {tuple(row[i] for i in indexes) for row in rel.rows}

if(__name__ == "__main__"):
    products = Relation(("id", "name", "price"))

    products.add_tuple((1, "retiisi", 7))
    products.add_tuple((2, "porkkana", 5))
    products.add_tuple((3, "nauris", 4))
    products.add_tuple((4, "lanttu", 8))
    products.add_tuple((5, "selleri", 4))

    # print(products)

    # print(projection(products, ("name")))
    # print(projection(products, ("price")))
    # print(projection(products, ("name", "price")))

    # - toimii tähän asti -

    # print(restriction(products, "name", "porkkana"))
    # print(restriction(products, "price", 4))

    # print(projection(restriction(products, "price", 4), ("name")))