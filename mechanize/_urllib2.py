# urllib2 work-alike interface
# ...from urllib2...
from urllib2 import \
     URLError, \
     HTTPError, \
     GopherError
# ...and from mechanize
from _opener import OpenerDirector, \
     build_opener, install_opener, urlopen, \
     OpenerFactory, urlretrieve
from _auth import \
     HTTPPasswordMgr, \
     HTTPPasswordMgrWithDefaultRealm, \
     AbstractBasicAuthHandler, \
     AbstractDigestAuthHandler, \
     HTTPProxyPasswordMgr, \
     ProxyHandler, \
     ProxyBasicAuthHandler, \
     ProxyDigestAuthHandler, \
     HTTPBasicAuthHandler, \
     HTTPDigestAuthHandler, \
     HTTPSClientCertMgr
from _urllib2_support import \
     Request, \
     RobotExclusionError

# handlers...
# ...from urllib2...
from urllib2 import \
     BaseHandler, \
     HTTPDefaultErrorHandler, \
     UnknownHandler, \
     FTPHandler, \
     CacheFTPHandler, \
     FileHandler, \
     GopherHandler
# ...and from mechanize
from _urllib2_support import \
     HTTPHandler, \
     HTTPRedirectHandler, \
     HTTPEquivProcessor, \
     SeekableProcessor, \
     HTTPCookieProcessor, \
     HTTPRefererProcessor, \
     HTTPRefreshProcessor, \
     HTTPErrorProcessor, \
     HTTPRobotRulesProcessor
from _upgrade import \
     HTTPRequestUpgradeProcessor, \
     ResponseUpgradeProcessor
from _debug import \
     HTTPResponseDebugProcessor, \
     HTTPRedirectDebugProcessor
# crap ATM
## from _gzip import \
##      HTTPGzipProcessor
import httplib
if hasattr(httplib, 'HTTPS'):
    from _urllib2_support import HTTPSHandler
del httplib