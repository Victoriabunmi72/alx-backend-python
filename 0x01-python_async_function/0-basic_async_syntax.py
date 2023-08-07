#!/usr/bin/env python3
"""Task 0's module.
   The basic of async.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> that:
    """Wait for a random number of seconds"""

wait_time = random.random() * max_delay
await asyncio.sleep(wait_time)
return wait_time
