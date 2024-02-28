from bottle import put, request
import x

@put("/items/<id>")
def _(id):
    item_title = request.forms.get("update_item_title")
    item_price = request.forms.get("update_item_price")

    try:
        db = x.db()
        q = db.execute("UPDATE items SET item_title = ?, item_price = ? WHERE item_id = ?", (item_title, item_price, id))
        db.commit()
        return f"""
        <template mix-target="#the_item_title" mix-replace>
      
           <h1>ITEM NAME: {item_title}</h1>
      
        </template>
        <template mix-target="#the_item_price" mix-replace>
      
           <h1 id="the_item_price">ITEM PRICE: {item_price}</h1>
      
        </template>

        <template mix-target="#update_item_input" mix-replace>
      
             <input
            id="update_item_input"
            name="update_item_title"
            type="text"
            mix-check=".{2,20}"
            value="{item_title}"
            />
      
        </template>
        <template mix-target="#update_item_price_input" mix-replace>
      
             <input
            id="update_item_price_input"
            name="update_item_title"
            type="text"
            mix-check=".{2,20}"
            value="{item_price}"
            />
      
        </template>
    """
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()