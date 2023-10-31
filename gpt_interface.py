import openai   
openai.api_key = open('api_key.txt').readline().strip()

def consult_ai(messages):
    chat = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", messages=messages
        #model="gpt-4", messages=messages 
    )
        
    reply = chat.choices[0].message.content 
    return {"role": "assistant", "content": reply}


def print_messages(messages):
    for message in messages:
        if message['role'] == 'user':
            print("user: " + message['content'])
        if message['role'] == 'assistant':
            print("ai: " + message['content'])
