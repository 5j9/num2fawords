cd ../num2fawords
coverage run test.py
coverage html
read -t5 -n1 -r -p 'Done!' key
