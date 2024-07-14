prePrompt="""this is resume data
<delimeter>"""


postPrompt="""
<delimeter>
stirctly use the below json data and fill the resume details give only valid JSON format same as the provided
strictly do not change any JSON key name use the same key name provided in the JSON formatting 
if information is not present make the json value null, use 2 short sentences for description
JSON format starts after delimeter
<delimeter> 
{
  "personalInfo":
  {
    "name": "",
    "phoneNumber": "",
    "gitHub":"",
    "email": "",
    "dob": "",
    "address":
    {
      "city": "",
      "state": "",
      "pinCode": "",
      "country": ""
    }
  },
  "education":
  {
    "Secondary":
    {
      "institution":
      {
        "name": "",
        "address":
    {
      "city": "",
      "state": "",
      "pinCode": "",
      "country": ""
    }
      },
      "board": "",
      "marks": "",
      "duration":"",
      "start":"",
      "end":""
    },
    "PU":
    {
      "institution":
      {
        "name": "",
        "address":
    {
      "city": "",
      "state": "",
      "pinCode": "",
      "country": ""
    }
      },
      "board": "",
      "marks": "",
      "duration":"",
      "start":"",
      "end":""
    },
    "UG":
    {
      "institution":
      {
        "name": "",
        "address":
    {
      "city": "",
      "state": "",
      "pinCode": "",
      "country": ""
    }
      },
      "board": "",
      "marks": "",
      "duration":"",
      "start":"",
      "end":""
    },
    "PG":
    {
      "institution":
      {
        "name": "",
        "address":
    {
      "city": "",
      "state": "",
      "pinCode": "",
      "country": ""
    }
      },
      "board": "",
      "marks": "",
      "duration":"",
      "start":"",
      "end":""
    }
  },
  "projects":
  [
    {
      "name": "",
      "description": "",
      "technologies":
      [
        "",
        "",
        ""
      ],
      "link": ""
    }
  ],
  "certifications":
  [
    {
      "name":"",
      "verificationLink":""
    }
  ],
  "experience":
  [
    {
      "company":"",
      "role":"",
      "project":
      {
        "name": "",
        "description": "",
        "technologies":
        [
          "",
          "",
          ""
        ],
        "link": ""
      },
      "duration":"",
      "start":"",
      "end":""
    }
  ],
  "codingPlatformLinks":
  {
    "leetCode":"",
    "hackerRank":"",
    "hackerEarth":"",
    "codeChef":"",
    "codeForces":"",
    "gfg":""
  },
  "skills":["","",""]
}
<delimeter>

this is the model and  determine which is compulsory and make it None if not present in the resume
class Address(BaseModel):
    city: str
    state: str
    pinCode: Optional[str]
    country: Optional[str]


class Institution(BaseModel):
    name: str
    address: Optional[Address] = None or str


class EducationLevel(BaseModel):
    institution: Institution = None  
    board: Optional[str] = None   
    marks: str = None  
    duration: str
    start: str
    end: str


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str]
    link: Optional[str] = None  


class Certification(BaseModel):
    name: str
    verificationLink: Optional[str]


class Experience(BaseModel):
    company: str   
    role: str = None  
    project: Optional[Project]
    duration: str = None  
    start: str = None  
    end: str = None  


class CodingPlatformLinks(BaseModel):
    leetCode: Optional[str]
    hackerRank: Optional[str]
    hackerEarth: Optional[str]
    codeChef: Optional[str]
    codeForces: Optional[str]
    gfg: Optional[str]


class PersonalInfo(BaseModel):
    name: str
    phoneNumber: str
    gitHub: str
    email: EmailStr
    dob: Optional[str] = None  
    address: Optional[Address] = None  


class OrganizationInfo(BaseModel):
    name: str
    id:int

class InstitutionInfo(BaseModel):
    name: str
    id:int

output JSON should start with a delimeter like <delJSON> and after the JSON ends it should end with end delimeter like </delJSON> """