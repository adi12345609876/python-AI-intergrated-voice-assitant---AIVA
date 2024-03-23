import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
# config
MY_API_GEMINI = os.getenv('API_KEY_GEMINI')
genai.configure(api_key=MY_API_GEMINI)
model = genai.GenerativeModel('gemini-pro')
#function
def promtgen(prompt,stop_sequences_prompt,candidate_count_prompt=1,max_output_tokens_prompt=100,top_p_prompt=0.7,top_k_prompt=4,temperature_prompt=0.7):
  print("Genrating promt....")
  if len(prompt)>0:
    response = model.generate_content(prompt,stream=True,generation_config=genai.types.GenerationConfig(candidate_count=candidate_count_prompt,stop_sequences=stop_sequences_prompt,max_output_tokens=max_output_tokens_prompt,top_p = top_p_prompt,top_k = top_k_prompt,temperature=temperature_prompt))
    try:
      response.resolve()
      # print(response.text)
      return response.text
    except Exception as e:
        print(e)
  else:
    print("NO prompt")    
  