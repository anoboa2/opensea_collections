import asyncio

collection = "zed-run-official"

async def testListen():
    reader, writer = await asyncio.open_connection(host="https://api.opensea.io/wyvern/v1/orders?bundled=false&include_bundled=false&include_invalid=false&limit=20&offset=0&order_by=created_date&order_direction=desc")
