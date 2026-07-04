import requests
import json
import os

# connect with ollama model
def chat_with_ollama(message: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",
        "prompt": f"{message}",
        "stream": True
    }

    output = ""

    with requests.post(url, json=payload, stream= True) as res:
        for line in res.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                
                output += data.get("response", "")
    return output

# connect with lmstudio model

def chat_with_lmstudio(message: str) -> str:
    response = requests.post(
    "http://localhost:1234/api/v1/chat",
    headers={
        "Content-Type": "application/json"
    },
    json={
        "model": "essentialai/rnj-1",
        "input": f"{message}"
    }
    )

    data = response.json()
    return data["output"][0]["content"]



# make a new file in this folder and name should be coming from model
def get_file_name(problem: str):
    prompt = f"give me the good name of a coding python file for {problem} and respond only with a proper file name, nothing else, just the file name with just name and file_name.py example return just: example.py, dont include ``` or anything else just the name of the file and .py extension. example: example.py or example.js or whichever language the user asked for"

    file_name = chat_with_lmstudio(prompt)
    print(file_name)
    return file_name


def clean_up_extra_parts_of_code(res):
    res = res.replace("```python", "")
    res = res.replace("```", "")
    
    return res
# let model input its content in this for python and then lets run it

def create_code(problem: str):
    prompt = f"Create a full code with best implementation in python on the problem {problem}, this code should be well organized and properly written, just respond with code lines only absolutely nothing else "
    
    res =  chat_with_lmstudio(prompt)
    res = clean_up_extra_parts_of_code(res)
    return res



def create_file_add_code(file_name, code):
    with open(f"examples/{file_name}", "w") as f:
        f.write(code)


if __name__ == "__main__":
    problem = input("What is a simple problem that we can solve in py \n")
    file_name = get_file_name(problem)
    code = create_code(problem)

    create_file_add_code(file_name, code)
