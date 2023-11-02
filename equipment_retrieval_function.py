from webex_bot.models.command import Command
from webex_bot.models.response import Response
import snowflake.snowpark
import pandas as pd
from snowflake.snowpark import Session
from dotenv import load_dotenv
import os

load_dotenv()

class equipment_info(Command):
    messages=[]
    #messages.append({"role": "system", "content": ""})

    def __init__(self):
        super().__init__()
    
    def execute(self, message, attachment_actions, activity):
    

        #self.messages.append({"role": "user", "content": message})
        #self.messages.append({"role": "assistant", "content": message})
        
        connection_parameters = {
  "account": os.getenv("SNOWFLAKE_ACCOUNT"),
  "user": os.getenv("SNOWFLAKE_USERNAME"),
  "password": os.getenv("SNOWFLAKE_PASSWORD"),
  "role": "ANALYST",
  "warehouse": "WH_ADHOC"
            }
        session = Session.builder.configs(connection_parameters).create()
        
        df = session.sql("""select equipment_code,"SIM_ESN#",refresh_date,edf_status,days_in_status,party_name,cat_class_desc,make,model
from DISCOVERY.DLA_A_19591.TBL_TELEMATICS_SUPERSTORE
where equipment_code = (?)""",params=[message])

        results = pd.DataFrame(df.collect())
        text = f"Equipment {results['EQUIPMENT_CODE'].values[0]} status is {results['EDF_STATUS'].values[0]}. It has been in status for {results['DAYS_IN_STATUS'].values[0]} days and was last refreshed {results['REFRESH_DATE'].values[0]}. The equipment is a {results['MAKE'].values[0]},{results['MODEL'].values[0]} which is a {results['CAT_CLASS_DESC'].values[0]}. Last party name is {results['PARTY_NAME'].values[0]}"

        #return(gpt_response)
        return(text)