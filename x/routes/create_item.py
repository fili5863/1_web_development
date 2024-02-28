from bottle import post, request
import x
import uuid
import random

####################
@post("/items")
def _():
    try:
        item_title = request.forms.get("item_title")
        item_id = uuid.uuid4().hex
        item_price = random.uniform(10.5, 999.99)
        db = x.db()
        q = db.execute("INSERT INTO items VALUES(?, ?, ?)", (item_id, item_title, item_price))
        db.commit()
        return f"""
        <template mix-target="#items" mix-top>
            <div>
            {item_title}
            </div>
        </template>
    """

    except Exception as ex:
        print(ex)

    finally:
        if "db" in locals(): db.close()