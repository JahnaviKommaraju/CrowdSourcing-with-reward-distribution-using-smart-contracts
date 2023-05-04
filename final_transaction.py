from web3 import Web3
import json
# import decimal
ganache_url = "HTTP://127.0.0.1:7545"
web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
# blockNumber = web3.eth.block_number
# # print(blockNumber)
# abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"string","name":"rname","type":"string"}],"name":"addReportEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tid","type":"uint256"},{"indexed":false,"internalType":"string","name":"tName","type":"string"}],"name":"addTaskEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"avgRating","type":"uint256"}],"name":"reviewReportEvent","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ReportIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"TaskIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalRating","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalwSubmittedReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"string","name":"rname","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"addReport","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"rAddress","type":"address"},{"internalType":"string","name":"tName","type":"string"},{"internalType":"string","name":"tDescription","type":"string"},{"internalType":"uint256","name":"minAmtForTask","type":"uint256"}],"name":"addTask","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllReportIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllTaskIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getAllWorkersForReport","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReport","outputs":[{"components":[{"internalType":"string","name":"reportName","type":"string"},{"internalType":"string","name":"reportContent","type":"string"},{"internalType":"address","name":"ReportCreatorAddress","type":"address"},{"internalType":"uint256","name":"avgRating","type":"uint256"},{"internalType":"uint256","name":"totalReviews","type":"uint256"},{"internalType":"address[]","name":"workers","type":"address[]"}],"internalType":"struct CrowdSource.Report","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReportAvgRating","outputs":[{"internalType":"string","name":"rname","type":"string"},{"internalType":"uint256","name":"avgrating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReportsSubmittedByWorker","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tid","type":"uint256"}],"name":"getTask","outputs":[{"components":[{"internalType":"string","name":"taskTitle","type":"string"},{"internalType":"string","name":"taskDescription","type":"string"},{"internalType":"address","name":"taskCreatorAddress","type":"address"},{"internalType":"uint256","name":"minAmt","type":"uint256"}],"internalType":"struct CrowdSource.Task","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rIdSubmittedByWorkerAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"uint256","name":"reportId","type":"uint256"},{"internalType":"uint256","name":"wRating","type":"uint256"},{"internalType":"string","name":"wComments","type":"string"}],"name":"reviewReport","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# address = web3.toChecksumAddress('0xBd2DeC728811241f867b9Fcc546B7008d4210134')
# contract  = web3.eth.contract(address=address, abi=abi)
reportRatings = {}
eachShare={}
def getReportRatings(data,tAmount):
    # print(data)
    # print(tAmount)
    totalRatingPoints=0
    for i in data:
        reportRatings[i['workerID']]= i['reportAvgRating']
        if i['reportAvgRating']!="":
            totalRatingPoints+=i['reportAvgRating']
    # print(reportRatings) #{'bob': 3.5, 'denny': 3.0, 'samhi': 4.0}
    # print(totalRatingPoints) #3.5 + 3 + 4 = 10.5

    for i in reportRatings:
        if reportRatings[i]!="":
            eachPercent=(reportRatings[i]/totalRatingPoints)*100
            eachShare[i]= float("{:.2f}".format(float("{:.2f}".format(eachPercent))/tAmount)) #{'bob': 3.33, 'denny': 2.86, 'samhi': 3.81}
    
    print(eachShare)
    return eachShare

print('hiiiiiiii')

def sendRewardAmt(workerWAddress,requestorWAdress,rewardAmt,privateKey):
    # print('hi')
    nonce = web3.eth.getTransactionCount(requestorWAdress)
    ts= {
        'nonce': nonce, #nonce prevents u from sending transaction twice on ethereum 
        'to': workerWAddress,
        'value': web3.toWei(rewardAmt,'ether'),
        'gas': 2000000, #units of gas but not ethereum #compensation/cryptocurrency for miners on blockchain network
        'gasPrice': web3.toWei('50', 'gwei')
    }
    print(ts)
    #sign transaction
    signed_ts = web3.eth.account.signTransaction(ts,privateKey)
    #send transaction
    ts_hash = web3.eth.sendRawTransaction(signed_ts.rawTransaction)
    #get transaction hash
    print(ts_hash) #binary format
    print(web3.toHex(ts_hash)) #Hex Format
    # print("transcation completed")
    return "transcation completed"

# workerData={'workerAddress':{},
#             'reportIdsOfWorker':None,
#             }

# reportData={'reportId':None,
#             'reportName':None,
#             'reportContent':None,
#             'reportAvgRating':None,
#             'reportTotalReviews':None,
#             'workersOfThisReport':None,
#             'reportReviewData':{}
# }


# def createTask(walletAddress,taskName,taskDescription,taskAmount):
#     # taskName = input('Enter Task Name: ')
#     # taskDescription = input('Enter task Description: ')
#     # taskAmount = int(input('Enter minimum amount for task: '))
#     web3.eth.defaultAccount = walletAddress
#     userAddress =web3.eth.defaultAccount
#     tAmt= int(taskAmount)
#     tx_hash = contract.functions.addTask(userAddress,taskName,taskDescription,tAmt).transact()
#     web3.eth.waitForTransactionReceipt(tx_hash)
#     print('Task successfully created')


# def getTask(tid):
#     task= contract.functions.getTask(tid).call()
#     print(task)
#     return task

# def getReportsCount(): #return integer
#     numOfReports=contract.functions.getTotalReports().call()
#     return numOfReports

# def getAllReportIds(): #returns list
#     report_ids= contract.functions.getAllReportIds().call()
#     # print('reports IDs are',report_ids)
#     return report_ids

