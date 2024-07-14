import google.generativeai as genai
from .LLMPrompts import prePrompt,postPrompt
from setup import get_llm_api_key,get_groq_api_key
from groq import Groq
import json

api_key_gemini = get_llm_api_key()




class ResumeParser:
    def __init__(self,resumeText):
        self.resumeText=resumeText

    def Google(self,genModel='gemini-pro'):
        genai.configure(api_key=api_key_gemini)
        model = genai.GenerativeModel(genModel)
        tem=None
        retry_count=0
        while tem is None and retry_count<2:
            try:
                response = model.generate_content(prePrompt+self.resumeText+postPrompt)
                tem=response.text
                tem=tem[tem.find("<delJSON>")+9:tem.rfind('</delJSON>')]
                tem = json.loads(tem)
            except Exception as exc:
                print(exc)
                tem=None
                print("retrying...")
            retry_count+=1
        return tem
    def Groq(self,model='llama3-70b-8192'):
        tem = ""
        retry_count=0
        try:
            client = Groq(api_key=get_groq_api_key())
            print("safe")
            chat_completion = client.chat.completions.create(messages=[{"role": "user","content": prePrompt+self.resumeText+postPrompt,}],model=model,)
            print("trouble")
            tem=chat_completion.choices[0].message.content
            tem=tem[tem.find("<delJSON>")+9:tem.rfind('</delJSON>')]
            print("ulalalalaalalalha")
            print(tem)
            tem = json.loads(tem)
        except Exception as exc:
            print(exc)
            print("error: ",exc)
            print("error file info: ",exc.__traceback__.tb_frame)
            print("error line#: ",exc.__traceback__.tb_lineno)
        retry_count+=1
        return tem
    

if __name__=="__main__":
    resumeText='''

'''
    parser=ResumeParser(resumeText)
    resumeJSON=parser.Gemini()
    print(resumeJSON)