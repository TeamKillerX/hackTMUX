import typer
import asyncio
from reqs import AsyicXSearcher

app = typer.Typer()

@app.command()
def chat(message: str):
    async def _chat():
        url = "https://akeno.randydev.my.id/ryuzaki/chatgpt-old"
        params = {"query": message}
        check_response = await AsyicXSearcher.search(
            url,
            post=True,
            re_json=True,
            json=params
        )
        print(check_response["randydev"]["message"])
    asyncio.run(_chat())

if __name__ == "__main__":
    app()
