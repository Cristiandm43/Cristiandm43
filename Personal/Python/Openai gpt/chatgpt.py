import openai

openai.api_key = "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"

while True:
    
    prompt = input("\nintroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine ="text-davinci-003",
                        prompt = prompt,
                        max_tokens = 2048)
    print(completion.choices[0].text)
