from bwStudent import db, app
from flask import Flask, render_template, request, redirect, flash, url_for, views
from models import Student


# 创建数据库
# db.drop_all()
# db.create_all()

@app.route("/",endpoint="index")
def index():
    a = db.session.query(Student).all()
    b = len(a)
    return render_template("index.html",b=b)

@app.route("/append/",methods=['POST','GET'],endpoint="add")
def add_stu_infor():
    if request.method.lower() == "post":
        id_get = request.form.get("id")
        name_get = request.form.get("name")
        english_get = request.form.get("e_score")
        python_get = request.form.get("p_score")
        c_get = request.form.get("c")
        if id_get and name_get and english_get and python_get and c_get:
            score_num = int(english_get)+int(python_get)+int(c_get)
            stu_infor = Student(id=id_get,name=name_get,english=english_get,python=python_get,c=c_get,sum=score_num)
            db.session.add(stu_infor)
            db.session.commit()
            return render_template("add_stu.html",ok="添加成功")
        else:
            return render_template("add_stu.html",err="请检查是否有漏填")

    else:
        return render_template("add_stu.html")

@app.route("/find/",methods=["POST",'GET'],endpoint="find")
def find_stu_infor():
    if request.method.lower() == "post":
        get_cond = request.form.get("condation")
        get_cont = request.form.get("tiaojian")
        if get_cond == "学号":
            a = db.session.query(Student).filter(Student.id == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "姓名":
            a = db.session.query(Student).filter(Student.name == get_cont).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "english分数":
            a = db.session.query(Student).filter(Student.english == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "python分数":
            a = db.session.query(Student).filter(Student.python == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
        if get_cond == "C语言分数":
            a = db.session.query(Student).filter(Student.c == int(get_cont)).all()
            return render_template("find_stu.html",stu_list = a)
    return render_template("find_stu.html")

@app.route("/del/",methods=["POST","GET"],endpoint="del")
def dele_stu_infor():
    if request.method.lower() == "post":
        stu_num = request.form.get("stu_id")
        db.session.query(Student).filter(Student.id == int(stu_num)).delete()
        db.session.commit()
        return render_template("del_stu.html",of="学生信息删除成功")
    else:
        return render_template("del_stu.html")
@app.route("/alter/",methods=["POST","GET"],endpoint="alter")
def alter_stu_infor():
    if request.method.lower() == "post":
        id_get = request.form.get("id")
        get_cond = request.form.get("condation")
        get_cont = request.form.get("tiaojian")
        if get_cond == "姓名":
            db.session.query(Student).filter(Student.id == int(id_get)).update({"name":get_cont})
            db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
        if get_cond == "english分数":
            db.session.query(Student).filter(Student.id == int(id_get)).update({"english":int(get_cont)})
            db.session.commit()
            a = db.session.query(Student).filter(Student.id == int(id_get))
            for i in a:
                a1 = i.english
                a2 = i.python
                a3 = i.c
                a4 = a1+a2+a3
                db.session.query(Student).filter(Student.id == int(id_get)).update({"sum":a4})
                db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
        if get_cond == "python分数":
            db.session.query(Student).filter(Student.id == int(id_get)).update({"python":int(get_cont)})
            db.session.commit()
            a = db.session.query(Student).filter(Student.id == int(id_get))
            for i in a:
                a1 = i.english
                a2 = i.python
                a3 = i.c
                a4 = a1+a2+a3
                db.session.query(Student).filter(Student.id == int(id_get)).update({"sum":a4})
                db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
        if get_cond == "C语言分数":
            db.session.query(Student).filter(Student.id == int(id_get)).update({"c":int(get_cont)})
            db.session.commit()
            a = db.session.query(Student).filter(Student.id == int(id_get))
            for i in a:
                a1 = i.english
                a2 = i.python
                a3 = i.c
                a4 = a1+a2+a3
                db.session.query(Student).filter(Student.id == int(id_get)).update({"sum":a4})
                db.session.commit()
            return render_template("alter_stu.html",ok="修改成功")
    return render_template("alter_stu.html")

@app.route("/sort_stu/",methods=['POST','GET'],endpoint="sort_stu")
def stu_infor_sort():
    if request.method.lower() == "post":
        get_cond = request.form.get("condation")
        get_cont = request.form.get("condation1")
        b = Student.query.order_by(Student.english).all()
        for i in b:
            print(i.python)
        if get_cond == "english分数":
            if get_cont == "升序":
                a = Student.query.order_by(Student.english).all()
                # a = db.session.query(Student).order_by(Student.english).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = Student.query.order_by(Student.english.desc()).all()
                # a = db.session.query(Student).order_by(Student.english.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
        if get_cond == "python分数":
            if get_cont == "升序":
                a = db.session.query(Student).order_by(Student.python).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(Student).order_by(Student.python.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
        if get_cond == "C语言分数":
            if get_cont == "升序":
                a = db.session.query(Student).order_by(Student.c).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(Student).order_by(Student.c.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
        if get_cond == "总分":
            if get_cont == "升序":
                a = db.session.query(Student).order_by(Student.sum).all()
                return render_template("sort_stu.html",stu_list1=a)
            if get_cont == "降序":
                a = db.session.query(Student).order_by(Student.sum.desc()).all()
                return render_template("sort_stu.html",stu_list1=a)
    return render_template("sort_stu.html")
@app.route("/show_stu/",methods=['POST','GET'],endpoint="show_stu")
def show_all_stu():
    a = db.session.query(Student).all()
    return render_template("show_stu.html",stu_list1=a)
if __name__ == "__main__":
    API_HOST = "127.1.1.1"
    API_PORT = 5555
    app.run(API_HOST,API_PORT,debug=True)

