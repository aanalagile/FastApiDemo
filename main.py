from typing import Union

from fastapi import FastAPI

app = FastAPI()

def Fibonacci(n):

	if n < 0:
		print("Incorrect input")

	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fibo/{length}")
def get_fibonacci(length:int):
    value = Fibonacci(length)
    return {"Fibonacci Value is":value}
