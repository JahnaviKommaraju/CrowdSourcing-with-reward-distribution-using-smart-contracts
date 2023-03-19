from flask import Flask,render_template,session,redirect,url_for,flash,get_flashed_messages
from functools import wraps
from user.models import *
import pymongo
import json
from bson import json_util
from bson.objectid import ObjectId
import final_transaction
from passlib.hash import pbkdf2_sha256
app = Flask(__name__)
app.secret_key = b'\x11\xca\xa8\xc8\xca\xfb\x84\xce\xbe\x85\xe5TG\x0c+\x8c'

client= pymongo.MongoClient('localhost',27017)
db= client.crowdSourceSystem

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/signup',methods=['POST'])
def signUp():
    return User().signUp()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login',methods=['POST'])
def login():
    return User().login()

@app.route('/requestorDashboard')
@login_required
def dashboard():
    return render_template('requestorDashboard.html')

@app.route('/workerDashboard')
@login_required
def worker():
    return render_template('workerDashboard.html')

@app.route('/requestorDashboard/<requestorID>/createTask',methods=['POST','GET'])
@login_required
def createTask(requestorID):
    if request.method=='POST':
        print(request.form)
        taskName= request.form['tName']
        taskDescription = request.form['tDescription']
        tAmount = request.form['tAmount']

        newtask={"requestorID":requestorID,
                "tName":taskName,
                "tDescription": taskDescription,
                "tAmount":int(tAmount),
                "reportIDs":[],
                "reportSubmitterAddress":[]
                }
        print(newtask)
        dbResponse=db.tasks.insert_one(newtask)
        db.requestors.update_one({'_id': requestorID},
                                {"$push":{
                                    "taskIDs": dbResponse.inserted_id
                                }}
        )
        return redirect(url_for('viewallTasksOfRequestor', rid= newtask['requestorID']))
    else:
        return render_template('createTask.html', rid= requestorID)


@app.route('/viewallTasksOfRequestor/<rid>',methods=['GET','POST'])
@login_required
def viewallTasksOfRequestor(rid):
    l=getTasks(rid)
    return render_template('viewallTasksOfRequestor.html', rid=rid, tasksList=l)

@app.route('/requestorDashboard/<requestorID>/viewTasks',methods=['GET'])
@login_required
def getTasks(requestorID):
    tasksList=[]
    data = list(db.tasks.find())
    for user in data:
        user["_id"] = str(user["_id"])

    for user in data:
        if user["requestorID"] == requestorID:
            tasksList.append(user)
    return tasksList

def getAllTasks():
    allTasks=[]
    data = list(db.tasks.find())
    for user in data:
        user["_id"] = str(user["_id"])

    for i in data:
        allTasks.append(i)

    return allTasks

@app.route('/workerDashboard/<wid>/viewTasks',methods=['GET','POST'])
@login_required
def viewAllTasksForWorker(wid):
    tasksList=getAllTasks()
    return render_template('viewAllTasksForWorker.html', wid=wid,tasksList=tasksList)

    
@app.route('/workerDashboard/<wid>/<tid>/<tName>/addReport', methods=['GET','POST'])
@login_required
def addReport(wid,tid,tName):
    if request.method=='POST':
        print(request.form)
        reportName= request.form['rName']
        reportContent = request.form['rContent']

        newReport={"workerID":wid,
                "reportName":reportName,
                "reportContent": reportContent,
                "reportAvgRating":"",
                "reviewReportIDs":[],
                "reviewSubmittedBy":[],
                "taskID":tid
                }
        print(newReport)
        print(wid,'||||',tid)
        worker_found = db.reports.find_one({"workerID":wid, 
                                        "taskID": tid  })
        print('--------') 
        print(worker_found)    
        print('--------')                            
        if worker_found:
            print(worker_found)
            flash("you have already submitted the report")
            return render_template('workerDashboard.html')
        dbResponse=db.reports.insert_one(newReport)
        updateTask=db.tasks.update_one({'_id': ObjectId(tid)},
                             {"$push":{
                                    "reportIDs": dbResponse.inserted_id,
                                    "reportSubmitterAddress":wid
                                }})
        print('updateTask',updateTask)
        updateWorker=db.workers.update_one({'_id': wid},
                                {"$push":{
                                    "reportIDs": dbResponse.inserted_id,
                                    "submittedTaskIDs": tid
                                }}
        )
        print('updateWorker',updateWorker)
        return redirect(url_for('viewallReportsOfWorker', wid= newReport['workerID']))
    else:
        return render_template('submitReport.html', tid=tid,wid=wid,tName=tName)


