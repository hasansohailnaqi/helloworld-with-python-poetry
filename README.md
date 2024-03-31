first create folder name quater
open folder
open powershell
poetry new helloworld
cd helloworld
code .
in vs code open terminal
poetry add request
poetry run python helloworld\main.py 
test
poetry add pytest     
poetry run pytest  
poetry add pytest -v  
poetry build     (upload file to pypi)
poetry publish  