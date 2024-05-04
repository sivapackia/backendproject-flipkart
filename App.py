from flask import Flask,render_template,redirect,url_for,session,request
from flask_mysqldb import MySQL
import re
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash,check_password_hash
from flask_bcrypt import check_password_hash

electric_list=[
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/k0lbdzk0pkrrdj/printer-refurbished/a/5/h/c-laserjet-m1005-mfp-hp-original-imafjfx2hvjhmysr.jpeg?q=80",
        "model":"Printers",
        "shop":"Shop Show"
    },
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/kokdci80/dslr-camera/v/e/x/z-24-200mm-z5-nikon-original-imag2zuekuxgxsgg.jpeg?q=80",
        "model":"Top Mirrorless Cameras",
        "shop":"Shop Show"
    },
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/xif0q/power-bank/d/a/f/-original-imagky3e8yp5ebvr.jpeg?q=80",
        "model":"Premium Power Banks",
        "shop":"Shop Show"
    },
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/xif0q/keyboard/gaming-keyboard/b/s/q/f2023-aula-original-imagnhc44uakb4zb.jpeg?q=80",
        "model":"Dell Keyboard",
        "shop":"Shop Show"
    },
      {
        "image":"https://rukminim2.flixcart.com/image/612/612/xif0q/trimmer/v/x/f/0-5-8-mm-hair-cutting-machine-for-men-beard-cutting-machine-hair-original-imagvyhs6xkq4u2z.jpeg?q=70",
        "model":"Best Of Shavers",
        "shop":"Shop Show"
    },
      {
        "image":"https://rukminim1.flixcart.com/image/210/210/ko8xtow0/monitor/t/a/y/d24-20-66aekac1in-lenovo-original-imag2qwzazcdmqtb.jpeg?q=80",
        "model":"Mointers",
        "shop":"Shop Show"
    }
    ]

beauty_list=[
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/jxz0brk0/stuffed-toy/n/t/s/4-feet-pink-very-beautiful-best-quality-for-special-gift-125-13-original-imafgv92puzkdytg.jpeg?q=80",
        "model":"Soft Toys",
        "shop":"Upto 70% Off"
    },
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/l58iaa80/electric-cycle/i/y/f/-original-imagfykthgudy4qz.jpeg?q=80",
        "model":"Electric Cycle",
        "shop":"Upto 40% Off"
    },
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/kzegk280/action-figure/9/v/t/3-30155-mcfarlane-2-5-original-imagbeyyzehpyk2m.jpeg?q=80",
        "model":"Best Of Action Toys",
        "shop":"Upto 60% Off"
    },
     {
        "image":"https://rukminim1.flixcart.com/image/210/210/k0plpjk0/remote-control-toy/9/g/k/4-function-remote-control-high-speed-big-racing-car-toy-funkey-original-imafkg33umd8dy93.jpeg?q=80",
        "model":"Remote Control Toys",
        "shop":"Upto 80% Off"
    },
      {
        "image":"https://rukminim1.flixcart.com/image/210/210/jlph9jk0/cycle/h/f/k/skyper-26t-sskp26bk0001-16-hero-original-imaf8ru5xysfgtmx.jpeg?q=80",
        "model":"Non-Geared Cycle",
        "shop":"Upto 70% Off"
    },
      {
        "image":"https://rukminim1.flixcart.com/image/210/210/kx50gi80/pen/h/z/k/119766-flair-original-imag9nzubznagufg.jpeg?q=80",
        "model":"Top Selling Stationery",
        "shop":"Upto 70% Off"
    }
    ]

kitchen_list=[
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/kirr24w0-0/wall-decoration/f/z/b/rafuf-wooden-intersecting-wall-shelves-set-of-8-black-white-8-original-imafyhg9dzdvyhnz.jpeg?q=80",
        "model":"Wall Dector Items",
        "shop":"Upto 80% Off" 
    },
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/k5e7o280/wall-clock/6/h/j/designer-wall-clock10-cw-ct-red25412-analog-ajanta-original-imafzyx3fdtf2hcb.jpeg?q=80",
        "model":"Clocks",
        "shop":"Upto 80% Off" 
    },
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/j5bceq80/diya/s/t/g/etl2042-etrendz-original-imaecayyx9nedubp.jpeg?q=80",
        "model":"Diyas Candle & Holders",
        "shop":"Upto 50% Off" 
    },
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/krtjgcw0/showpiece-figurine/q/8/d/sg-royalbox-original-imag5gy2rxubzkgq.jpeg?q=80",
        "model":"Showpieces",
        "shop":"Upto 75% Off" 
    }, 
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/l02r1jk0/bulb/j/e/o/motion-sensor-9w-01-philips-original-imagbxcabmu8yvhh.jpeg?q=80",
        "model":"Bulbs",
        "shop":"Upto 85% Off" 
    }, 
    {
        "image":"https://rukminim1.flixcart.com/image/210/210/kkmwr680/painting/y/x/r/42-sanfpnl31211-saf-original-imafzxvjzwepgfzc.jpeg?q=80",
        "model":"Paintings",
        "shop":"Upto 85% Off" 
    }
]

