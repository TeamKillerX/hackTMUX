import argparse
import asyncio
from reqs import AsyicXSearcher

async def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('--ask', type=str, help='A question to be asked')

    args = parser.parse_args()
    url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
    params = {"query": args.ask}
    check_response = await AsyicXSearcher.search(
        url,
        post=True,
        re_json=True,
        json=params
    )
    if args.ask:
        return check_response["randydev"]["message"]
    else:
        print("No question was asked.")

if __name__ == "__main__":
    await asyncio.run(main())
