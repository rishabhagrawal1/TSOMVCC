import sys, os
import request
import json

class Obj:
    def __init__(self, id, type):
        self.id = id
        self.type = type

##Object of attribute versions to be used in latestVersion and latestVersionBefore
class StaticAnalysis:
    def __init__(self, attr_file, coord_list):
        self.attr_file = attr_file  
        self.attr_data = None
        self.coord_list = coord_list
        self.loadAttrFileObj()
    
    def calculateHash(self, id):
        count = 0
        for i in id:
            count += ord(i)
        return count
        
    def loadAttrFileObj(self):  
        try:
            if(os.path.exists(self.attr_file)):
                with open(self.attr_file, encoding='utf-8') as attrs:
                    self.attr_data = json.loads(attrs.read())
        except:
            print("Error in reading Attribute file")

    def mightWriteObj(self, req):
        req_attr = []
        for req_prop in self.attr_data['request_properties']:
            if(list(req_prop.keys())[0] == req.req_type):
                req_attr = list(req_prop.values())[0]
                break
        result_set = set()
        if(not self.attr_data):
            return result_set
        for element in self.attr_data['attribute_properties']:
            #print(element.keys(), list(element.keys())[0] in req_attr, list(element.values())[0][1]['write'] == 'mutable')
            if(list(element.keys())[0] in req_attr and list(element.values())[0][1]['write'] == 'mutable'):
               result_set.add(list(element.values())[0][2]['obj'])
        #print("result_set is ", result_set)
        return result_set
        
    def defReadAttr(self, x, req):
        req_attr = []
        for req_prop in self.attr_data['request_properties']:
            if(list(req_prop.keys())[0] == req.req_type):
                req_attr = list(req_prop.values())[0]
                break
        result_set = set()
        if(not self.attr_data):
            return result_set
        for element in self.attr_data['attribute_properties']:
            if(list(element.keys())[0] in req_attr and list(element.values())[0][2]['obj'] == x.type and list(element.values())[0][0]['read'] == 'def'):
               result_set.add(list(element.keys())[0])
        return result_set
    
    def mightReadAttr(self, x, req):
        req_attr = []
        for req_prop in self.attr_data['request_properties']:
            if(list(req_prop.keys())[0] == req.req_type):
                req_attr = list(req_prop.values())[0]
                break
        #print(req_attr, x.type)
        result_set = set()
        if(not self.attr_data):
            return result_set

        for element in self.attr_data['attribute_properties']:
            #print(element.keys(), list(element.keys())[0] in req_attr, list(element.values())[0][2]['obj'], list(element.values())[0][0]['read'])
            if(list(element.keys())[0] in req_attr and list(element.values())[0][2]['obj'] == x.type and list(element.values())[0][0]['read'] == 'might'):
                result_set.add(list(element.keys())[0])
        return result_set
        
    def mightWriteAttr(self, x, req):
        req_attr = []
        for req_prop in self.attr_data['request_properties']:
            if(list(req_prop.keys())[0] == req.req_type):
                req_attr = list(req_prop.values())[0]
                break
        print("mightWriteAttr xtype reqid", x.type, req.id)
        result_set = set()
        if(not self.attr_data):
            return result_set
        for element in self.attr_data['attribute_properties']:
            if(list(element.keys())[0] in req_attr and list(element.values())[0][2]['obj'] == x.type and list(element.values())[0][1]['write'] == 'mutable'):
                result_set.add(list(element.keys())[0])
        print("mightWriteAttr result_set", result_set)
        return result_set
        
    def obj(self, req, i):
        result = 'sub'
        result_set = self.mightWriteObj(req)
        if(len(result_set) == 1):
            if(next(iter(result_set)) == 'sub' and i == 1):
                result = 'res'
            elif(next(iter(result_set)) == 'res' and i == 2):
                result = 'res'
        else:
            if(i == 2):
                result = 'res'
        if (result == 'sub'):
            ob = Obj(req.subj_id, result)
        else:
            ob = Obj(req.res_id, result)
        return ob
        
    def coord(self, obj):
        return self.coord_list[self.calculateHash(obj.id) % len(self.coord_list)]
        
        
        
        
        
        
