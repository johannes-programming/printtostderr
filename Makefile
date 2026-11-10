.ONESHELL:
.PHONY: all beautiful black build clean commit echo isort jacobus py311 py312 py313 py314 py315 pypi rebase test toml_sorted_pyproject upload version
SHELL := /bin/zsh

all: beautiful commit

beautiful: isort black jacobus toml_sorted_pyproject

black: py311
	conda run -n py311 pip install 'black>=24.5,<26';
	conda run -n py311 black --line-length=79 . ;

build: py311
	conda run -n py311 pip install 'build>=1.3,<2';
	conda run -n py311 python -m build;

commit: py311
	git add -A;
	conda run -n py311 pip install 'toml_get>=1.0,<2';
	git commit --allow-empty "$$(conda run -n py311 python -m toml_get @make/toml_get.txt)";

clean:
	rm -fr 'dist/';

echo:
	echo $(PARAMS);

isort: py311
	conda run -n py311 pip install 'isort>=6.0,<7';
	conda run -n py311 isort . ;

jacobus: py311
	conda run -n py311 pip install 'jacobus>=2.0,<3';
	conda run -n py311 python -m jacobus @make/jacobus.txt;

py311:
	conda run -n base python make/env.py py311 --python=3.11;

py312:
	conda run -n base python make/env.py py312 --python=3.12;

py313:
	conda run -n base python make/env.py py313 --python=3.13;

py314:
	conda run -n base python make/env.py py314 --python=3.14;

py315:
	conda run -n base python make/env.py py315 --python=3.15;

pypi: clean build upload

rebase:
	git rebase --empty=drop --interactive $(PARAMS);

reset:
	git reset HEAD~1;

test:
	@conda env remove -y -n test311 2>/dev/null || true;
	conda create -y -n test311 python=3.11;
	conda run -n test311 pip install -e .;
	conda run -n test311 python -c 'import printtostderr.tests; printtostderr.tests.test()';
	conda run -n test311 pip install mypy;
	conda run -n test311 python -m mypy -p printtostderr;

toml_sorted_pyproject: py311
	conda run -n py311 pip install 'toml_sorted>=2.0,<3';
	conda run -n py311 python -m toml_sorted @make/toml_sorted_pyproject.txt;

upload: py311
	conda run -n py311 pip install 'twine>=5.2,<7';
	conda run -n py311 twine upload 'dist/*';

version: all pypi
