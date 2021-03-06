#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import requests
from mfrc522 import SimpleMFRC522

BASE_URL_HARDWARE = "http://threetiersystem.local:5000/api/v1"
BASE_URL_MAIN = "http://threetiersystem.local:8000/api"

reader = SimpleMFRC522()


def open_door(pin_number: int, employee_id: str):
    try:
        requests.post(
            f'{BASE_URL_HARDWARE}/turn-on', json={'number': pin_number})
        print("Door open!!!")
        requests.post(
            f'{BASE_URL_HARDWARE}/write-to-lcd', json={'text': "Door open..."})
        time.sleep(5)
        requests.post(
            f'{BASE_URL_HARDWARE}/turn-off', json={'number': pin_number})
        print("Door closed.")
        requests.post(
            f'{BASE_URL_HARDWARE}/write-to-lcd', json={'text': "Door closed..."})
        requests.post(
            f'{BASE_URL_MAIN}/access/', json={'employee': employee_id, "direction": "in", "status": True})
        requests.post(
            f'{BASE_URL_HARDWARE}/write-to-lcd', json={'text': ""})
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.Timeout:
        print('The request timed out')
    except Exception as err:
        print(f'Other error occurred: {err}')


def main():
    try:
        print("----------------")
        print("Authenticating card...")
        print("----------------")
        requests.post(
            f'{BASE_URL_HARDWARE}/write-to-lcd', json={'text': "Place card..."})
        id, text = reader.read()
        employee_id = text.strip()
        employee_response = requests.get(
            f'{BASE_URL_MAIN}/rfid/?employee__id={employee_id}')
        results = employee_response.json()
        if results:
            current_employee = results[0]["employee"]
            first_name = current_employee["first_name"]
            last_name = current_employee["last_name"]
            print(
                f"successfully authenticated user: {first_name} {last_name}")
            open_door(36, employee_id)
        else:
            print(
                f"No employee found with the given id: {employee_id}")
    except Exception as err:
        print(f'Other error occurred: {err}')
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
