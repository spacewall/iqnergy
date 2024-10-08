import asyncio
import os

import pytest

from upscaler import upscale
from main import ProcessController

@pytest.fixture
def tasks_gen():
    tasks = [(upscale, (f"raw_images/{path}", f"upscaled_images/{path}", "EDSR_x2.pb")) for path in os.listdir("raw_images")]

    yield tasks

def test_three_picture(tasks_gen):
    controller = ProcessController()
    controller.set_max_proc(3)

    controller.wait()
    asyncio.run(controller.start(list(tasks_gen), 10))

    assert tasks_gen[1][1] in os.listdir("upscaled_images")
