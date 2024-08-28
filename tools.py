import typer
from reqs import AsyicXSearcher

app = typer.Typer()

@app.command()
def chat_response(message: str):
    url = "https://akeno.randydev.my.id/ryuzaki/chatgpt-old"
    params = {"query": message}
    check_response = await AsyicXSearcher.search(
        url,
        post=True,
        re_json=True,
        json=params
    )
    print(check_response["randydev"]["message"])

if __name__ == "__main__":
    app()
