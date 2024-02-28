from bottle import delete
import x

##############################
@delete("/items/<id>")
def _(id):
    try:
        db = x.db()
        q = db.execute("DELETE FROM items WHERE item_id = ?", (id,))
        db.commit()
        return f"""
        <template mix-target="#item_{id}" mix-replace>
            <div mix-ttl="2000">
            <img class="w-full h-auto" src="./art.billyraycyrus.gi.jpeg" alt="">
        
            </div>
        </template>
        """
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()