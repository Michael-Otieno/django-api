# django-api

- Django restframework Web Api for taking land listing.

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
 ## Structure
 | Endpoint | HTTP Method   | CRUD Method  | Result |
| :---:   | :---: | :---: |:---: |
| `register/` | POST   | CREATE  |Register a user |
| `login/` | POST  | POST |Login a user |
| `user/` | GET  | CREATE  |Get all users  |
| `logout/` | POST   | POST  |Update atendance detail  |
| `attendance/:id` | DELETE  | DELETE |Delete atendance detail  |

## Use
- We can use [Postman](https://www.postman.com/) or `curl -i -H ` for testing the Rest Api
 

## Known Bugs

## Contact Information
- If you have any question or contributions, please email me at m.otieno205@gmail.com

## License
- Copyright (c) 2022 Michael-Otieno

