# django-api

- Django restframework Web Api for taking land listing.

## Features
- Register,Login, and Logout a user
- Get all list of registered user
- Get all list of land owners and also be able to perform CRUD on land owners
- Get all list of land information and also perform CRUD on land information

## Requirements

- Python3.8.10
- Djanog 4.1
- Django restframework

## Set up and Installation
- Clone the repository
```bash
git clone https://github.com/Michael-Otieno/django-api/
```
 - Create and activate virtual environment
 ```bash
 python3 -m venv .venv - source .venv/bin/activate  
 ```
 - Install dependencies
  ```bash
pip install -r requirements.txt 
 ```
 - Run project
  ```bash
python3 manage.py runserver
 ```
 ## Structure
 | Endpoint | HTTP Method   | CRUD Method  | Result |
| :---:   | :---: | :---: |:---: |
| `register/` | POST   | CREATE  |Register a user |
| `login/` | POST  | POST |Login a user |
| `user/` | GET  | GET  |Get all users  |
| `logout/` | POST   | POST  |Update atendance detail  |
| `land-owner-information/` | GET  | GET |GET land owners information |
| `land-owner-information/` | POST  | CREATE |Create land owners information |
| `land-owner-information/:id` | GET | GET |Get land owner information |
| `land-owner-information/:id` | PUT | UPDATE |Update land owner information |
| `land-owner-information/:id` | DELETE  | DELETE |Delete land owner information |
| `land-detail/` | GET | GET |Get land details information |
| `land-detail/` | POST | POST |Post land details information |
| `land-detail/:id` | GET | GET |Get land details information |
| `land-detail/:id` | PUT | UPDATE |Update land details information |
| `land-detail/:id` | DELETE |DELETE |Delete land details information |



## Use
- We can use [Postman](https://www.postman.com/) or `curl -i -H ` for testing the Rest Api
 

## Known Bugs

## Contact Information
- If you have any question or contributions, please email me at m.otieno205@gmail.com

## License
- Copyright (c) 2022 Michael-Otieno

