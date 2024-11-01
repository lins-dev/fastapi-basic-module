import asyncio

async def sum(n1: int, n2: int) -> int:
    return n1+n2

async def printAsyncSum(n1: int, n2: int) -> None:
    res = await sum(n1, n2)
    print(f"The result is {res}")