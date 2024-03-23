from functions import Aifunctions
webiste_Name="facebook"
Ai_response_text = Aifunctions.promtgen(f"Your are an assistant , you're asked to genrate link for {webiste_Name} , genrate the link only",stop_sequences_prompt=None)
print(Ai_response_text)