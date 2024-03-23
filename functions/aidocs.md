#props for gemini
Let’s go through each of the parameters below:

- candidate_count=1: Tells the Gemini to generate only one response per Prompt/Query. As discussed before, right now Google limits the number of candidates to 1
- stop_sequences=["."]: Tells Gemini to stop generating text when it encounters a period (.)
- max_output_tokens=20: Limits the generated text to a specified maximum number which here is set to 20
- top_p = 0.7: Influences how likely the next word will be chosen based on its probability. 0.7 favors more probable words, while higher values favor less likely but potentially more creative choices
- top_k = 4: Considers only the top 4 most likely words when selecting the next word, promoting diversity in the output
- temperature=0.7: Controls the randomness of the generated text. A higher temperature (like 0.7) increases randomness and creativity, while lower values favor more predictable and conservative outputs