best_list=[
     {
        "image":"https://rukminim2.flixcart.com/image/250/250/xif0q/fabric/h/k/m/no-na-unstitched-na-febriccal056-hutah-original-imagtya2pqhd5z4a.jpeg?q=80",
        "model":"Womens Sarees",
        "shop":"Min 50% Off" 
    },
    {
        "image":"https://rukminim2.flixcart.com/image/250/250/xif0q/dslr-camera/e/h/v/dmc-g85kgw-k-16-dmc-g85kgw-k-panasonic-original-imagzknqpwukucj8.jpeg?q=80",
        "model":"DSLR & Mirrorless",
        "shop":"Min 30% Off" 
    },
    {
        "image":"https://rukminim2.flixcart.com/image/250/250/xif0q/headphone-pouch-case/j/u/t/silicone-press-stud-headphone-case-apl-original-imagz4x3npzfp9uy.jpeg?q=80",
        "model":"Headphones",
        "shop":"Min 50% Off" 
    },
    {
        "image":"https://rukminim2.flixcart.com/image/250/250/xif0q/t-shirt/c/8/x/xl-jawan-one-nb-nicky-boy-original-imagwbavcwbtznv5.jpeg?q=80",
        "model":"Mens T-Shirts",
        "shop":"Min 45% Off" 
    }
]

App=Flask(__name__)
App.secret_key="sivapackia"
App.config['MYSQL_HOST']='localhost'
App.config['MYSQL_USER']='root'
App.config['MYSQL_PASSWORD']='Rspk2822@'
App.config['MYSQL_DB']='flipkart'
App.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(App)
bcrypt=Bcrypt(App)

def islogin():
    return "SL_NO" in session

def hash_password_check(Password):
    if len(Password)<=4:
        return False
    if not re.search(r"[a-z]",Password) or not re.search(r"[A-Z]",Password):
        return False
    if not re.search(r"[!@#$%^&*()-+{}|\"<>]_?",Password) or not re.search(r"\d",Password):
        return False
    return True

@App.route("/")
def Home():
    return render_template("Home.html",data=electric_list,dataa=beauty_list,dataaa=kitchen_list,value=best_list)

@App.route("/Login",methods=["GET","POST"])
def Login():
    if request.method == "POST":
        Name=request.form.get("Name")
        Password=request.form.get("Password")
        cur=mysql.connection.cursor()
        cur.execute("SELECT  SL_NO,Name,Password FROM signup WHERE Name=%s",(Name,))
        data=cur.fetchone()
        if data and check_password_hash(data[2],Password):
            id=data[0]
            Name=data[1]
            Password=data[2]
            session["SL_NO"]=id
            return redirect(url_for('Home'))
        cur.connection.commit()
        cur.close()
    return render_template("Login.html")

@App.route("/Signup",methods=["GET","POST"])
def Signup():
    if request.method == "POST":
        Name=request.form.get("Name")
        Password=request.form.get("Password")
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM signup WHERE Name=%s",(Name,))
        data=cur.fetchone()
        cur.connection.commit()
        cur.close()
        if data:
            return "Already Name Is Exist"
        else:
            if not hash_password_check(Password):
                return "Check The Password Given Character"
            else:
                Hash_password=bcrypt.generate_password_hash(Password).decode('utf-8')
                cur=mysql.connection.cursor()
                cur.execute("INSERT INTO signup (Name,Password) VALUES(%s,%s)",(Name,Hash_password))
                cur.connection.commit()
                cur.close()
                return redirect(url_for('Login'))
    return render_template("Signup.html")

@App.route("/Login",methods=["GET","POST"])
def Logout():
    session.pop("SL_NO",None)
    return render_template("Login.html")

@App.route("/Component",methods=["GET","POST"])
def Component():
    cur=mysql.connection.cursor()
    cur.execute("select *from detail" )
    data=cur.fetchall()
    cur.connection.commit()
    cur.close()
    return render_template("Component.html",data=data)

@App.route("/Addtocard/<string:id>",methods=["GET","POST"])
def Addtocard(id):
    cur=mysql.connection.cursor()
    cur.execute("select *from detail where id=%s",(id,))
    data=cur.fetchone()
    cur.connection.commit()
    cur.close()
    return render_template("Addtocard.html",data=data)

@App.route("/Card",methods=["GET","POST"])
def Card():
    cur=mysql.connection.cursor()
    cur.execute("select *from addtocard")
    data=cur.fetchall()
    cur.connection.commit()
    sum=0
    for i in data:
        sum+=int(i["prize"])
    return render_template("Card.html",data=data,sum=sum)

@App.route("/Kannan/<string:id>",methods=["GET","POST"])
def Kannan(id):
    cur=mysql.connection.cursor()
    cur.execute("select *from detail where id=%s",(id,))
    data=cur.fetchone()
    cur.connection.commit()
    cur.close()

    cur=mysql.connection.cursor()
    cur.execute("select *from addtocard where id=%s",(id,))
    dataa=cur.fetchone()
    cur.connection.commit()
    cur.close()

    if dataa:
        return redirect(url_for('Card'))
    else:
        cur=mysql.connection.cursor()
        cur.execute("insert into addtocard (id,product_img,product_company,rating,view,flip_img,offer_prize,prize,offer) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)  ",(data["id"],data["product_img"],data["product_company"],data["rateing"],data["view"],data["flip_img"],data["offer_prize"],data["prize"],data["offer"]))
        cur.connection.commit()
        cur.close()
        return redirect(url_for('Card'))
    

@App.route("/Remove/<string:id>",methods=["GET","POST"])
def Remove(id):
    cur=mysql.connection.cursor()
    cur.execute("delete from addtocard where id=%s",(id,))
    cur.connection.commit()
    cur.close()
    return redirect(url_for('Card'))

if __name__ == "__main__":
    App.run(debug=True)