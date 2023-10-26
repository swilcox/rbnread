import argparse
import asyncio

from .rbn_decoder import decode_rbn_message

# adapted from
# https://www.geeksforgeeks.org/how-to-create-telnet-client-with-asyncio-in-python/


async def rbn_telnet_client(
    host: str, port: int, username: str, password: str = ""
) -> None:
    reader, writer = await asyncio.open_connection(host, port)
    print(f"connected to ({host}, {port})")

    # Login to the server, if the server requires authentication

    writer.write(f"{username}\n".encode())
    if password:
        writer.write(f"{password}\n".encode())

    while True:
        data = await reader.readuntil(separator=b"\n")
        print(data.decode().strip())
        rbn_record = decode_rbn_message(data)
        print(rbn_record)


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
        default="http://locahlost:8000/api/spots/",
    )
    args = parser.parse_args()
    asyncio.run(rbn_telnet_client(args.rbn_server, args.rbn_port, args.call_sign))


if __name__ == "__main__":
    main()
