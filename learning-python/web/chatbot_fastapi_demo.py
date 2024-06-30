from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import asyncio


app = FastAPI()


async def message_stream():
    for i in range(10):
        yield f"Message {i}\n"
        await asyncio.sleep(1)


async def my_chain():
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(base_url="https://api.deepseek.com", model="deepseek-chat")
    # llm = ChatOpenAI(base_url='https://dashscope.aliyuncs.com/compatible-mode/v1', model='qwen-max')
    async for chunk in llm.astream("介绍一下 HTTP"):
        # print(chunk.content, end="|", flush=True)
        yield chunk.content


@app.get("/stream")
async def stream(request: Request):
    return StreamingResponse(my_chain(), media_type="text/plain")

# if __name__ == '__main__':
#     asyncio.run(my_chain())
