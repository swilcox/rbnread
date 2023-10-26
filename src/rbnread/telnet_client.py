import argparse
import asyncio
import aiohttp

from .rbn_decoder import decode_rbn_message
from .models import RBNRecord

# adapted from
# https://www.geeksforgeeks.org/how-to-create-telnet-client-with-asyncio-in-python/


async def send_to_api_server(session, url, rbn_record: RBNRecord):
    async with session.post(url, json=rbn_record.jsonify()) as response:
        json_data = await response.json()
        return (response.status, json_data)


async def rbn_telnet_client(
    *,
    host: str,
    port: int,
    username: str,
    password: str = "",
    api_server_url="",
) -> None:
    # api_server_session = aiohttp.ClientSession()
    reader, writer = await asyncio.open_connection(host, port)
    print(f"connected to ({host}, {port})")

    # Login to the server, if the server requires authentication

    writer.write(f"{username}\n".encode())
    if password:
        writer.write(f"{password}\n".encode())

    async with aiohttp.ClientSession() as api_server_session:
        while True:
            data = await reader.readuntil(separator=b"\n")
            print(data.decode().strip())
            rbn_record = decode_rbn_message(data)
            if rbn_record:
                status, json_response = await send_to_api_server(
                    api_server_session, api_server_url, rbn_record
                )
                print(status, json_response)


def main():
    parser = argparse.ArgumentParser(
        "RBN Reader Client",
        description="for connecting to RBN and calling our custom RBN Server API",
    )
    parser.add_argument("call_sign")
    parser.add_argument(
        "--rbn_server", "-r", help="RBN Server name", default="telnet.reversebeacon.net"
    )
    parser.add_argument(
        "--rbn_port", "-p", help="RBN Server Port to connect to", default=7000, type=int
    )
    parser.add_argument(
        "--api_server_url",
        "-a",
        help="API Server URL",
        default="http://localhost:8000/api/spots/",
    )
    args = parser.parse_args()
    asyncio.run(
        rbn_telnet_client(
            host=args.rbn_server,
            port=args.rbn_port,
            username=args.call_sign,
            api_server_url=args.api_server_url,
        )
    )


if __name__ == "__main__":
    main()
