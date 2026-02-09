import asyncio

async def do_some_process() -> str :   ## nevük coroutine
    # do some work
    print("Start!")
    await asyncio.sleep(10)
    return "done!"




async def main():
    result = await do_some_process()
    print(result)
##    ha többet is összevárunk
##    result = await asyncio.gather(do_some_process(), other_some_process(), ...)

# Run the event loop
asyncio.run(main())


