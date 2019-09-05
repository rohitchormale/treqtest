import treq
from twisted.internet import reactor


geturl = "http://localhost:5000/get"
posturl = "http://localhost:5000/post"


def done(result, test=""):
    def parse(res):
        print("%s | %s" %(test, res))
    # df = result.json()
    df = result.text()
    df.addBoth(parse)


def testAuthGetReq():
    auth = ("john", "john")
    df = treq.get(geturl, auth=auth)
    df.addBoth(done, test="authorized-get-req")


def testAuthPostReq():
    auth = ("john", "john")
    data = {"foo": "Bar", "baz": "baz"}
    df = treq.post(posturl, data=data, auth=auth)
    df.addBoth(done, test="authorized-post-req")


def testGetReq():
    auth = ("john", "johndafdas")
    df = treq.get(geturl, auth=auth)
    df.addBoth(done, test="UNAUTHORIZED-get-req")


def testPostReq():
    auth = ("john", "johndafdas")
    data = {"foo": "Bar", "baz": "baz"}
    df = treq.post(posturl, data=data, auth=auth)
    df.addBoth(done, test="UNAUTHORIZED-post-req")


if __name__ == "__main__":
    reactor.callLater(1, testGetReq)
    reactor.callLater(1, testPostReq)
    reactor.callLater(1, testAuthGetReq)
    reactor.callLater(1, testAuthPostReq)
    reactor.run()