# def getReportAvgRating(report_id):
#     reportRating = contract.functions.getReportAvgRating(report_id).call()
#     # reviewData['reportRating'] = reportRating
#     return reportRating 

# def getCurrentWorkerComments(report_id):
#     workerComments= contract.functions.getCurrentWorkerComments(report_id).call()
#     # reviewData['reportComments'] = workerComments
#     return workerComments

# def getCurrentWorkerRating():
#     report_id = input('Enter report_id: ')
#     workerRatings = contract.functions.getCurrentWorkerRating(report_id).call()
#     return workerRatings

# def getAnyWorkerComments():
#     worker_eth_address =  input('Enter eth address: ')
#     report_id = input('Enter report_id: ')
#     return contract.functions.getAnyWorkerComments(report_id, worker_eth_address).call()

# def getAnyWorkerRating():
#     worker_eth_address =  input('Enter eth address: ')
#     report_id = input('Enter report_id: ')
#     return contract.functions.getAnyWorkerRating(report_id, worker_eth_address).call()

# def getAllWorkersForReport():
#     report_id = input('Enter report_id: ')
#     allWorkers = contract.functions.getAllWorkersForReport(report_id).call()
#     return allWorkers

# def getReportIdsByWorkerAddress():
#     report_ids=contract.functions.getReportsSubmittedByWorker().call()
#     return report_ids

# def getWorkerCompleteData(wAddress):
#     workerData['workerAddress']=wAddress
#     rIdsOfWorker=getReportIdsByWorkerAddress()
#     workerData['reportIdsOfWorker'] = rIdsOfWorker
#     print(workerData)

# def addReport(walletAddress,reportName,reportContent):
#     web3.eth.defaultAccount = walletAddress
#     userAddress =web3.eth.defaultAccount
#     # reportName=input('Enter Report Name: ')
#     # reportContent = input('Enter response for report: ')
#     tx_hash = contract.functions.addReport(userAddress,reportName,reportContent).transact()
#     web3.eth.waitForTransactionReceipt(tx_hash)
#     print('Report successfully added')
#     print('New count of Reports: ', getReportsCount())

# reviewData={'reportRating':None,
#             'reportComments':None}

# def getReport(rid):
#     report=contract.functions.getReport(rid).call()
#     rName,rContent,rWorkerAddress,rAvgRating,rTotalReviews,rSubmittedWorkers=report
#     reviewData['reportRating'] = getReportAvgRating(rid)
#     reviewData['reportComments'] = getCurrentWorkerComments(rid)
#     reportData['reportId']=rid
#     reportData['reportName']=rName
#     reportData['reportContent']=rContent
#     reportData['reportAvgRating']=rAvgRating
#     reportData['reportTotalReviews']= rTotalReviews
#     reportData['workersOfThisReport']= rSubmittedWorkers
#     reportData['reportReviewData'] = reviewData
#     print(reportData)
#     return reportData


# # addReport()
# # getReportIdsByWorkerAddress()
# # getTask(111)

# def reviewReport(walletAddress,report_id,report_rating,report_feedback):
#     web3.eth.defaultAccount = walletAddress
#     userAddress =web3.eth.defaultAccount
#     # report_id = int(input('Enter report_id: '))
#     # print('Please review the report and rate it on scale of 1-5 and share feedback')
#     # print(getReport(report_id))
#     # report_rating = int(input('Enter rating: '))
#     # report_feedback = input('Enter feedback: ')
#     tx_hash = contract.functions.reviewReport(userAddress,report_id,report_rating,report_feedback).transact()
#     web3.eth.waitForTransactionReceipt(tx_hash)
#     print('Successfully reviewed the report')

# r={"w1":4,"w2":5,"w3":1,"w4":5,"w5":2}
# w={"w1":"0x2C0F2309353Bc39488441Cd26435BF9fc0eCD45B","w2":"0x7e40C15D4b6fD97514A0C129719e52D70d9E81f6","w3":"0x4a668be030C58C3A8623d0882c6704Bd601e7dBC","w4":"0xd74DC5ACe67a85F4EF21F1E1b722b1BdFd667eBe","w5":"0x836ef27e80980CfC4Fb552C549DC6eaC5F6DDDDb"}
# # account_1= "0x78b0B460744F309Ca344697B83349daafed473D7"
# account_2= "0x3124b53d988f3D715Dbc15352DF62F7222Bc4300"
# private_key="76e4c8fb3a82517bd6faf8a86c0eac6be7a68563188fd9038690566eefbaf4e8"
# #send crytp currency from actn1 to acunt2
# ##STEPS
# #get the nonce 
# budget=50.00
# s=0
# for i in w:
#     s=s+r[i]
# print(s)
# a=budget/s
# amount="{0:.2f}".format(a)
# amount=float(amount)
# print(amount)
# for i in w:
#     print(i)
#     nonce = web3.eth.getTransactionCount(account_2)
#     #build transaction
#     print(w[i])
#     n=amount*r[i]
#     print(i+" worker got",n)
#     account_1=w[i]
#     ts= {
#         'nonce': nonce, #nonce prevents u from sending transaction twice on ethereum 
#         'to': account_1,
#         'value': web3.toWei(n,'ether'),
#         'gas': 2000000, #units of gas but not ethereum #compensation/cryptocurrency for miners on blockchain network
#         'gasPrice': web3.toWei('50', 'gwei')
#     }
#     print(ts)
#     #sign transaction
#     signed_ts = web3.eth.account.signTransaction(ts,private_key)
#     #send transaction
#     ts_hash = web3.eth.sendRawTransaction(signed_ts.rawTransaction)
#     #get transaction hash
#     print(ts_hash) #binary format
#     print(web3.toHex(ts_hash)) #Hex Format
# print("transcation completed")
