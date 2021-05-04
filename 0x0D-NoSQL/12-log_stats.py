#!/usr/bin/env python3
""" 12-log_stats docstring """
from pymongo import MongoClient


def print_counts(count, methods, checks):
    """ print_counts docstring """
    print(f"{count} logs")
    print("Methods:")
    for method in methods:
        value = methods[method]
        print(f"\tmethod {method}: {value}")
    print(f"{checks} status check")


if __name__ == "__main__":
    client = MongoClient()
    nginx_logs = client.logs.nginx
    count = nginx_logs.count_documents({})
    status = nginx_logs.count_documents({"path": "/status"})
    methods = {
        "GET": nginx_logs.count_documents({"method": "GET"}),
        "POST": nginx_logs.count_documents({"method": "POST"}),
        "PUT": nginx_logs.count_documents({"method": "PUT"}),
        "PATCH": nginx_logs.count_documents({"method": "PATCH"}),
        "DELETE": nginx_logs.count_documents({"method": "DELETE"})
    }

    print_counts(count, methods, status)
