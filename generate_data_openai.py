# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:47:28 2023

@author: dindraatmadja
"""

from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)


prompt = """
Create a table with the following fields:
    - Destination: name of the travel destination in the format City, Country
    - Longitude: longitude of the destination
    - Latitude: latitude of the destination
    
Generate 1 row in this table.
"""

system_prompt="""
Do not include ---|---|--- in the output
Never include any other text than the CSV data.
Any monetary values should be calculated and listed as CAD (without explicitly denoting the currency).
This is not a research and data gathering task; we are looking for roughly accurate estimates based on the data you are trained on.
Always construct datasets in CSV table format with vertical bar | delimiter that can be easily read as a pandas DataFrame.


"""

prompt0 ="""
Do not include ---|---|--- in the output
Never include any other text than the CSV data.
Any monetary values should be calculated and listed as CAD (without explicitly denoting the currency).

"""

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt0 + prompt}
  ]
)

with open('output_data.txt', 'wb') as f:
    f.write(completion.choices[0].message.content.replace('"', '').encode("utf-8"))
