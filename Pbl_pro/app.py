from flask import Flask,flash,render_template,request,redirect,abort
from sqlalchemy import text
# from models import db,EmployeeModel
# from models import db,login_model
from models import db,sg
from ml_model import predict_college

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.route('/')
def firstpage():
    return render_template('fit.html')
@app.route('/firstpagecopy')
def firstpagecopy():
    return render_template('fit2.html') 
@app.route('/pro')
def pro():
    return render_template('profile.html') 
@app.route('/login')
def login():
    return render_template('signup.html')
@app.route('/feature')
def feature():
    return render_template('features.html')
@app.route('/login1')
def login1():
    return render_template('signup.html')
@app.route('/getstarted')
def getstarted():
    return render_template('get1.html')
@app.route('/getstarted/questions')
def getstartedforques():
    return render_template('home.html')
@app.route('/getstarted/quizques')
def quizz():
    return render_template('quiz_1.html')
@app.route('/getstarted/quizques/ans')
def fans():
    return render_template('final.html')
@app.route('/mlmodel')
def mlmodel():
    return render_template('mlhome.html')
@app.route('/comp')
def comp():
    return render_template('comp.html')
@app.route('/entc')
def entc():
    return render_template('entc.html')
@app.route('/mech')
def mech():
    return render_template('mech.html')
@app.route('/civil')
def civil():
    return render_template('civil.html')
