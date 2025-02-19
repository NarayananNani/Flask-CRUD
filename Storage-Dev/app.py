import uuid
from flask import Flask, request
from db import db, StoreModel


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.get("/all_stores")
def all_stores():
    stores = StoreModel.query.all()
    store_list = []
    for store in stores:
        store = {"name":store.name, "id":store.id}
        store_list.append(store)
    return store_list

@app.post("/add_store")
def add_store():
    json_body = request.get_json()
    store_id = uuid.uuid4().hex
    store = StoreModel(**json_body, id=store_id)
    db.session.add(store)
    db.session.commit()
    store = StoreModel.query.get(store_id)
    return {"name":store.name, "id":store.id}

@app.get("/specific_store/<id>")
def specific_store(id):
    store = StoreModel.query.get(id)
    return {"name":store.name, "id":store.id}

@app.put("/update_store/<id>")
def update_store(id):
    json_body = request.get_json()
    store = StoreModel.query.get(id)
    store.name = json_body["name"]
    store = StoreModel.query.get(id)
    return {"name":store.name, "id":store.id}

@app.delete("/delete_store/<id>")
def delete_store(id):
    store = StoreModel.query.get(id)
    db.session.delete(store)
    db.session.commit()
    return {"msg":"Store is deleted"}

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)