
from flask import Flask, request, render_template, redirect, url_for, redirect, session, current_app
from flask import flash
from flask.helpers import total_seconds
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import time
import os
import pymongo
from pymongo import MongoClient
from pymongo import collection
import datetime
import pytz

from werkzeug.datastructures import iter_multi_items

cluster = MongoClient('mongodb+srv://verain111:OofOofKgn@cluster0.oggqb.mongodb.net/test?retryWrites=true&w=majority')


app = Flask(__name__)

imgFolder = os.path.join('img')

app.config['UPLOAD_FOLDER'] = imgFolder

app.secret_key = "your secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'foodordering'

order_list = list()
qty_list = list()
totalPrice_list = list()
price_list = list()
items_count = 0
opt = True
opt1 = True
totalBill = 0
quantity = []
QTY_list_me = []
dict_1 = dict()
Items_del = list()
item_id = list()

sr_list = []
Flist = []
foodCart = []
opt1 = False

mysql = MySQL(app)


@app.route("/mainpage", methods = ['POST', 'GET'])
def mainpage():
    global items_count
    global opt
    return render_template('mainpage.html', items_count = items_count)

@app.route("/SoyaSpecials", methods = ["GET", "POST"])
def SoyaSpecials():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""
    global dict_1

    
    if request.method == "POST" and 'ChaampTikkaQTY' in request.form:
        quantity1 = request.form["ChaampTikkaQTY"]

        if not quantity1:
            error_1 = "Enter a value"
        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chaamp Tikka"
                    price = 130
                    p_id = 101
                    totalPrice = quantity1 * price
                    error_1 = "Item added to the cart"

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                    

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChaampTikkaQTY")
                        Items_del.append("ChaampTikkaDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"
            else:
                error_1 = "Enter a valid quantity"
            
            

    
    if request.method == "POST" and 'AchariChaampQTY' in request.form:
        quantity2 = request.form["AchariChaampQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Achari Chaamp"
                    price = 130
                    p_id = 102
                    totalPrice = quantity2 * price
                    error_2 = "Item added to the cart"

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("AchariChaampQTY")
                        Items_del.append("AchariChaampDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"
            else:
                error_2 = "Enter a valid quantity"

    
    if request.method == "POST" and 'IraniChaampQTY' in request.form:
        quantity3 = request.form["IraniChaampQTY"]

        if not quantity3:
            error_4 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Irani Chaamp"
                    price = 130
                    p_id = 103
                    totalPrice = quantity3 * price
                    error_3 = "Item added to the cart"

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                      
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("IraniChaampQTY")
                        Items_del.append("IraniChaampDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"
            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'PudinaChaampQTY' in request.form:
        quantity4 = request.form["PudinaChaampQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Pudina Chaamp"
                    price = 130
                    p_id = 104
                    totalPrice = quantity4 * price
                    error_4 = "Item added to the cart"

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(price_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PudinaChaampQTY")
                        Items_del.append("PudinaChaampDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"
            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'CreamyChaampQTY' in request.form:
        quantity5 = request.form["CreamyChaampQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Creamy Chaamp"
                    price = 140
                    p_id = 105
                    totalPrice = quantity5 * price
                    error_5 = "Item added to the cart"

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(price_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CreamyChaampQTY")
                        Items_del.append("CreamyChaampDEL")
                        dict_1 = {p_id: {'name': dishName, 'price': price, 'quantity': quantity5,'totalPrice': totalPrice}}
                        items_count += 1
                        print(dict_1)
                        error_5 = "Item added to the cart"
            else:   
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'PlatterQTY' in request.form:
        quantity6 = request.form["PlatterQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():

                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    error_6 = "Item added to the cart"
                    dishName = "Tandoori Platter"
                    price = 180
                    p_id = 106
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(price_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PlatterQTY")
                        Items_del.append("PlatterDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'StuffedChaampQTY' in request.form:
        quantity7 = request.form["StuffedChaampQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Stuffed Chaamp"
                    price = 170
                    p_id = 107
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(price_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("StuffedChaampQTY")
                        Items_del.append("StuffedChaampDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)

    return render_template('SoyaSpecials.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7)
    #error_1 = error_1

@app.route("/Soups", methods = ["GET", "POST"])
def Soups():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'TomatoSoupQTY' in request.form:

        quantity1 = request.form["TomatoSoupQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Tomato Soup"
                    price = 70
                    p_id = 201
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("TomatoSoupQTY")
                        Items_del.append("TomatoSoupDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'SpinachSoupQTY' in request.form:
        quantity2 = request.form["SpinachSoupQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Spinach Soup"
                    price = 70
                    p_id = 202
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("SpinachSoupQTY")
                        Items_del.append("SpinachSoupDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'RiceWaterSoupQTY' in request.form:
        quantity3 = request.form["RiceWaterSoupQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Rice Water Soup"
                    price = 90
                    p_id = 203
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("RiceWaterSoupQTY")
                        Items_del.append("RiceWaterSoupDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"
            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'CreamAndCornSoupQTY' in request.form:
        quantity4 = request.form["CreamAndCornSoupQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Cream and Corn Soup"
                    price = 100
                    p_id = 204
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CreamAndCornSoupQTY")
                        Items_del.append("CreamAndCornSoupDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'CarrotSoupQTY' in request.form:
        quantity5 = request.form["CarrotSoupQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Carrot Soup"
                    price = 100
                    p_id = 205
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CarrotSoupQTY")
                        Items_del.append("CarrotSoupDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ManchowSoupQTY' in request.form:
        quantity6 = request.form["ManchowSoupQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Manchow Soup"
                    price = 110
                    p_id = 206
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ManchowSoupQTY")
                        Items_del.append("ManchowSoupDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'TomatoAndCornSoupQTY' in request.form:
        quantity7 = request.form["TomatoAndCornSoupQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Tomato And Corn Soup"
                    price = 120
                    p_id = 207
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("TomatoAndCornSoupQTY")
                        Items_del.append("TomatoAndCornSoupDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)



    return render_template('Soups.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7)

@app.route("/VegSnacks", methods = ["GET", "POST"])
def VegSnacks():
    
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'PaneerTikkaQTY' in request.form:

        quantity1 = request.form["PaneerTikkaQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Paneer Tikka"
                    price = 220
                    p_id = 301
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PaneerTikkaQTY")
                        Items_del.append("PaneerTikkaDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChillyPaneerQTY' in request.form:
        quantity2 = request.form["ChillyPaneerQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chilly Paneer"
                    price = 220
                    p_id = 302
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChillyPaneerQTY")
                        Items_del.append("ChillyPaneerDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"
            else:
                error_2 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'Paneer65QTY' in request.form:
        quantity3 = request.form["Paneer65QTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Paneer65"
                    price = 230
                    p_id = 303
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("Paneer65QTY")
                        Items_del.append("Paneer65QTY")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'VegKababQTY' in request.form:
        quantity4 = request.form["VegKababQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Veg Kabab"
                    price = 210
                    p_id = 304
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("VegKababQTY")
                        Items_del.append("VegKababDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'PaneerManchurianQTY' in request.form:
        quantity5 = request.form["PaneerManchurianQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"
                
                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Paneer Manchurian"
                    price = 230
                    p_id = 305
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PaneerManchurianQTY")
                        Items_del.append("PaneerManchurianDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'FalafelQTY' in request.form:
        quantity6 = request.form["FalafelQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Falafel"
                    price = 240
                    p_id = 306
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("FalafelQTY")
                        Items_del.append("FalafelDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'SamosaQTY' in request.form:
        quantity7 = request.form["SamosaQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Samosa"
                    price = 140
                    p_id = 307
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("SamosaQTY")
                        Items_del.append("SamosaDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"    

    if request.method == "POST" and 'FrenchFriesQTY' in request.form:
        quantity8 = request.form["FrenchFriesQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"
                
                else:
                    dishName = "French Fries"
                    price = 190
                    p_id = 308
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("FrenchFriesQTY")
                        Items_del.append("FrenchFriesDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"

            else:
                error_8 = "Enter a valid quantity"

    if request.method == "POST" and 'MomosQTY' in request.form:
        quantity9 = request.form["MomosQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"

                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Momos"
                    price = 140
                    p_id = 309
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MomosQTY")
                        Items_del.append("MomosDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"
            else:
                error_9 = "Enter a valid quantity"

    if request.method == "POST" and 'ChillyPotatoQTY' in request.form:
        quantity10 = request.form["ChillyPotatoQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chilly Potato"
                    price = 200
                    p_id = 310
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChillyPotatoQTY")
                        Items_del.append("ChillyPotatoDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"

            else:
                error_10 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)



    return render_template('VegSnacks.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10)

@app.route("/NonVegSnacks", methods = ["GET", "POST"])
def NonVegSnacks():
    
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'ChillyChickenQTY' in request.form:

        quantity1 = request.form["ChillyChickenQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"
                else:

                    dishName = "Chilly Chicken"
                    price = 380
                    p_id = 401
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChillyChickenQTY")
                        Items_del.append("ChillyChickenDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'Chicken65QTY' in request.form:
        quantity2 = request.form["Chicken65QTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken65"
                    price = 350
                    p_id = 402
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("Chicken65QTY")
                        Items_del.append("Chicken65DEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"        
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'ChickenManchurianQTY' in request.form:
        quantity3 = request.form["ChickenManchurianQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Manchurian"
                    price = 320
                    p_id = 403
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenManchurianQTY")
                        Items_del.append("ChickenManchurianDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChickenGarlicQTY' in request.form:
        quantity4 = request.form["ChickenGarlicQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Garlic"
                    price = 250
                    p_id = 404
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenGarlicQTY")
                        Items_del.append("ChickenGarlicDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'LemonChickenQTY' in request.form:
        quantity5 = request.form["LemonChickenQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Lemon Chicken"
                    price = 250
                    p_id = 405
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("LemonChickenQTY")
                        Items_del.append("LemonChickenDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'CrispyNonVegQTY' in request.form:
        quantity6 = request.form["CrispyNonVegQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Crispy Non-Veg"
                    price = 240
                    p_id = 406
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CrispyNonVegQTY")
                        Items_del.append("CrispyNonVegDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'BarBCueQTY' in request.form:
        quantity7 = request.form["BarBCueQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Bar-B-Cue"
                    price = 380
                    p_id = 407
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("BarBCueQTY")
                        Items_del.append("BarBCueDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"
    
    if request.method == "POST" and 'FishFingersQTY' in request.form:
        quantity8 = request.form["FishFingersQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Fish Fingers"
                    price = 260
                    p_id = 408
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("FishFingersQTY")
                        Items_del.append("FishFingersDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"

            else:
                error_8 = "Enter a valid quantity"

    if request.method == "POST" and 'FishTikkaQTY' in request.form:
        quantity9 = request.form["FishTikkaQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"
                
                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"
                
                else:
                    dishName = "Fish Tikka"
                    price = 280
                    p_id = 409
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("FishTikkaQTY")
                        Items_del.append("FishTikkaDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"

            else:
                error_9 = "Enter a valid quantity"

    if request.method == "POST" and 'GarlicFishQTY' in request.form:
        quantity10 = request.form["GarlicFishQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Garlic Fish"
                    price = 280
                    p_id = 410
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("GarlicFishQTY")
                        Items_del.append("GarlicFishDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"


            else:
                error_10 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)



    return render_template('NonVegSnacks.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10)
    #return render_template('NonVegSnacks.html')

@app.route('/VegPizza', methods = ['POST', 'GET'])
def VegPizza():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'MarghertiaQTY' in request.form:

        quantity1 = request.form["MarghertiaQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Marghertia Pizza"
                    price = 199
                    p_id = 501
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MarghertiaQTY")
                        Items_del.append("MarghertiaDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'DoubleCheeseMargheritaQTY' in request.form:
        quantity2 = request.form["DoubleCheeseMargheritaQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Double Cheese Margherita Pizza"
                    price = 300
                    p_id = 502
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("DoubleCheeseMarghertiaQTY")
                        Items_del.append("DoubleCheeseMarghertiaDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"        
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'FarmHouseQTY' in request.form:
        quantity3 = request.form["FarmHouseQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Farm House Pizza"
                    price = 320
                    p_id = 503
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("FarmHouseQTY")
                        Items_del.append("FarmHouseDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'PeppyPaneerQTY' in request.form:
        quantity4 = request.form["PeppyPaneerQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Peppy Paneer Pizza"
                    price = 395
                    p_id = 504
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PeppyPaneerQTY")
                        Items_del.append("PeppyPaneerDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'DeluxeVeggieQTY' in request.form:
        quantity5 = request.form["DeluxeVeggieQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Deluxe Veggie Pizza"
                    price = 450
                    p_id = 505
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("DeluxeVeggieQTY")
                        Items_del.append("DeluxeVeggieDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'PaneerMakhniQTY' in request.form:
        quantity6 = request.form["PaneerMakhniQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Paneer Makhni Pizza"
                    price = 395
                    p_id = 506
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PaneerMakhniQTY")
                        Items_del.append("PaneerMakhniDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'TandooriPaneerQTY' in request.form:
        quantity7 = request.form["TandooriPaneerQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Indi Tandoori Paneer Pizza"
                    price = 450
                    p_id = 507
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        price_list.append(price)
                        item_id.append(p_id)
                        totalPrice_list.append(totalPrice)
                        QTY_list_me.append("TandooriPaneerQTY")
                        Items_del.append("TandooriPaneerDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"

    return render_template('VegPizza.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6,  error_7 = error_7)

@app.route('/NonVegPizza', methods = ['POST', 'GET'])
def NonVegPizza():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'PepperBarBCueQTY' in request.form:

        quantity1 = request.form["PepperBarBCueQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Pepper Bar-B-Cue Pizza"
                    price = 305
                    p_id = 601
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PepperBarBCueQTY")
                        Items_del.append("PepperBarBCueDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChickenSausageQTY' in request.form:
        quantity2 = request.form["ChickenSausageQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Sausage Pizza"
                    price = 450
                    p_id = 602
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenSausageQTY")
                        Items_del.append("ChickenSausageDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"        
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'ChickenGoldenDelightQTY' in request.form:
        quantity3 = request.form["ChickenGoldenDelightQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Golden Delight Pizza"
                    price = 450
                    p_id = 603
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenGoldenDelightQTY")
                        Items_del.append("ChickenGoldenDelightDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChickenDominatorQTY' in request.form:
        quantity4 = request.form["ChickenDominatorQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Dominator Pizza"
                    price = 555
                    p_id = 604
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenDominatorQTY")
                        Items_del.append("ChickenDominatorDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'IndiChickenTikkaQTY' in request.form:
        quantity5 = request.form["IndiChickenTikkaQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Indi Chicken Tikka Pizza"
                    price = 550
                    p_id = 605
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("IndiChickenTikkaQTY")
                        Items_del.append("IndiChickenTikkaDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ChickenFiestaQTY' in request.form:
        quantity6 = request.form["ChickenFiestaQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Fiesta Pizza"
                    price = 450
                    p_id = 606
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenFiestaQTY")
                        Items_del.append("ChickenFiestaDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'NonVegSupremeQTY' in request.form:
        quantity7 = request.form["NonVegSupremeQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Non-Veg Supreme Pizza"
                    price = 555
                    p_id = 607
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("NonVegSupremeQTY")
                        Items_del.append("NonVegSupremeDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"

    return render_template('NonVegPizza.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6,  error_7 = error_7)

@app.route('/VegMainCourse', methods = ['POST', 'GET'])
def VegMainCourse():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'ChannaMasalaQTY' in request.form:

        quantity1 = request.form["ChannaMasalaQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Channa Masala"
                    price = 219
                    p_id = 701
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChannaMasalaQTY")
                        Items_del.append("ChannaMasalaDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'SoyaChaampGravyQTY' in request.form:
        quantity2 = request.form["SoyaChaampGravyQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Soya Chaamp Gravy"
                    price = 219
                    p_id = 702
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("SoyaChaampGravyQTY")
                        Items_del.append("SoyaChaampGravyDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"        
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'MalaiKoftaQTY' in request.form:
        quantity3 = request.form["MalaiKoftaQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Malai Kofta"
                    price = 229
                    p_id = 703
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        price_list.append(price)
                        item_id.append(p_id)
                        totalPrice_list.append(totalPrice)
                        QTY_list_me.append("MalaiKoftaQTY")
                        Items_del.append("MalaiKoftaDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'DalMakhniQTY' in request.form:
        quantity4 = request.form["DalMakhniQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Dal Makhni"
                    price = 239
                    p_id = 704
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("DalMakhniQTY")
                        Items_del.append("DalMakhniDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'MushroomMasalaQTY' in request.form:
        quantity5 = request.form["MushroomMasalaQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Mushroom Masala"
                    price = 239
                    p_id = 705
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MushroomMasalaQTY")
                        Items_del.append("MushroomMasalaDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'CheeseTomatoQTY' in request.form:
        quantity6 = request.form["CheeseTomatoQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Cheese Tomato"
                    price = 239
                    p_id = 706
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CheeseTomatoQTY")
                        Items_del.append("CheeseTomatoDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ShahiPaneerQTY' in request.form:
        quantity7 = request.form["ShahiPaneerQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Shahi Paneer"
                    price = 239
                    p_id = 707
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ShahiPaneerQTY")
                        Items_del.append("ShahiPaneerDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"
    
    if request.method == "POST" and 'PaneerLababdarQTY' in request.form:
        quantity8 = request.form["PaneerLababdarQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Paneer Lababdar"
                    price = 239
                    p_id = 708
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PaneerLababdarQTY")
                        Items_del.append("PaneerLababdarDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"

            else:
                error_8 = "Enter a valid quantity"

    if request.method == "POST" and 'PaneerTikkaMasalaQTY' in request.form:
        quantity9 = request.form["PaneerTikkaMasalaQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"

                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Paneer Tikka Masala"
                    price = 259
                    p_id = 709
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PaneerTikkaMasalaQTY")
                        Items_del.append("PaneerTikkaMasalaDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"

            else:
                error_9 = "Enter a valid quantity"

    if request.method == "POST" and 'PaneerButterMasalaQTY' in request.form:
        quantity10 = request.form["PaneerButterMasalaQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Paneer Butter Masala"
                    price = 269
                    p_id = 710
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PaneerButterMasalaQTY")
                        Items_del.append("PaneerButterMasalaDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"

            else:
                error_10 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)



    return render_template('VegMainCourse.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10)


@app.route('/NonVegMainCourse', methods = ['POST', 'GET'])
def NonVegMainCourse():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    error_11 = ""
    error_12 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'CreamChickenQTY' in request.form:

        quantity1 = request.form["CreamChickenQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Cream Chicken"
                    price = 490
                    p_id = 801
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CreamChickenQTY")
                        Items_del.append("CreamChickenDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ButterChickenQTY' in request.form:
        quantity2 = request.form["ButterChickenQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Butter Chicken"
                    price = 480
                    p_id = 802
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ButterChickenQTY")
                        Items_del.append("ButterChickenDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"        
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'ButterChickenBonelessQTY' in request.form:
        quantity3 = request.form["ButterChickenBonelessQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Butter Chicken Boneless"
                    price = 480
                    p_id = 803
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ButterChickenBonelessQTY")
                        Items_del.append("ButterChickenBonelessDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'KadhaiChickenQTY' in request.form:
        quantity4 = request.form["KadhaiChickenQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Kadhai Chicken"
                    price = 480
                    p_id = 804
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("KadhaiChickenQTY")
                        Items_del.append("KadhaiChickenDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ChickenTikkaMasalaQTY' in request.form:
        quantity5 = request.form["ChickenTikkaMasalaQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Tikka Masala"
                    price = 480
                    p_id = 805
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenTikkaMasalaQTY")
                        Items_del.append("ChickenTikkaMasalaDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ChickenKaliMirchQTY' in request.form:
        quantity6 = request.form["ChickenKaliMirchQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Kali Mirch"
                    price = 480
                    p_id = 806
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenKaliMirchQTY")
                        Items_del.append("ChickenKaliMirchDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ChickenCurryQTY' in request.form:
        quantity7 = request.form["ChickenCurryQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Curry"
                    price = 480
                    p_id = 807
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenCurryQTY")
                        Items_del.append("ChickenCurryDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"
    
    if request.method == "POST" and 'MuttonCurryQTY' in request.form:
        quantity8 = request.form["MuttonCurryQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "MuttonCurry"
                    price = 270
                    p_id = 808
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MuttonCurryQTY")
                        Items_del.append("MuttonCurryDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"

            else:
                error_8 = "Enter a valid quantity"

    if request.method == "POST" and 'MuttonRaraQTY' in request.form:
        quantity9 = request.form["MuttonRaraQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"

                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Mutton Rara"
                    price = 280
                    p_id = 809
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MuttonRaraQTY")
                        Items_del.append("MuttonRaraDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"

            else:
                error_9 = "Enter a valid quantity"

    if request.method == "POST" and 'RoganJoshQTY' in request.form:
        quantity10 = request.form["RoganJoshQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "RoganJosh"
                    price = 280
                    p_id = 810
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("RoganJoshQTY")
                        Items_del.append("RoganJoshDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"


            else:
                error_10 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)
    if request.method == "POST" and 'KeemaMutterQTY' in request.form:
        quantity11 = request.form["KeemaMutterQTY"]

        if not quantity11:
            error_11 = "Enter a value"
        else:
            if quantity11.isdigit():
                quantity11 = int(quantity11)
                if quantity11 <= 0:
                    error_11 = "Quantity should be over 0"

                elif quantity11 > 20:
                    error_11 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Keema Mutter"
                    price = 280
                    p_id = 811
                    totalPrice = quantity11 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity11
                        totalPrice_list[index] = totalPrice
                        error_11 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity11)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("KeemaMutterQTY")
                        Items_del.append("KeemaMutterDEL")
                        items_count += 1
                        error_11 = "Item added to the cart"

            else:
                error_11 = "Enter a valid quantity"

    if request.method == "POST" and 'EggCurryQTY' in request.form:
        quantity12 = request.form["EggCurryQTY"]

        if not quantity12:
            error_12 = "Enter a value"
        else:
            if quantity12.isdigit():
                quantity12 = int(quantity12)
                if quantity12 <= 0:
                    error_12 = "Quantity should be over 0"

                elif quantity12 > 20:
                    error_12 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Egg Curry"
                    price = 100
                    p_id = 812
                    totalPrice = quantity12 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity12
                        totalPrice_list[index] = totalPrice
                        error_12 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity12)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("EggCurryQTY")
                        Items_del.append("EggCurryDEL")
                        items_count += 1
                        error_12 = "Item added to the cart"

            else:
                error_12 = "Enter a valid quantity"

    return render_template('NonVegMainCourse.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10, error_11 = error_11, error_12 = error_12)


@app.route('/MilkShakes', methods = ['POST', 'GET'])
def MilkShakes():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    error_11 = ""
    error_12 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'CaramelOreoQTY' in request.form:

        quantity1 = request.form["CaramelOreoQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Caramel Oreo Shake"
                    price = 180
                    p_id = 901
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CaramelOreoQTY")
                        Items_del.append("CaramelOreoDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"
            else:
                error_1 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChocolateOreoQTY' in request.form:
        quantity2 = request.form["ChocolateOreoQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chocolate Oreo Shake"
                    price = 180
                    p_id = 902
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChocolateOreoQTY")
                        Items_del.append("ChocolateOreoDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"
            
            else:
                error_2 = "Enter a valid quantity"
                    
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'CoffeeOreoQTY' in request.form:
        quantity3 = request.form["CoffeeOreoQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Coffee Oreo Shake"
                    price = 180
                    p_id = 903
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CoffeeOreoQTY")
                        Items_del.append("CoffeeOreoDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"
            
            else:
                error_3 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'CoffeeHazelnutQTY' in request.form:
        quantity4 = request.form["CoffeeHazelnutQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Coffee Hazelnut Shake"
                    price = 180
                    p_id = 904
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CoffeeHazelnutQTY")
                        Items_del.append("CoffeeHazelnutDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"
            
            else:
                error_4 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'PeanutButterNutellaQTY' in request.form:
        quantity5 = request.form["PeanutButterNutellaQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Peanut Butter Nutella Shake"
                    price = 180
                    p_id = 905
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PeanutButterNutellaQTY")
                        Items_del.append("PeanutButterNutellaDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"
            
            else:
                error_5 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'RedVelvetQTY' in request.form:
        quantity6 = request.form["RedVelvetQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Red Velvet Shake"
                    price = 180
                    p_id = 906
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("RedVelvetQTY")
                        Items_del.append("RedVelvetDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"
            
            else:
                error_6 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'BlackChocolateForestQTY' in request.form:
        quantity7 = request.form["BlackChocolateForestQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Black Chocolate Forest Shake"
                    price = 180
                    p_id = 907
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("BlackChocolateForestQTY")
                        Items_del.append("BlackChocolateForestDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"
            else:
                error_7 = "Enter a valid quantity"

    
    if request.method == "POST" and 'BubbleGumQTY' in request.form:
        quantity8 = request.form["BubbleGumQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Bubble Gum Shake"
                    price = 180
                    p_id = 908
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("BubbleGumQTY")
                        Items_del.append("BubbleGumDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"
            
            else:
                error_8 = "Enter a valid quantity"


    if request.method == "POST" and 'BlackCurrantQTY' in request.form:
        quantity9 = request.form["BlackCurrantQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"

                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Black Currant Shake"
                    price = 180
                    p_id = 909
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("BlackCurrantQTY")
                        Items_del.append("BlackCurrantDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"
            else:
                error_9 = "Enter a valid quantity"


    if request.method == "POST" and 'AllBerryQTY' in request.form:
        quantity10 = request.form["AllBerryQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "All Berries Shake"
                    price = 180
                    p_id = 910
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("AllBerryQTY")
                        Items_del.append("AllBerryDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"

            else:
                error_10 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)
    if request.method == "POST" and 'VanillaCaramelQTY' in request.form:
        quantity11 = request.form["VanillaCaramelQTY"]

        if not quantity11:
            error_11 = "Enter a value"
        else:
            if quantity11.isdigit():
                quantity11 = int(quantity11)
                if quantity11 <= 0:
                    error_11 = "Quantity should be over 0"

                elif quantity11 > 20:
                    error_11 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Vanilla Caramel Shake"
                    price = 180
                    p_id = 911
                    totalPrice = quantity11 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity11
                        totalPrice_list[index] = totalPrice
                        error_11 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity11)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("VanillaCaramelQTY")
                        Items_del.append("VanillaCaramelDEL")
                        items_count += 1
                        error_11 = "Item added to the cart"

            else:
                error_11 = "Enter a valid quantity"

    if request.method == "POST" and 'TheChocolateMudPotQTY' in request.form:
        quantity12 = request.form["TheChocolateMudPotQTY"]

        if not quantity12:
            error_12 = "Enter a value"
        else:
            if quantity12.isdigit():
                quantity12 = int(quantity12)
                if quantity12 <= 0:
                    error_12 = "Quantity should be over 0"

                elif quantity12 > 20:
                    error_12 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "The Chocolate Mud Pot Shake"
                    price = 250
                    p_id = 912
                    totalPrice = quantity12 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity12
                        totalPrice_list[index] = totalPrice
                        error_12 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity12)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("TheChocolateMudPotQTY")
                        Items_del.append("TheChocolateMudPotDEL")
                        items_count += 1
                        error_12 = "Item added to the cart"

            else:
                error_12 = "Enter a valid quantity"
    return render_template('MilkShakes.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10, error_11 = error_11, error_12 = error_12)



@app.route('/Breads', methods = ['POST', 'GET'])
def Breads():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    error_11 = ""
    error_12 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'PlainRotiQTY' in request.form:

        quantity1 = request.form["PlainRotiQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"


                else:

                    dishName = "Plain Roti"
                    price = 8
                    p_id = 1001
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PlainRotiQTY")
                        Items_del.append("PlainRotiDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ButterRotiQTY' in request.form:
        quantity2 = request.form["ButterRotiQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Butter Roti"
                    price = 10
                    p_id = 1002
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ButterRotiQTY")
                        Items_del.append("ButterRotiDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"  

            else:
                error_2 = "Enter a valid quantity"      
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'MissiRotiQTY' in request.form:
        quantity3 = request.form["MissiRotiQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Missi Roti"
                    price = 20
                    p_id = 1003
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MissiRotiQTY")
                        Items_del.append("MissiRotiDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'RumaliRotiQTY' in request.form:
        quantity4 = request.form["RumaliRotiQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Rumali Roti"
                    price = 20
                    p_id = 1004
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("RumaliRotiQTY")
                        Items_del.append("RumaliRotiDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ButterRumaliRotiQTY' in request.form:
        quantity5 = request.form["ButterRumaliRotiQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Butter Rumali Roti"
                    price = 25
                    p_id = 1005
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ButterRumaliRotiQTY")
                        Items_del.append("ButterRumaliRotiDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'PlainNaanQTY' in request.form:
        quantity6 = request.form["PlainNaanQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Plain Naan"
                    price = 25
                    p_id = 1006
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PlainNaanQTY")
                        Items_del.append("PlainNaanDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"
            
            else:
                error_6 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ButterNaanQTY' in request.form:
        quantity7 = request.form["ButterNaanQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Butter Naan"
                    price = 30
                    p_id = 1007
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ButterNaanQTY")
                        Items_del.append("ButterNaanDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"

    
    if request.method == "POST" and 'GarlicNaanQTY' in request.form:
        quantity8 = request.form["GarlicNaanQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Garlic Naan"
                    price = 35
                    p_id = 1008
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("GarlicNaanQTY")
                        Items_del.append("GarlicNaanDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"

            else:
                error_8 = "Enter a valid quantity"


    if request.method == "POST" and 'LachhaParanthaQTY' in request.form:
        quantity9 = request.form["LachhaParanthaQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"

                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"


                else:
                    dishName = "Lachha Parantha"
                    price = 20
                    p_id = 1009
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("LachhaParanthaQTY")
                        Items_del.append("LachhaParanthaDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"

            else:
                error_9 = "Enter a valid quantity"


    if request.method == "POST" and 'PudinaParanthaQTY' in request.form:
        quantity10 = request.form["PudinaParanthaQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"


                else:
                    dishName = "PudinaParantha"
                    price = 20
                    p_id = 1010
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PudinaParanthaQTY")
                        Items_del.append("PudinaParanthaDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"

            else:
                error_10 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)
    if request.method == "POST" and 'CheeseNaanGravyQTY' in request.form:
        quantity11 = request.form["CheeseNaanGravyQTY"]

        if not quantity11:
            error_11 = "Enter a value"
        else:
            if quantity11.isdigit():
                quantity11 = int(quantity11)
                if quantity11 <= 0:
                    error_11 = "Quantity should be over 0"

                elif quantity11 > 20:
                    error_11 = "Sorry, quantity can't be over 20!"


                else:
                    dishName = "Cheese Naan Gravy"
                    price = 150
                    p_id = 1011
                    totalPrice = quantity11 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity11
                        totalPrice_list[index] = totalPrice
                        error_11 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity11)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CheeseNaanGravyQTY")
                        Items_del.append("CheeseNaanGravyDEL")
                        items_count += 1
                        error_11 = "Item added to the cart"

            else:
                error_11 = "Enter a valid quantity"

    if request.method == "POST" and 'KeemaNaanGravyQTY' in request.form:
        quantity12 = request.form["KeemaNaanGravyQTY"]

        if not quantity12:
            error_12 = "Enter a value"
        else:
            if quantity12.isdigit():
                quantity12 = int(quantity12)
                if quantity12 <= 0:
                    error_12 = "Quantity should be over 0"

                elif quantity12 > 20:
                    error_12 = "Sorry, quantity can't be over 20!"


                else:
                    dishName = "Keema Naan Gravy"
                    price = 190
                    p_id = 1012
                    totalPrice = quantity12 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity12
                        totalPrice_list[index] = totalPrice
                        error_12 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity12)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("KeemaNaanGravyQTY")
                        Items_del.append("KeemaNaanGravyDEL")
                        items_count += 1
                        error_12 = "Item added to the cart"

            else:
                error_12 = "Enter a valid quantity"


    return render_template('Breads.html', items_count  = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10, error_11 = error_11, error_12 = error_12)


@app.route('/Rice', methods = ['GET', 'POST'])
def Rice():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'VegBiryaniGravyQTY' in request.form:

        quantity1 = request.form["VegBiryaniGravyQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Veg Biryani with Gravy"
                    price = 220
                    p_id = 1101
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("VegBiryaniGravyQTY")
                        Items_del.append("VegBiryaniGravyDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChickenBiryaniGravyQTY' in request.form:
        quantity2 = request.form["ChickenBiryaniGravyQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Biryani with Gravy"
                    price = 270
                    p_id = 1102
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChickenBiryaniGravyQTY")
                        Items_del.append("ChickenBiryaniGravyDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"        
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'MuttonBiryaniGravyQTY' in request.form:
        quantity3 = request.form["MuttonBiryaniGravyQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chicken Biryani with Gravy"
                    price = 290
                    p_id = 1103
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MuttonBiryaniGravyQTY")
                        Items_del.append("MuttonBiryaniGravyDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"
                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'CheesePulaoGravyQTY' in request.form:
        quantity4 = request.form["CheesePulaoGravyQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Cheese Pulao with Gravy"
                    price = 240
                    p_id = 1104
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CheesePulaoGravyQTY")
                        Items_del.append("CheesePulaoGravyDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"
                        #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'PlainRiceQTY' in request.form:
        quantity5 = request.form["PlainRiceQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Plain Rice"
                    price = 120
                    p_id = 1105
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PlainRiceQTY")
                        Items_del.append("PlainRiceDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"
    return render_template('Rice.html', items_count = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5)


@app.route('/Beverages', methods = ['POST', 'GET'])
def Beverages():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    error_8 = ""
    error_9 = ""
    error_10 = ""
    error_11 = ""
    error_12 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'MineralWaterQTY' in request.form:

        quantity1 = request.form["MineralWaterQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Mineral Water"
                    price = 25
                    p_id = 1201
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("MineralWaterQTY")
                        Items_del.append("MineralWaterDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"
            
            else:
                error_1 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'ChaiQTY' in request.form:
        quantity2 = request.form["ChaiQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chai"
                    price = 35
                    p_id = 1202
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChaiQTY")
                        Items_del.append("ChaiDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"
            
            else:
                error_2 = "Enter a valid quantity"
                    
                        #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'CocaColaQTY' in request.form:
        quantity3 = request.form["CocaColaQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "CocaCola"
                    price = 40
                    p_id = 1203
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CocaColaQTY")
                        Items_del.append("CocaColaDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'SpriteQTY' in request.form:
        quantity4 = request.form["SpriteQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Sprite"
                    price = 40
                    p_id = 1204
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("SpriteQTY")
                        Items_del.append("SpriteDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"

            else:
                error_4 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ThumsUpQTY' in request.form:
        quantity5 = request.form["ThumsUpQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"
                
                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Thums Up"
                    price = 40
                    p_id = 1205
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ThumsUpQTY")
                        Items_del.append("ThumsUpDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'LimcaQTY' in request.form:
        quantity6 = request.form["LimcaQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Limca"
                    price = 40
                    p_id = 1206
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("LimcaQTY")
                        Items_del.append("LimcaDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"

            else:
                error_6 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'IceTeaLemonQTY' in request.form:
        quantity7 = request.form["IceTeaLemonQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Ice Tea Lemon"
                    price = 60
                    p_id = 1207
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("IceTeaLemonQTY")
                        Items_del.append("IceTeaLemonDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"

            else:
                error_7 = "Enter a valid quantity"

    
    if request.method == "POST" and 'IceTeaPeachQTY' in request.form:
        quantity8 = request.form["IceTeaPeachQTY"]

        if not quantity8:
            error_8 = "Enter a value"
        else:
            if quantity8.isdigit():
                quantity8 = int(quantity8)
                if quantity8 <= 0:
                    error_8 = "Quantity should be over 0"

                elif quantity8 > 20:
                    error_8 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Ice Tea Peach"
                    price = 60
                    p_id = 1208
                    totalPrice = quantity8 * price
                        
                    if dishName in order_list:
                            
                        index = order_list.index(dishName)
                        qty_list[index] = quantity8
                        totalPrice_list[index] = totalPrice
                        error_8 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity8)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("IceTeaPeachQTY")
                        Items_del.append("IceTeaPeachDEL")
                        items_count += 1
                        error_8 = "Item added to the cart"

            else:
                error_8 = "Enter a valid quantity"


    if request.method == "POST" and 'VirginMojitoQTY' in request.form:
        quantity9 = request.form["VirginMojitoQTY"]

        if not quantity9:
            error_9 = "Enter a value"
        else:
            if quantity9.isdigit():
                quantity9 = int(quantity9)
                if quantity9 <= 0:
                    error_9 = "Quantity should be over 0"

                elif quantity9 > 20:
                    error_9 = "Sorry, quantity can't be over 20!"


                else:
                    dishName = "Virgin Mojito"
                    price = 119
                    p_id = 1209
                    totalPrice = quantity9 * price
                            
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity9
                        totalPrice_list[index] = totalPrice
                        error_9 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity9)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("VirginMojitoQTY")
                        Items_del.append("VirginMojitoDEL")
                        items_count += 1
                        error_9 = "Item added to the cart"

            else:
                error_9 = "Enter a valid quantity"


    if request.method == "POST" and 'BlueLagoonQTY' in request.form:
        quantity10 = request.form["BlueLagoonQTY"]

        if not quantity10:
            error_10 = "Enter a value"
        else:
            if quantity10.isdigit():
                quantity10 = int(quantity10)
                if quantity10 <= 0:
                    error_10 = "Quantity should be over 0"

                elif quantity10 > 20:
                    error_10 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Blue Lagoon"
                    price = 129
                    p_id = 1210
                    totalPrice = quantity10 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity10
                        totalPrice_list[index] = totalPrice
                        error_10 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity10)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("BlueLagoonQTY")
                        Items_del.append("BlueLagoonDEL")
                        items_count += 1
                        error_10 = "Item added to the cart"

            else:
                error_10 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_7, qty = quantity7, dishName = dishName, totalPrice = totalPrice)
    if request.method == "POST" and 'PinkLadyQTY' in request.form:
        quantity11 = request.form["PinkLadyQTY"]

        if not quantity11:
            error_11 = "Enter a value"
        else:
            if quantity11.isdigit():
                quantity11 = int(quantity11)
                if quantity11 <= 0:
                    error_11 = "Quantity should be over 0"

                elif quantity11 > 20:
                    error_11 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Pink Lady"
                    price = 139
                    p_id = 1211
                    totalPrice = quantity11 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity11
                        totalPrice_list[index] = totalPrice
                        error_11 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity11)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PinkLadyQTY")
                        Items_del.append("PinkLadyDEL")
                        items_count += 1
                        error_11 = "Item added to the cart"

            else:
                error_11 = "Enter a valid quantity"

    if request.method == "POST" and 'SpicyGuavaQTY' in request.form:
        quantity12 = request.form["SpicyGuavaQTY"]

        if not quantity12:
            error_12 = "Enter a value"
        else:
            if quantity12.isdigit():
                quantity12 = int(quantity12)
                if quantity12 <= 0:
                    error_12 = "Quantity should be over 0"

                elif quantity12 > 20:
                    error_12 = "Sorry, quantity can't be over 20!"


                else:
                    dishName = "Spicy Guava"
                    price = 149
                    p_id = 1212
                    totalPrice = quantity12 * price
                            
                    if dishName in order_list:
                                
                        index = order_list.index(dishName)
                        qty_list[index] = quantity12
                        totalPrice_list[index] = totalPrice
                        error_12 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)
                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity12)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("SpicyGuavaQTY")
                        Items_del.append("SpicyGuavaDEL")
                        items_count += 1
                        error_12 = "Item added to the cart"

            else:
                error_12 = "Enter a valid quantity"


    return render_template('Beverages.html', items_count = items_count, error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7, error_8 = error_8, error_9 = error_9, error_10 = error_10, error_11 = error_11, error_12 = error_12)



@app.route('/Sundaes', methods = ['POST', 'GET'])
def Sundaes():
    error_1 = ""
    error_2 = ""
    error_3 = ""
    error_4 = ""
    error_5 = ""
    error_6 = ""
    error_7 = ""
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dishName = ""


    if request.method == "POST" and 'PeanutButterSundaeQTY' in request.form:

        quantity1 = request.form["PeanutButterSundaeQTY"]

        if not quantity1 :
            error_1 = "Enter a value"

        else:
            if quantity1.isdigit():
                quantity1 = int(quantity1)
                if quantity1 <= 0:
                    error_1 = "Quantity should be over 0"

                elif quantity1 > 20:
                    error_1 = "Sorry, quantity can't be over 20!"

                else:

                    dishName = "Peanut Butter Sundae"
                    price = 200
                    p_id = 1301
                    totalPrice = quantity1 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity1
                        totalPrice_list[index] = totalPrice
                        error_1 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity1)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("PeanutButterSundaeQTY")
                        Items_del.append("PeanutButterSundaeDEL")
                        items_count += 1
                        error_1 = "Item added to the cart"

            else:
                error_1 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_1, qty = quantity1, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'OreoSundaeQTY' in request.form:
        quantity2 = request.form["OreoSundaeQTY"]

        if not quantity2:
            error_2 = "Enter a value"
        else:
            if quantity2.isdigit():
                quantity2 = int(quantity2)
                if quantity2 <= 0:
                    error_2 = "Quantity should be over 0"

                elif quantity2 > 20:
                    error_2 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Oreo Sundae"
                    price = 200
                    p_id = 1302
                    totalPrice = quantity2 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity2
                        totalPrice_list[index] = totalPrice
                        error_2 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity2)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("OreoSundaeQTY")
                        Items_del.append("OreoSundaeDEL")
                        items_count += 1
                        error_2 = "Item added to the cart"

            else:
                error_2 = "Enter a valid quantity"
                    
                    #return render_template("sample.html", error_1 = error_2, qty = quantity2, dishName = dishName, totalPrice = totalPrice)
    

    
    if request.method == "POST" and 'ChocolateBrownieSundaeQTY' in request.form:
        quantity3 = request.form["ChocolateBrownieSundaeQTY"]

        if not quantity3:
            error_3 = "Enter a value"
        else:
            if quantity3.isdigit():
                quantity3 = int(quantity3)
                if quantity3 <= 0:
                    error_3 = "Quantity should be over 0"

                elif quantity3 > 20:
                    error_3 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chocolate Brownie Sundae"
                    price = 220
                    p_id = 1303
                    totalPrice = quantity3 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity3
                        totalPrice_list[index] = totalPrice
                        error_3 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity3)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChocolateBrownieSundaeQTY")
                        Items_del.append("ChocolateBrownieSundaeDEL")
                        items_count += 1
                        error_3 = "Item added to the cart"

            else:
                error_3 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_3, qty = quantity3, dishName = dishName, totalPrice = totalPrice)

    
    if request.method == "POST" and 'BananaSplitSundaeQTY' in request.form:
        quantity4 = request.form["BananaSplitSundaeQTY"]

        if not quantity4:
            error_4 = "Enter a value"
        else:
            if quantity4.isdigit():
                quantity4 = int(quantity4)
                if quantity4 <= 0:
                    error_4 = "Quantity should be over 0"

                elif quantity4 > 20:
                    error_4 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Banana Split Sundae"
                    price = 220
                    p_id = 1304
                    totalPrice = quantity4 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity4
                        totalPrice_list[index] = totalPrice
                        error_4 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity4)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("BananaSplitSundaeQTY")
                        Items_del.append("BananaSplitSundaeDEL")
                        items_count += 1
                        error_4 = "Item added to the cart"
            else:
                error_4 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_4, qty = quantity4, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'CaramelCornSundaeQTY' in request.form:
        quantity5 = request.form["CaramelCornSundaeQTY"]

        if not quantity5:
            error_5 = "Enter a value"
        else:
            if quantity5.isdigit():
                quantity5 = int(quantity5)
                if quantity5 <= 0:
                    error_5 = "Quantity should be over 0"

                elif quantity5 > 20:
                    error_5 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Caramel Corn Sundae"
                    price = 220
                    p_id = 1305
                    totalPrice = quantity5 * price

                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity5
                        totalPrice_list[index] = totalPrice
                        error_5 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity5)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("CaramelCornSundaeQTY")
                        Items_del.append("CaramelCornSundaeDEL")
                        items_count += 1
                        error_5 = "Item added to the cart"

            else:
                error_5 = "Enter a valid quantity"

                    #return render_template("sample.html", error_1 = error_5, qty = quantity5, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'ChocolateFudgeSundaeQTY' in request.form:
        quantity6 = request.form["ChocolateFudgeSundaeQTY"]

        if not quantity6:
            error_6 = "Enter a value"
        else:
            if quantity6.isdigit():
                quantity6 = int(quantity6)
                if quantity6 <= 0:
                    error_6 = "Quantity should be over 0"

                elif quantity6 > 20:
                    error_6 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Chocolate Fudge Sundae"
                    price = 230
                    p_id = 1306
                    totalPrice = quantity6 * price
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity6
                        totalPrice_list[index] = totalPrice
                        error_6 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity6)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("ChocolateFudgeSundaeQTY")
                        Items_del.append("ChocolateFudgeSundaeDEL")
                        items_count += 1
                        error_6 = "Item added to the cart"
            
            else:
                error_6 = "Enter a valid quantity"


                    #return render_template("sample.html", error_1 = error_6, qty = quantity6, dishName = dishName, totalPrice = totalPrice)


    if request.method == "POST" and 'RaspberryRoseSundaeQTY' in request.form:
        quantity7 = request.form["RaspberryRoseSundaeQTY"]

        if not quantity7:
            error_7 = "Enter a value"
        else:
            if quantity7.isdigit():
                quantity7 = int(quantity7)
                if quantity7 <= 0:
                    error_7 = "Quantity should be over 0"

                elif quantity7 > 20:
                    error_7 = "Sorry, quantity can't be over 20!"

                else:
                    dishName = "Raspberry Rose Sundae"
                    price = 230
                    p_id = 1307
                    totalPrice = quantity7 * price
                    
                    if dishName in order_list:
                        
                        index = order_list.index(dishName)
                        qty_list[index] = quantity7
                        totalPrice_list[index] = totalPrice
                        error_7 = "Item updated"
                        print(order_list)
                        print(qty_list)
                        print(totalPrice_list)

                    else:
                        order_list.append(dishName)
                        qty_list.append(quantity7)
                        totalPrice_list.append(totalPrice)
                        price_list.append(price)
                        item_id.append(p_id)
                        QTY_list_me.append("RaspberryRoseSundaeQTY")
                        Items_del.append("RaspberryRoseSundaeDEL")
                        items_count += 1
                        error_7 = "Item added to the cart"
            
            else:
                error_7 = "Enter a valid quantity"


    return render_template('Sundaes.html', items_count = items_count,error_1 = error_1, error_2 = error_2, error_3 = error_3, error_4 = error_4, error_5 = error_5, error_6 = error_6, error_7 = error_7)


@app.route('/Cart', methods = ["GET", "POST"])
def Cart():
    global sr_list
    global order_list
    global qty_list
    global price_list
    global totalPrice_list
    global QTY_list_me
    global Items_del
    global item_id
    #QTY_list_me= ['ChaampTikkaQTY', 'AchariChaampQTY']
    items_count = len(order_list)
    global totalBill

    if len(order_list) == 0:
        print("Empty")
        totalBill = 0
        return render_template('EmptyCart.html',items_count = items_count, item_id = item_id, QTY_list_me = QTY_list_me, sr_list = sr_list, totalBill = totalBill, order_list = order_list, qty_list = qty_list, price_list = price_list, totalPrice_list = totalPrice_list)
        

    else:
        print("SErial:     ", sr_list)
        totalBill = sum(totalPrice_list)
        return render_template('Cart.html',items_count = items_count, item_id = item_id, QTY_list_me = QTY_list_me, sr_list = sr_list, totalBill = totalBill, order_list = order_list, qty_list = qty_list, price_list = price_list, totalPrice_list = totalPrice_list)

    


@app.route('/update/<string:id>', methods=["POST"])
def update(id):
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    dbtn = False
    try :
        dbtn = request.form['deleteBTN'] and True
    except :
        dbtn = False
    if dbtn :
        print("I'm working")
        remove(int(id))
        return redirect(url_for('Cart'))

    print("###############", id, request.form)
    print(request.form[id])
    qty = request.form[id]
    print(qty)
    qty = int(qty)
    id = int(id)
    index1 = item_id.index(id)
    qty_list[index1] = qty

    totalPrice_list[index1] = qty * price_list[index1]
    #totalBill = sum(totalPrice_list)

    print(order_list)
    print(qty_list)
    print(totalPrice_list)
    print(totalBill)

    return redirect(url_for('Cart'))

def remove(id):
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    print("REMOVE",id)
    if id in item_id:
        index2 = item_id.index(id)
        item_id.pop(index2)
        order_list.pop(index2)
        qty_list.pop(index2)
        totalPrice_list.pop(index2)
        items_count = len(item_id)
        price_list.pop(index2)
        QTY_list_me.pop(index2)
        Items_del.pop(index2)

    # return redirect(url_for('Cart'))

@app.route("/cancelorder", methods=['POST', 'GET'])
def cancelorder():
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id
    order_list = []
    qty_list = []
    totalPrice_list = []
    items_count = 0
    price_list = []
    QTY_list_me = []
    Items_del = []
    item_id = []
    time.sleep(3)
    return redirect(url_for('mainpage'))

@app.route("/confirmorder", methods = ["POST", "GET"])
def confirmorder():
    print("Confirmed")
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id

    db = cluster["test"] #database name
    collection = db["test"]  #cluster name

    list_2 = []
    now = datetime.datetime.now()
    Date_time = now.strftime("%d-%m-%y %H:%M:%S")
    results = collection.find()
    for result in results:
        list_2.append(result)
        print(list_2)

    count = len(list_2)
    if count == 0:
        id = 1
        post = { "_id": id, "CustomerID": session['id'], "CustomerName": session['fullname'], "date": Date_time,"Order": order_list, "Quantity": qty_list, "Price": price_list, "TotalPrice": totalPrice_list, "TotalBill": totalBill}
        collection.insert_one(post)
    else:
        id = count + 1
        post = { "_id": id, "CustomerID": session['id'], "CustomerName": session['fullname'], "date": Date_time, "Order": order_list, "Quantity": qty_list, "Price": price_list, "TotalPrice": totalPrice_list, "TotalBill": totalBill}
        collection.insert_one(post)

    order_list = []
    qty_list = []
    totalPrice_list = []
    items_count = 0
    price_list = []
    QTY_list_me = []
    Items_del = []
    item_id = []
    time.sleep(3)
    return redirect(url_for('mainpage'))

@app.route('/updateorder', methods = ["POST", "GET"])
def updateorder():
    global order_list
    global qty_list
    global totalPrice_list
    global items_count
    global price_list
    global QTY_list_me
    global Items_del
    global item_id

    for i in item_id:
        print(i)
        quantity1 = request.form.get[i]
        #print(quantity1)
    return redirect(url_for('Cart'))

@app.route('/emptyCart', methods = ["POST", "GET"])
def emptyCart():
    time.sleep(3)
    return redirect(url_for('SoyaSpecials'))

@app.route('/PreviousOrders', methods = ['POST', 'GET'])
def PreviousOrders():
    db = cluster["test"] #database name    
    collection = db["test"]  #cluster name

    orders = []
    if session['id'] == 12:
        results = collection.find()
    else:
        results = collection.find({"CustomerID":session['id']})
    for result in results:
        orders.append(result)
    
    #print(orders)


    return render_template('PreviousOrders.html', orders = orders)



@app.route('/')
@app.route('/login', methods=["GET", "POST"])
def login():

    global opt1
    opt1 = True

    msg = ''
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:

        username = request.form.get("username")
        password = request.form.get("password")
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s and password = % s', (username, password))
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['fullname'] = account['fullname']
            session['age'] = account['age']
            session['phonenum'] = account['phonenum']
            #print(session)
            #msg = 'Logged in successfully'
            #return render_template('index.html', msg = msg)
            return render_template('mainpage.html')

        else:
            msg = 'Incorrect username/ password'

    return render_template('login.html', msg = msg) 




@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('fullname', None)
    session.pop('age', None)
    session.pop('password', None)

    sr_list = []
    Flist = []
    foodCart = []
    global order_list
    global qty_list
    global price_list
    global totalPrice_list
    global items_count
    items_count = 0

    order_list.clear()
    qty_list.clear()
    price_list.clear()
    totalPrice_list.clear()

    return redirect(url_for('login'))

@app.route("/register", methods = ["POST", "GET"])
def register():
    msg = ''
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        phonenum = request.form['phonenum']
        age = request.form['age']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', [username] )
        account = cursor.fetchone()

        
        if not username or not password or not username or not fullname or not phonenum or not age:
            msg = 'Please fill out the form !'



        elif len(password) < 6:
            msg = 'Password must be over 5 characters long!' 

        elif len(phonenum) != 10:
            msg = "Enter a valid phone number"


        elif len(password) > 15:
            msg = 'Password must not be over 15 characters long!'

        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'

        elif not re.search("[a-z]", password):
            msg = 'Password must contain atleast one lowercase letter!'

        elif not re.search("[A-Z]", password):
            msg = 'Password must contain atleast one uppercase letter!'

        elif not re.search("[0-9]", password):
            msg = 'Password must contain atleast one number!'

        elif re.search("[\s]", password):
            msg = 'Password cannot contain spaces'

        elif account:
            msg = 'Account already exists'


        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s)', [fullname, username, phonenum, age, password])
            mysql.connection.commit()
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg = msg)



#Driver Code
if __name__ == "__main__":
    app.run(debug=True)