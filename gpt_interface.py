import openai   
openai.api_key = open('api_key.txt').readline().strip()

model_tier = [
    "gpt-3.5-turbo",
    "gpt-4-1106-preview"
]

def consult_ai(messages, model=model_tier[0]):
    chat = openai.ChatCompletion.create( 
        model=model, messages=messages 
    )
        
    reply = chat.choices[0].message.content 
    return {"role": "assistant", "content": reply}


def print_messages(messages):
    for message in messages:
        if message['role'] == 'user':
            print("user: " + message['content'])
        if message['role'] == 'assistant':
            print("ai: " + message['content'])
