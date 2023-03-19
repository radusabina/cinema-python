from Tests.testDomain import testAllDomains
from Tests.testRepository import testAllRepositories
from Tests.testService import testAllServices


def testAll():
    testAllDomains()
    testAllServices()
    testAllRepositories()
