class ResumeValidator:
    def __init__(self,resume):
        import json
        print(resume)
        self.resume = json.loads(json.dumps(resume))
        self.invalid = ["None","null","",None]
        self.sampleEdu = {'institution': {'name': None, 'address': {'city': None, 'state': None, 'pinCode': None, 'country': None}}, 'board': None, 'marks': None, 'duration': None, 'start': None, 'end': None}

    def _personalInfo(self):
        if self.resume['personalInfo']:
            try:
                if self.resume['personalInfo']['name'] in self.invalid:
                    self.resume['personalInfo']['name'] = None
            except Exception as e :
                    print(e)
                    self.reusme['personalInfo']['name'] = None
            try:

                if self.resume['personalInfo']['phoneNumber'] in self.invalid:
                    self.resume['personalInfo']['phoneNumber'] = None
            except Exception as e :
                    print(e)
                    self.resume['personalInfo']['phoneNumber'] = None

            try:
                if type(self.resume['personalInfo']['github'])==str:
                    self.resume['personalInfo']['github'] = self.resume['personalInfo']['github'].replace(" ",'')

                if self.resume['personalInfo']['github'] in self.invalid:
                    self.resume['personalInfo']['github'] = None
            except Exception as e :
                    print(e)
                    self.resume['personalInfo']['github'] = None

            try:
                if type(self.resume['personalInfo']['email'])==str:
                    self.resume['personalInfo']['email'] = self.resume['personalInfo']['email'].replace(" ",'')

                if self.resume['personalInfo']['email'] in self.invalid:
                    self.resume['personalInfo']['email'] = None
            except Exception as e:
                 print(e)
                 self.resume['personalInfo']['email'] = None

        else:
             self.resume['personalInfo'] = None
        return self.resume
             

    def _education(self):
        if self.resume['education']:
             for edu in self.resume['education']:
                print(edu)
                try:
                    if self.resume['education'][edu] in self.invalid:
                        self.resume['education'][edu] = self.sampleEdu
                    else:
                        try:
                            if self.resume['education'][edu]['institution']in self.invalid:
                                self.resume['education'][edu] = self.sampleEdu
                            else:
                                insti = self._institution(self.resume['education'][edu]['institution'])
                                self.resume['education'][edu]['institution'] = insti
                        except:
                            self.resume['education'][edu] = self.sampleEdu

                        if self.resume['education'][edu]['institution'] in self.invalid:
                            self.resume['education'][edu] = self.sampleEdu
                        else:
                            try:
                                if self.resume['education'][edu]['marks'] in self.invalid:
                                    self.resume['education'][edu]['marks'] = str(0)
                                else:
                                    self.resume['education'][edu]['marks'] = self._parseMarks(self.resume['education'][edu]['marks'])    
                            except:
                                self.resume['education'][edu]['marks'] = '0'
                        
                except Exception as e:
                    print(e)
                    self.resume['education'][edu] = self.sampleEdu 
        else:
            self.resume['education'] = []
    
    def _parseMarks(self,pmarks):
        marks = ''
        for i in pmarks:
            if i.isnumeric() or i=='.':
                marks += i
            continue
        if float(marks)<=10:
            marks = 10*float(marks)
        elif float(marks)<=5:
            marks = (float(marks)/5)*100
        return str(float(marks))

    def _projects(self):
        try:
            if self.resume['projects']:
                projects = []
                for project in self.resume['projects']:
                    if project:
                        try:
                            if project['name']in self.invalid:
                                project['name']==None
                        except Exception as e:
                            print(e)
                            project['name'] == None

                        try:
                            if project['description']in self.invalid:
                                project['description']=None
                        except Exception as e:
                            print(e)
                            project['description']=None

                        try:
                            if project['technologies']:
                                if len(project['technologies'])<=0:
                                    project['technologies'] = []
                        except Exception as e:
                            print(e)
                            project['technologies'] = []
                        projects.append(project)

                self.resume['projects'] = projects
            else:
                self.resume['projects'] = None
        except Exception as e:
            print(e)
            self.resume['projects'] = None


    def _certifications(self):
        try:
            if self.resume['certifications']:
                certifications = []
                for cert in self.resume['certification']:
                    try:
                        if cert['name'] in self.invalid:
                            cert['name'] = None 
                    except Exception as e:
                        print(e)
                        cert['name'] = None
                    
                    try:
                        if cert['verificationLink'] in self.invalid:
                            cert['verificationLink'] = None
                    except Exception as e:
                        print(e)
                        cert['verificationLink'] = None
                    certifications.append(cert)
                self.resume['certifications'] = certifications
            else:
                self.resume['certifications'] = None
        except Exception as e:
            print(e)
            self.resume['certifications'] = None
            

    def _institution(self,institution):
        try:
             if institution:
                try:
                    if institution['name'] in self.invalid:
                        institution['name'] = None
                except Exception as e:
                    print(e)
                    institution['name'] = None

                try:
                    if institution['address']:
                        address = self._address(institution['address'])
                        institution['address'] = address
                    else:
                        institution['address'] = self._address(None)
                except Exception as e:
                    print(e)
                    institution['address'] = self._address(None)
             else:
                institution = {
                "name":"",
                "address": self._address(None)
                }
        except Exception as e:
            print(e)
            institution = {
            "name":"",
            "address": self._address(None)
            }

        return institution
    
    def _address(self,address):
        try:
            if address:
                try:
                    if address['city'] in self.invalid:
                        address['city'] = None
                except Exception as e:
                    print(e)
                    address['city'] = None

                try:
                    if address['state'] in self.invalid:
                        address['state'] = None
                except Exception as e:
                    print(e)
                    address['state'] = None

                try:
                    if address['pinCode'] in self.invalid:
                        address['pinCode'] = None
                except Exception as e:
                    print(e)
                    address['pinCode'] = None

                try:
                    if address['country'] in self.invalid:
                        address['country'] = None
                except Exception as e:
                    print(e)
                    address['country'] = None
            else:
                address = {
                    "city":None,
                    "state":None,
                    "pinCode":None,
                    "country":None
                    }
        except Exception as e:
            print(e)
            address = {
                "city":None,
                "state":None,
                "pinCode":None,
                "country":None
                }
            
        return address
    
    def _validate(self):
        self._personalInfo()
        self._education()
        self._projects()
        self._certifications()
        print("rgtergergergwehbfwehbfg4etfguj4egnhbdsbdjbdsjbdsfbhrdfgvbrhfgbryhgbvrygbrbgvrbg",self.resume)
        return self.resume
if __name__ == "__main__":
    from pydantic_models.sampleResume import resume_data
    jsum = resume_data
    res = ResumeValidator(jsum)._validate()
    print(res)
    
        
 