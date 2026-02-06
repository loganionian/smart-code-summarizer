import openai

def summarize_function_code(code: str) -> str:
    """Summarizes the given function code."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this function:\n{code}"}]
    )
    return response['choices'][0]['message']['content'].strip()

def summarize_module_code(code: str) -> str:
    """Provides a high-level overview of the module."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Provide an overview of the following code:\n{code}"}]
    )
    return response['choices'][0]['message']['content'].strip()