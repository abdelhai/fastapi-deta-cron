from fastapi import FastAPI
from bitcoin import realtime_price
from deta import App


app = App(FastAPI())


@app.lib.run()
@app.lib.cron()
@app.get("/")
def price(e = None):
    return realtime_price()
