import asyncio
import openai
import backoff

client = openai.AsyncOpenAI(api_key='OpenAI_API_key')

@backoff.on_exception(backoff.expo, openai.RateLimitError)
async def make_api_call_to_gpt(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    
    return response.choices[0].message.content

async def main():
    prompts = ["Hello, ChatGPT!", "How does async programming work?"]

    # Create a list to store the results of asynchronous calls
    results = []

    # Asynchronously call the function for each prompt
    tasks = [make_api_call_to_gpt(prompt) for prompt in prompts]
    print(tasks)
    results = await asyncio.gather(*tasks)
    print(results)
    

asyncio.run(main())