def getReportsOfWorker(wid):
    reportsList=[]
    data = list(db.reports.find())
    for user in data:
        user["_id"] = str(user["_id"])

    for user in data:
        if user["workerID"] ==wid:
            reportsList.append(user)
    return reportsList

@app.route('/viewallReportsOfWorker/<wid>',methods=['GET','POST'])
@login_required
def viewallReportsOfWorker(wid):
    l=getReportsOfWorker(wid)
    return render_template('viewallReportsOfWorker.html', wid=wid, reportsList=l)


def getReportsForWorker(wid):
    widData=[]
    rdata= list(db.reports.find())
    for user in rdata:
        if user["workerID"] == wid:
            widData.append(user)
    # print(widData)
    tIDS=[]
    for r in widData:
        tIDS.append(r["taskID"])
    # print('tIDS',tIDS)

    myData=[]
    wData= list(db.workers.find())
    for worker in wData:
        if worker["_id"] == wid:
            myData.append(worker)
    # print(wData)
    # print(myData)

    myreportIDs=[]
    for rIDList in myData:
        for id in rIDList['reportIDs']:
            myreportIDs.append(str(id))

    # print(myreportIDs)

    tdata= list(db.tasks.find())

    wSubmittedReportIDs=[]
    wSubmittedTaskdata=[]

    for id in tIDS:
        for task in tdata:
            if task["_id"] ==  ObjectId(id):
                wSubmittedReportIDs.append(task)
    # print('|||||||||||||||||||||')
    # print(wSubmittedReportIDs)      
    allreportsForTask=[]
    # print('|||||||||||||||||||||')
    for wtask in wSubmittedReportIDs:
        for id in wtask['reportIDs']:
            allreportsForTask.append(str(id))
    # print(allreportsForTask)

    reportIDsForWorkerReview = [x for x in allreportsForTask if x not in myreportIDs]
    # print(reportIDsForWorkerReview)

    return reportIDsForWorkerReview,tIDS


def getTaskDescription(tid):
    allTasks= list(db.tasks.find())
    # print(allTasks)
    for i in allTasks:
        if i['_id']== ObjectId(tid):
            return i['tDescription']
    print("--------------------------------")

@app.route('/workerDashboard/<wid>/viewReportsForReview',methods=['GET','POST'])
@login_required
def viewReportsForReview(wid):
    resReports=[]
    reportIDsList,tIDS= getReportsForWorker(wid)
    allReports= list(db.reports.find())
    for report in allReports:
        report["_id"] = str( report["_id"])

    # print(tasksList)
    for report in allReports:
        if report["_id"] in reportIDsList:
            resReports.append(report)

    # print(resReports)
    l=[]
    for report in resReports:
        rID= report['_id']
        rContent= report['reportContent']
        rTaskID= report['taskID']
        l.append({'rID':rID,'rContent':rContent,'rTaskID':rTaskID,'rTaskDescription':""})

    for i in l:
        i['rTaskDescription'] = getTaskDescription(i['rTaskID'])
    
    print(l)
    return render_template('viewReportsForReview.html', wid=wid, reviewReports=l)

@app.route('/workerDashboard/<wid>/<rTaskID>/<rID>/addReview',methods=['GET','POST'])
@login_required
def addReview(wid,rTaskID,rID):
    if request.method=="POST":
        print(request.form)
        reportRating = request.form['rRating']
        reportComment = request.form['rComment']

        newReview={"reportID": rID,
                    "workerID": wid,
                    "taskIDForReport":rTaskID,
                    "reportRating" : reportRating,
                    "reportComment": reportComment
                }

        

        print(newReview)

        worker_found = db.reviews.find_one({"workerID":wid, 
                                        "reportID":rID  })
        print('--------') 
        print(worker_found)    
        print('--------')                            
        if worker_found:
            print(worker_found)
            flash("you have already submitted the review")
            return render_template('viewReportsForReview.html')
        dbResponse=db.reviews.insert_one(newReview)
        updateReport=db.reports.update_one({'_id': ObjectId(rID)},
                             {"$push":{
                                    "reviewReportIDs": dbResponse.inserted_id,
                                    "reviewSubmittedBy":wid
                                }})
        print('updateReport',updateReport)
        updateWorker=db.workers.update_one({'_id': wid},
                                {"$push":{
                                    "reviewedReportIDs": dbResponse.inserted_id
                                }},
        )
        print('updateWorker',updateWorker)
        getReviewsOfReport(wid,rID)
        return redirect(url_for('viewallReportsOfWorker', wid= wid))
    return render_template('addReview.html',rid=rID,wid=wid)

