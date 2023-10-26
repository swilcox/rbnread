# rbnread

## Overview

This is a telnet client and [Reverse Beacon Network](https://reversebeacon.net) parser. It connects to a reverse beacon telnet server and parses incoming data in real-time.

Valid RBN spots are then sent via HTTP POST requests to a special RBN API server (see other project) where the spots are stored in a database.

### Other uses

This client could be modified to send/stream the spots to other services like Kafka or any other pubsub/event bus or data stream service or the records could be directly written to a database.

## Instructions

This project uses `pdm` for python virtualenv and requirements management.

`git clone` the repository to a directory.

`pdm install` to install dependencies.

`pdm run pytest` to run tests.

`pdm run client <call_sign>` where `call_sign` is a valid ham radio call sign. **NOTE:** Be sure you've got the API server up and running first.


