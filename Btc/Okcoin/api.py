from client import Bihang

class BihangClient(Bihang):
    def __init__(self,http):
        self.http = http
    @staticmethod
    def api_secret(api_key, api_secret):
        return BihangClient(Bihang(api_key = api_key, api_secret = api_secret))  


    def addressesAddress(self, params=None):
        return self.http.get("addresses",params)



    def buttonsListButton(self, params=None):
        return self.http.get("buttons",params)



    def buttonsButton(self, params=None):
        return self.http.post("buttons",params)



    def createOrderButton(self, id,params=None):
        return self.http.post("buttons/%s/create_order" % id,params)



    def listOrderButton(self, id,params=None):
        return self.http.get("buttons/%s/orders" % id,params)



    def listContacts(self, params=None):
        return self.http.get("contacts",params)



    def testContacts(self, params=None):
        return self.http.post("contacts/test",params)



    def listNation(self, params=None):
        return self.http.get("nations",params)



    def applicationsOauth(self, params=None):
        return self.http.get("oauth/applications",params)



    def applicationOauth(self, id,params=None):
        return self.http.get("oauth/applications/%s" % id,params)



    def createApplicationsOauth(self, params=None):
        return self.http.post("oauth/applications",params)



    def listOrder(self, params=None):
        return self.http.get("orders",params)



    def createOrder(self, params=None):
        return self.http.post("orders",params)



    def detailOrder(self, id,params=None):
        return self.http.get("orders/%s" % id,params)



    def simpleTransaction(self, params=None):
        return self.http.get("transactions",params)



    def sendMoneyTransaction(self, params=None):
        return self.http.put("transactions/send_money",params)



    def requestMoneyTransaction(self, params=None):
        return self.http.put("transactions/request_money",params)



    def transactionDetailTransaction(self, id,params=None):
        return self.http.get("transactions/%s" % id,params)



    def payOrder4Step2Transaction(self, id,params=None):
        return self.http.put("transactions/%s/complete_send" % id,params)



    def cancelPayOrderTransaction(self, id,params=None):
        return self.http.put("transactions/%s/cancel_payorder" % id,params)



    def cancelPaymentOrderTransaction(self, id,params=None):
        return self.http.put("transactions/%s/cancel_send" % id,params)



    def cancelReceivePayOrderTransaction(self, id,params=None):
        return self.http.put("transactions/%s/cancel_request" % id,params)



    def userInfoUser(self, params=None):
        return self.http.get("users",params)



    def userBalanceUser(self, params=None):
        return self.http.get("users/balance",params)



    def registeUser(self, params=None):
        return self.http.post("users",params)



    def listWallet(self, params=None):
        return self.http.get("wallets",params)



    def deleteWallet(self, id,params=None):
        return self.http.delete("wallets/%s/delete" % id,params)



    def createWallet(self, params=None):
        return self.http.post("wallets",params)



    def setDefaultWallet(self, id,params=None):
        return self.http.put("wallets/%s/default" % id,params)



    def updateWallet(self, id,params=None):
        return self.http.put("wallets/%s/update" % id,params)



    def listDefaultWallet(self, params=None):
        return self.http.get("wallets/default",params)


