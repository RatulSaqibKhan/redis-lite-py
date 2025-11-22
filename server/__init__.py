"""
server package

This package contains all networking-related components for the project.
Currently it includes a minimal TCP server that mimics Redis-style command
handling (e.g., responding to PING with PONG).

Modules:
    tcp_server.py - Implements the TCPServer class.

Usage:
    from server import TCPServer
"""

from .tcp_server import TCPServer

__all__ = ["TCPServer"]
