from ckstyle.plugins.Base import *

class PluginClass(RuleChecker):
    def __init__(self):
        self.id = 'first-demo-plugin'
	self.errorLevel = ERROR_LEVEL.ERROR
	self.errorMsg = 'error message from demo plugin'
    
    def check(self, rule, config):
        return False
    
    def fix(self, rule, config):
        print 'fixing ' + rule.name
