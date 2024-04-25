#!/usr/local/bin/python

import sys
import time
import os
import random
import asyncio
from saq import Queue, Job

NUMBER = 50
pid = os.getpid()


async def func_async(i, d):
    queue = Queue.from_url('redis://localhost')

    job_args = dict(
        timeout=60,
        function='rpc',
        scheduled=0,
        kwargs={'d': d}
    )

    try:
        print(f'Client #{pid} send {i} of {NUMBER} ({d})')
        job = Job(**job_args)
        result = await queue.apply(job, timeout=60)
        print(f'Client #{pid} recv {i} of {NUMBER} ({result})')
        return result
    finally:
        await queue.disconnect()


async def main():
    await asyncio.sleep(random.random() * 0.2)
    print(f'Client #{pid} has started')
    await asyncio.sleep(0.3)

    for i in range(NUMBER):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        r = await func_async(i + 1, dict(id=i, a=a, b=b))
        assert a + b == r['result']
        await asyncio.sleep(0.2)

        if i == 15 and '--stop' in sys.argv:
            print('\n!!! STOP worker pid', r['pid'], '\n')
            os.kill(r['pid'], 19)  # SIGSTOP
            await asyncio.sleep(1)

    print(f'Client #{pid} done')


asyncio.run(main())
