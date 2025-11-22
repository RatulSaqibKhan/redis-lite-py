# TCP Server Module

This module contains a minimal TCP server that imitates the Redis networking behavior.
It listens on port 6379 by default and supports the PING command using the RESP protocol.

## 🚀 Features

- Accepts multiple client connections (thread-based)
- RESP-style replies for supported commands
- Basic command parsing
- Graceful shutdown on Ctrl + C

## 📁 File: tcp_server.py
### Current Supported Commands

<table>
  <thead>
    <tr>
      <th>Command</th>
      <th>Response</th>
    </tr>
  </thead>
  <tbpdy>
    <tr>
      <td>PING</td>
      <td>+PONG\r\n</td>
    </tr>
    <tr>
      <td>Any other</td>
      <td>-ERR Unknown command\r\n</td>
    </tr>
  </tbpdy>
</table>

## 🧑‍💻 Usage
### Run from project root:
```
python3 main.py
```
### Or run server module directly:
```
python3 server/tcp_server.py
```

## 📡 Connecting via Client
- Using `telnet`:
    ```
    telnet localhost 6379
    PING
    ```
- Output:
    ```
    +PONG
    ```
## 🧭 Roadmap (for this module)

- Add RESP parser (Array, Bulk Strings, Integers, Errors)
- Switch from threads → asyncio event loop
- Integrate with actual command engine in redis_lite/
- Add logging and connection limits
- Benchmark utilities

## 📝 Notes

This is a minimal learning-oriented TCP implementation.<br>
Full Redis behavior—including persistence, pub/sub, memory model, and eviction—will be implemented later under the redis_lite/ directory.