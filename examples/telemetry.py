#!/usr/bin/env python3

import asyncio
from mavsdk import System
import sys

async def run():
    # Init the drone
    drone = System()
    await drone.start()

    succeed = await drone.core.add_new_connection("udp://:14551")
    print("first connection: ", succeed)
    asyncio.ensure_future(print_in_air(drone, 1))
    asyncio.ensure_future(print_position(drone, 1))

    succeed = await drone.core.add_new_connection("udp://:14552")
    print("second connection: ", succeed)
    asyncio.ensure_future(print_in_air(drone, 2))
    asyncio.ensure_future(print_position(drone, 2))

    await drone.action.arm(1)
    await drone.action.takeoff(1)
    await asyncio.sleep(10)
    await drone.action.land(1)

    await drone.action.arm(2)
    await drone.action.takeoff(2)
    await asyncio.sleep(5)
    await drone.action.land(2)

    while True:
        await asyncio.sleep(1)

async def print_in_air(drone, id):
    async for in_air in drone.telemetry.in_air(id):
        print(id, " : ", f"In air: {in_air}")


async def print_position(drone, id):
    async for position in drone.telemetry.position(id):
        print(id, " : ", position)


if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
