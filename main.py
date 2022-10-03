from typing import Union

from fastapi import FastAPI
import socket

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
	ip_address=socket.gethostbyname(socket.gethostname())
	return {"Hello": f"Ip address is {ip_address}"}


@app.get("/fibo/{length}")
def get_fibonacci(length:int):
	value = Fibonacci(length)
	ip_address=socket.gethostbyname(socket.gethostname())
	return {f"From instance with IP: {ip_address},Fibonacci Value is":value}
