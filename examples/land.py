#!/usr/bin/env python3

import asyncio
from mavsdk import System
import sys

async def run():

    drone = System()
    # await drone.connect(system_address="udp://:1455" + sys.argv[1])

    status_text_task = asyncio.ensure_future(print_status_text(drone))


    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state(int(sys.argv[1])):
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health(int(sys.argv[1])):
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Landing")
    await drone.action.land(int(sys.argv[1]))



async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text(int(sys.argv[1])):
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
