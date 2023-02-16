from flask import Flask,jsonify,request,session,redirect
from passlib.hash import pbkdf2_sha256
 
from app import db

class User:

    def start_session(self,user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        print('hi session')
        print(user)
        return jsonify(user),200
        
    def signUp(self):
        print('hi')
        print(request.form)
        name=request.form.get('name')
        email = request.form.get('email')
        id= email.split('@')[0]
        password = pbkdf2_sha256.encrypt(request.form.get('pwd'))
        wAdd = request.form.get('wAddress')
        userType = request.form.get('userType')
        emailExt = email.split('.')[1]
        if emailExt == "edu":
            newRequestor={
                "_id":id,
                "name":name,
                "email":email,
                "wAddress":wAdd,
                "password":password,
                "userType":userType,
                "taskIDs":[]
            }
            if db.requestors.find_one({"email": newRequestor['email']}):
                return jsonify({"error": "Email already in use"}),400

            if db.requestors.insert_one(newRequestor):
                return self.start_session(newRequestor)
                # return jsonify(user),200

        elif emailExt == "in":
            newWorker={
                "_id":id,
                "name":name,
                "email":email,
                "wAddress":wAdd,
                "password":password,
                "userType":userType,
                "reportIDs":[],
                "reviewedReportIDs":[],
                "submittedTaskIDs":[]
            }
            if db.workers.find_one({"email": newWorker['email']}):
                return jsonify({"error": "Email already in use"}),400

            if db.workers.insert_one(newWorker):
                return self.start_session(newWorker)
                # return jsonify(user),200
        
        return jsonify({"error": "SignUp failed"}),400
    
    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        print(request.form)
        email= request.form.get('email')
        emailExt = email.split('.')[1]
        print(email)
        print(emailExt)
        if emailExt == "edu":
            loginUser = db.requestors.find_one({
                "email" : request.form.get('email'),
                "userType": request.form.get('userType'),
            })
            try:
                loginUser['taskIDs'] = str(loginUser['taskIDs'])
                # loginUser['reviewedReportIDs'] = str(loginUser['reviewedReportIDs'])
            except TypeError:
                c=0

        elif emailExt == "in":
            loginUser = db.workers.find_one({
                "email" : request.form.get('email'),
                "userType": request.form.get('userType'),
            })
            try:
                loginUser['reportIDs'] = str(loginUser['reportIDs'])
                loginUser['reviewedReportIDs'] = str(loginUser['reviewedReportIDs'])
            except TypeError:
                c=0

        # for i in loginUser['taskIDs']:
        #     print(i)
        if loginUser and pbkdf2_sha256.verify(request.form.get('password'),loginUser['password']):
            return self.start_session(loginUser)
        
        return jsonify({"error": 'invalid login credentials'}),401
