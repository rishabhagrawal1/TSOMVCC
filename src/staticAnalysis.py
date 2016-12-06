import sys
import message
import json

##Object of attribute versions to be used in latestVersion and latestVersionBefore
class StaticAnalysis:

    def __init__(self, attr_file):
        self.attr_file = attr_file  
        self.attr_data = None
        
    def loadAttrFileObj(self):  
        try:    
            if(os.path.exists(attr_file)):
                with open(attr_file, encoding='utf-8') as attrs:
                    self.attr_data = json.loads(attrs.read())
        except:
            output("Error in reading Attribute file")

    def mightWriteObj(self, req):
        req_attr = dir(req)
        result_set = set()
        for element in self.attr_data['attribute_properties']:
            if(element.keys() in req_attr and element.values[0][1]['write'] = 'mutable'):
                result_set.add(element.values[0][2]['obj'])
        return result_set
        
   def defReadAttr(self, x, req):
        req_attr = dir(req)
        result_set = set()
        for element in self.attr_data['attribute_properties']:
            if(element.keys() in req_attr and element.values[0][2]['obj'] == x and element.values[0][0]['read'] = 'def'):
                result_set.add(element.keys())
        return result_set
    
    def mightReadAttr(self, x, req):
        req_attr = dir(req)
        result_set = set()
        for element in self.attr_data['attribute_properties']:
            if(element.keys() in req_attr and element.values[0][2]['obj'] == x and element.values[0][0]['read'] = 'might'):
                result_set.add(element.keys())
        return result_set
        
    def mightWriteAttr(self, x, req):
        req_attr = dir(req)
        result_set = set()
        for element in self.attr_data['attribute_properties']:
            if(element.keys() in req_attr and element.values[0][2]['obj'] == x and element.values[0][1]['write'] = 'mutable'):
                result_set.add(element.keys())
        return result_set
        
    def obj(self, req, i):
        result = 'sub'
        result_set = mightWriteObj(self, req)
        if(len(result_set) == 1):
            if(next(iter(s)) == 'sub' and i == 1):
                result = 'res'
            elif(next(iter(s)) == 'res' and i == 2):
                result = 'res'
        else:
            if(i == 2):
                result = 'res'
        return result
        
                
        
        
        
        
        
        