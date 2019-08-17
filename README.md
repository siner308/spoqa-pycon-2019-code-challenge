# 0. 요약
아래의 커맨드를 따라 배포가 가능합니다.
`python 3.5` 를 지원하는 virtualenv를 사용하였으며,
`django 2.2` 를 사용하였습니다.

# 1. Install Ubuntu 16.04

# 2. Install PIP
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
# 3. Install Virtualenv
```bash
pip install virtualenv
```
# 4. Create Virtual Environment and Activate
```bash
virtualenv -p python3 venv
source venv/bin/activate
```

# 5. Get Repository
```bash
git clone https://github.com/siner308/spoqa-pycon-2019-code-challenge.git
cd spoqa-pycon-2019-code-challenge
```

# 6. Install Dependencies
```bash
pip install -r requirements.txt
```

# 7. Run Server
```bash
python manage.py runserver 0.0.0.0:8000
```

# 8. FIND PYTHONISTAS in WEB
maybe you can find multiple images in `localhost:8000` (when refresh website, you can get new images)
