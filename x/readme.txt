activate 
source bin/activate


Start server
sudo python -m bottle --server paste --bind 127.0.0.1:80 --debug --reload app

Start tailwind
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch




ROUTING/ROUTES

C - create
R - read
U - update
D - delete


/items                  GET - to get many items
/items/1                GET - to get one item
/items                  POST - create or save an item
/items/1                DELETE - to delete an item
/items/1                PUT or PATCH - to update the item