@app.route('/getstarted/quizques', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        q1 = int(request.form['q1'])
        q2 = int(request.form['q2'])
        q3 = int(request.form['q3'])
        q4 = int(request.form['q4'])
        q5 = int(request.form['q5'])
        ce_score = q1 + q2 + q3 + q4 + q5
        q1 = int(request.form['q6'])
        q2 = int(request.form['q7'])
        q3 = int(request.form['q8'])
        q4 = int(request.form['q9'])
        q5 = int(request.form['q10'])
        ete_score = q1 + q2 + q3 + q4 + q5
        q1 = int(request.form['q11'])
        q2 = int(request.form['q12'])
        q3 = int(request.form['q13'])
        q4 = int(request.form['q14'])
        q5 = int(request.form['q15'])
        me_score = q1 + q2 + q3 + q4 + q5
        q1 = int(request.form['q16'])
        q2 = int(request.form['q17'])
        q3 = int(request.form['q18'])
        q4 = int(request.form['q19'])
        q5 = int(request.form['q20'])
        cev_score = q1 + q2 + q3 + q4 + q5
        max_score = max(ce_score, ete_score, me_score, cev_score)
        if ce_score == max_score:
            branch = 'Computer Engineering'
        elif ete_score == max_score:
            branch = 'Electronics and Telecommunication Engineering'
        elif me_score == max_score:
            branch = 'Mechanical Engineering'
        else:
            branch = 'Civil Engineering'
        
        return render_template('result_quiz.html', branch=branch)

    else:
        return render_template('quiz_1.html')

@app.route('/predict', methods=['POST'])
def predict_class():
    marks = request.form.get('cet_marks')
    branch = predict_college(float(marks))
    return render_template('final.html', branch=branch)
# @app.route('/ll/l')
# def ll():
#     return render_template('a1.html')

# @app.before_first_request
# def create_table():
#     db.create_all()
# @app.route('/login1/addback' , methods = ['GET','POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('a1.html')

#     if request.method == 'POST':
        
#         email = request.form['gmail']
#         pswd = request.form.get('pswd')
#         log = login_model(email=email, pswd=pswd)
#         db.session.add(log)
#         db.session.commit()
#         return redirect('/data')
# @app.route('/data')
# def RetrieveList():
#     employees = login_model.query.all()
#     return render_template('list_employees.html',employees = employees)
# @app.route('/data/<int:id>')
# def RetrieveEmployee(id):
#     employee =login_model.query.filter_by(employee_id=id).first()
#     if employee:
#         return render_template('data.html', employee = employee)
#     return f"Employee with id ={id} Doenst exist"
#################################################
@app.before_first_request
def create_table():
    db.create_all()
@app.route('/login' , methods = ['GET','POST'])
def create1():
    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST':
        txt = request.form['txt'] 
        e = request.form['e']
        p= request.form.get('p')
        log1= sg(txt=txt,e=e, p=p)
        db.session.add(log1)
        db.session.commit()
        flash("Data Added Succesfully")
        return redirect('/login1')
    # if request.method=="POST":
    #     usid=request.form['usid']
    #     pas=request.form['pas']
    #     sql = text('select e from signin')
    #     result = db.engine.execute(sql)
    #     names = [row[0] for row in result]
    #     if usid in names:
    #         print("u can cont")
    #         return render_template('fit2.html',usid=usid)
    #     else:
    #         print("register first")
            # return redirect('/login')
        # sql = text('select e from signin')
        # result = db.engine.execute(sql)
        # names = [row[0] for row in result]
        # print(names)
        
    

       
  
        

@app.route('/login1' , methods = ['GET','POST'])
def lll():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        usid=request.form['usid']
        pas=request.form['pas']
        sql = text('select txt from signin')
        sql2 = text('select p from signin')
        result = db.engine.execute(sql)
        result2 = db.engine.execute(sql2)
        names = [row[0] for row in result]
        names2 = [row[0] for row in result2]
        # return names
        dict={}
        for i in range(len(names)):
            dict[names[i]]=names2[i]
        # return dict
        if usid in names:
            print("u can cont")
            return render_template('fit2.html',usid=usid)
        else:
            print("register first")
            return redirect('/login1')
        
       

        
        
        
        
        
        

        
    
        
        # if usid in c:
        #     return redirect('/login')
        # else:
        #     print("register first")
    # return redirect('/getstarted')
        



    
        
@app.route('/data1')
def RetrieveList1():
    employees= sg.query.all()
    # return render_template('fit.html')
    return render_template('ls1.html',employees = employees)
# def RetrieveEmployee1(id1):
#     employee =sg.query.filter_by(employee_id=id1).first()
#     if employee:
#         return render_template('data1.html', employee = employee)
#     return f"Employee with id ={id1} Doenst exist"

# @app.route('/data/create' , methods = ['GET','POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('createpage.html')

#     if request.method == 'POST':
#         employee_id = request.form['employee_id']
#         name = request.form['name']
#         age = request.form['age']
#         position = request.form['position']
#         employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
#         db.session.add(employee)
#         db.session.commit()
#         return redirect('/data')


# @app.route('/data')
# def RetrieveList():
#     employees = EmployeeModel.query.all()
#     return render_template('datalist.html',employees = employees)


# @app.route('/data/<int:id>')
# def RetrieveEmployee(id):
#     employee = EmployeeModel.query.filter_by(employee_id=id).first()
#     if employee:
#         return render_template('data.html', employee = employee)
#     return f"Employee with id ={id} Doenst exist"


# @app.route('/data/<int:id>/update',methods = ['GET','POST'])
# def update(id):
#     employee = EmployeeModel.query.filter_by(employee_id=id).first()
#     if request.method == 'POST':
#         if employee:
#             db.session.delete(employee)
#             db.session.commit()
#             name = request.form['name']
#             age = request.form['age']
#             position = request.form['position']
#             employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
#             db.session.add(employee)
#             db.session.commit()
#             return redirect(f'/data/{id}')
#         return f"Employee with id = {id} Does nit exist"

#     return render_template('update.html', employee = employee)


# @app.route('/data/<int:id>/delete', methods=['GET','POST'])
# def delete(id):
#     employee = EmployeeModel.query.filter_by(employee_id=id).first()
#     if request.method == 'POST':
#         if employee:
#             db.session.delete(employee)
#             db.session.commit()
#             return redirect('/data')
#         abort(404)

#     return render_template('delete.html')

app.run(host='localhost', port=5000)