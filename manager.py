import asyncio


class Manager:
    def __init__(self):
        self.id = "jV7OUwjn4"
        self.queue = []

    async def jqve(self, item):
        await asyncio.sleep(0)
        self.queue.append(item)
        return len(self.queue)


async def main():
    obj = Manager()
    for i in range(5):
        await obj.jqve(i)
    print(obj.queue)


if __name__ == "__main__":
    asyncio.run(main())
