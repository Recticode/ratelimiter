import typer
from limiter import Limiter
from clock import Clock

app = typer.Typer()

limiter = Limiter(N=3, T=10, clock=Clock())

@app.command()
def whatisthis():
    print("this is a ratelimiter")

@app.command()
def allow(user_id: int):
    allowed = limiter.allow(user_id)
    if allowed:
        print("allowed")
    else:
        print("rate limited")

if __name__ == "__main__":
    app()
