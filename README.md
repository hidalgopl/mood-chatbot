# Requirements to run a project:
1. virtualenv


# How to run a project locally
1. If you are running project for the first time type `./build_venv.sh`
2. Then `./run_locally.sh`
3. Bot local webhook is available on http://127.0.0.1:8000

To test bot locally, I recommend using ngrok. 
After runing `./run_locally.sh` type `ngrok http 8000` and change webhook settings in Facebook Developer panel.
