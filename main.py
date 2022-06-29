from fastapi import FastAPI

app = FastAPI()

@app.post("/deliverActCode")
async def deliverActCode():
    return {"responseInfo": {
   "responseUID": "user0016-lgkj-7777-7777-123456789aze",
   "resultID": "ProceedWithSuccess",
   "errorCode": "00000",
   "errorDescription": "ProceedWithSuccess"
},
    "stepUpMethodExpirationTime": "2010-02-08T11:04:50.001Z",
    "activationCodeLength": "10"
}