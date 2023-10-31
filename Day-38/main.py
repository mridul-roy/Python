import requests


APP_ID = "10ac5a93"
API_KEY = "9044e2bc3dfd03f0c0dc9514a0c4b761"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header ={
 "x-app-id": APP_ID,
 "x-app-key": API_KEY,
 "Content-Type": "application/json"
}

exercise_text = input("Tell me which exercises you did: ")

params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 49,
    "height_cm": 67,
    "age": 24,

}

exercise_response = requests.post(url=exercise_endpoint, json=params, headers=header)

result = exercise_response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/e4898d8c59080f2ca2ba33459ae28546/workoutTracking/workouts"