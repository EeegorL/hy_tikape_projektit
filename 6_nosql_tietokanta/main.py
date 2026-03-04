import pymongo;

connection_string = "mongodb+srv://tikape:NAq8a4pNLWF8TMfd@cluster0.u4vehy9.mongodb.net/"
client = pymongo.MongoClient(connection_string);

database = client.get_database("tikape");
apartments = database["apartments"];

postinro_00700 = apartments.count_documents({"zip_code": "00700"});
print(f'Monessako asunnossa postinumero on 00700? - {postinro_00700}');

rakennusvuosi_2000 = apartments.count_documents({"construction_year": {"$gte": 2000}});
print(f'Monessako asunnossa rakennusvuosi on 2000-luvulla? - {rakennusvuosi_2000}');

pinta_ala = apartments.count_documents({"apartment_size": {"$gte": 50, "$lte": 70}});
print(f'Monessako asunnossa pinta-ala on välillä 50–70 m²? - {pinta_ala}');

myyty_ainakin_kerran = apartments.count_documents({"transactions.date": {
    "$gte": "2010-01-01",
    "$lte": "2012-12-31"
        }
    }  
);
print(f'Moniko asunnoista on myyty ainakin kerran vuosina 2010–2012? - {myyty_ainakin_kerran}');

kallein = apartments.find_one({}, {"transactions": 1}, sort={"transactions.selling_price": -1});
kallein_hinta = max(kallein["transactions"], key=lambda x: x["selling_price"])["selling_price"];
print(f'Mikä on kallein asunnon myyntihinta aineistossa? - {kallein_hinta}');