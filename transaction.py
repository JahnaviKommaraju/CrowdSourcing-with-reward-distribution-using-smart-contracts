from web3 import Web3
import decimal
ganache_url = "HTTP://127.0.0.1:7545"
web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
blockNumber = web3.eth.block_number
print(blockNumber)
r={"w1":4,"w2":5,"w3":1,"w4":5,"w5":2}
w={"w1":"0x2C0F2309353Bc39488441Cd26435BF9fc0eCD45B","w2":"0x7e40C15D4b6fD97514A0C129719e52D70d9E81f6","w3":"0x4a668be030C58C3A8623d0882c6704Bd601e7dBC","w4":"0xd74DC5ACe67a85F4EF21F1E1b722b1BdFd667eBe","w5":"0x836ef27e80980CfC4Fb552C549DC6eaC5F6DDDDb"}
# account_1= "0x78b0B460744F309Ca344697B83349daafed473D7"
account_2= "0x3124b53d988f3D715Dbc15352DF62F7222Bc4300"
private_key="76e4c8fb3a82517bd6faf8a86c0eac6be7a68563188fd9038690566eefbaf4e8"
#send crytp currency from actn1 to acunt2
##STEPS
#get the nonce 
budget=50.00
s=0
for i in w:
    s=s+r[i]
print(s)
a=budget/s
amount="{0:.2f}".format(a)
amount=float(amount)
print(amount)
for i in w:
    print(i)
    nonce = web3.eth.getTransactionCount(account_2)
    #build transaction
    print(w[i])
    n=amount*r[i]
    print(i+" worker got",n)
    account_1=w[i]
    ts= {
        'nonce': nonce, #nonce prevents u from sending transaction twice on ethereum 
        'to': account_1,
        'value': web3.toWei(n,'ether'),
        'gas': 2000000, #units of gas but not ethereum #compensation/cryptocurrency for miners on blockchain network
        'gasPrice': web3.toWei('50', 'gwei')
    }
    print(ts)
    #sign transaction
    signed_ts = web3.eth.account.signTransaction(ts,private_key)
    #send transaction
    ts_hash = web3.eth.sendRawTransaction(signed_ts.rawTransaction)
    #get transaction hash
    print(ts_hash) #binary format
    print(web3.toHex(ts_hash)) #Hex Format
print("transcation completed")