def getAvgRatingOfReport():
    return

def getReviewsOfReport(wid,reportid):
    reviewsList=[]
    data = list(db.reviews.find())
    # print('hi',data)
    for user in data:
        user["_id"] = str(user["_id"])
    print('---------')
    for user in data: 
        if user["reportID"]==reportid:
            reviewsList.append(user)
    if len(reviewsList)>0:
        avgReportRating=0
        sumOfreportRating=0
        for review in reviewsList:
            sumOfreportRating+= int(review['reportRating'])
        
        avgReportRating=sumOfreportRating/len(reviewsList)
        print(avgReportRating)
        updateavgReportRating=db.reports.update_one({'_id': ObjectId(reportid)},
                                {"$set":{
                                        "reportAvgRating": avgReportRating
                                    }})
    return reviewsList



@app.route('/workerDashboard/<wid>/viewallReviewsOfReport/<reportid>',methods=['GET','POST'])
@login_required
def viewallReviewsOfReport(wid,reportid):
    reviewsList= getReviewsOfReport(wid,reportid)
    return render_template('viewallReviewsOfReport.html',wid=wid,reportid=reportid, reviewsList=reviewsList)

def getReportDetailsForTask(requestorId,taskid):
    reportDetailsList=[]
    reportData = list(db.reports.find())
    # workersData = list(db.workers.find())
    for i in reportData:
        if i['taskID'] == taskid:
            # workerWAdress=db.workers.find_one({'_id':i['workerID']})
            # print(workerWAdress['wAddress'])
            reportDetailsList.append(i)
            # print(i)
    print(reportDetailsList)
    return reportDetailsList

@app.route('/requestorDashboard/<rid>/viewallReportsOfTask/<taskid>',methods=['GET','POST'])
@login_required
def viewallReportsOfTask(rid,taskid):
    # reportDetailsList=getReportDetailsForTask(rid,taskid)
    data=getReportDetailsForTask(rid,taskid)
    eachTask= db.tasks.find_one({'_id':ObjectId(taskid)})
    reportAmounts= final_transaction.getReportRatings(data,eachTask['tAmount'])
    # workerWalletAddress= getReportDetailsForTask(rid,taskid)
    return render_template('viewallReportsOfTask.html',data=data,requestorId=rid, taskid=taskid,reportAmounts=reportAmounts)

@app.route('/<requestorId>/<rid>/sendReward/<rewardAmt>/<workerID>',methods=['GET','POST'])
@login_required
def sendReward(requestorId,rid,rewardAmt,workerID):
    workerWAdress=db.workers.find_one({'_id':workerID})
    requestorWAdress = db.requestors.find_one({'_id':requestorId})
    print(workerWAdress['wAddress'],requestorWAdress['wAddress'],rewardAmt)
    # amountTransaction(workerWAdress['wAddress'],requestorWAdress['wAddress'],rewardAmt)
    return render_template('sendReward.html',requestorId=requestorId,wAddress=workerWAdress['wAddress'],requestorWAdress=requestorWAdress['wAddress'],rewardAmt=rewardAmt,rid=rid,workerID=workerID)

@app.route('/amountTransaction/<wAddress>/<requestorWAdress>/<rewardAmt>',methods=['GET','POST'])
@login_required
def amountTransaction(wAddress,requestorWAdress,rewardAmt):
    # print(request.form)
    if request.method=='POST':
        print(wAddress,requestorWAdress,rewardAmt)
        print(request.form)
        privateKey=request.form['requestorPrivateKey']
        data=final_transaction.sendRewardAmt(wAddress,requestorWAdress,rewardAmt,privateKey)
        # request.form['requestorPrivateKey']=pbkdf2_sha256.encrypt(request.form.get('requestorPrivateKey'))
        print('----------------')
        print(data)
        return render_template('amountTransaction.html',data=data)
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=80,debug=True)