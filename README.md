# Djangogirls Tutorial

## requirements

- Python 3.6

## 프로젝트 구조

```
projects/
	django/ # Django project들
		djangogirls_project/ # Django project folder
			.git
			.gitignore
			  Django, Python, Linux, macOS,
			  PyCharm
			  # Custom
			  .idea/
			.python-version (pyenv local)
			requirements.txt

			djangogirls/ # Django application folder
				manage.py
				djangogirls/ # Django settings folder
					__init__.py
					settings.py
					urls.py
					wsgi.py
```

## 새 프로젝트 구성
1. djangogirls폴더 생성
2. git init
3. gitignore작성
 3-1. gitignore내부에 .idea/ 추가
4. pyenv virtualenv fc-djangogirls생성
5. pyenv local로 적용할 가상환경 설정
6. GitHub에 Djangogirls저장소 추가
7. 로컬 git에 GitHub remote저장소 추가
8. PyCharm으로 해당 프로젝트 폴더 open후 interpreter설정
  macOS: /usr/local/var/pyenv/versions/
  Linux: $HOME/.pyenv/versions
