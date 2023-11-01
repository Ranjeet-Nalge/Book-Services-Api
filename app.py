import json
from config import app, db
from flask import request
from models import Book



@app.route('/book/api',methods = ['GET'])
def book_list():
    book_list = Book.query.all()  # select * from book
    json_booklist = []
    if book_list:
        for bk in book_list:
            json_booklist.append({"BOOK-ID": bk.id, "BOOK-NAME": bk.name, "BOOK-VENDER": bk.vender,
                                  "BOOK-LANG": bk.lang, "BOOK-PRICE": bk.price, "BOOK-AUTHOR": bk.author})
    return json.dumps(json_booklist)

@app.route('/book/api',methods = ['POST'])
def book_add():
    reqdata = request.get_json()
    if reqdata:
        try:
            bk = Book(name=reqdata.get("BOOK-NAME"),
                           vender=reqdata.get("BOOK-VENDER"),
                           lang=reqdata.get("BOOK-LANG"),
                           price=reqdata.get("BOOK-PRICE"),
                           author=reqdata.get("BOOK-AUTHOR"))
            db.session.add(bk)
            db.session.commit()
            return json.dumps({"SUCCESS": f"Book {bk.id} Successfully added...!"})
        except BaseException as e:
            print(e.args)
    return json.dumps({"ERROR": f"Problem in Adding an Book"})


@app.route('/book/api/<int:bkid>',methods = ['DELETE'])
def book_delete(bkid):
    if bkid > 0:
        record = Book.query.filter_by(id=bkid).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return json.dumps({"SUCCESS": f"Book removed Successfully...!"})
        else:
            return json.dumps({"ERROR": f"No Record with Given id for Delete "})
    else:
        return json.dumps({"ERROR": f"Invalid ID"})


@app.route('/book/api/<int:bkid>',methods = ['PUT'])
def book_update(bkid):
    record = Book.query.filter_by(id=bkid).first()
    if record:
        reqdata = request.get_json()
        record.name = reqdata.get("BOOK-NAME")
        record.price = reqdata.get("BOOK-PRICE")
        record.vender = reqdata.get("BOOK-VENDER")
        db.session.commit()
        return json.dumps({"SUCCESS": f"Book {record.name} Updated Successfully...!"})
    else:
        return json.dumps({"ERROR": f"No Record with Given ID for Update "})


@app.route('/book/api/<int:bkid>',methods = ['GET'])
def book_search(bkid):
    book = Book.query.filter_by(id=bkid).first()
    if book:
        return json.dumps({"BOOK-ID": book.id, "Book_NAME": book.name, "BOOK-VENDER": book.vender,
                           "BOOK-LANG": book.lang, "BOOK-PRICE": book.price, "BOOK-AUTHOR": book.author})
    return json.dumps({"ERROR": f"No Record with Given ID NO.{bkid} for Search"})



@app.route('/book/api/<string:bkname>',methods = ['GET'])
def book_search_by_name(bkname):
    book = Book.query.filter_by(name=bkname).first()
    if book:
        return json.dumps({"BOOK-ID": book.id, "Book_NAME": book.name, "BOOK-VENDER": book.vender,
                           "BOOK-LANG": book.lang, "BOOK-PRICE": book.price, "BOOK-AUTHOR": book.author})
    return json.dumps({"ERROR": f"No Record with Given Name {bkname} for Search"})





if __name__ == '__main__':
    app.run(debug=True)
