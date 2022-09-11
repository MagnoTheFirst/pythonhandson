from yaspin import yaspin
import httpx



from random import randint
from yaspin import yaspin

input = input("type in an uri")
r = httpx.get(input)

with yaspin(text="Loading", color="yellow") as spinner:


    success = randint(0, 1)
    if r.status_code == 200:
        spinner.ok("✅ HTTP Status code 200")
    else:
        spinner.fail("💥 Bad Request ")
