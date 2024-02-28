from bottle import get, template
import x

##############################
@get("/items/<id>")
def _(id):
    try:
        db = x.db()
        q = db.execute("SELECT * FROM items WHERE item_id = ?", (id,))
        item = q.fetchone()
        title = "item" + id
        return template('item', id=id, item_title=item["item_title"], title=title, item_price=item["item_price"])
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()

