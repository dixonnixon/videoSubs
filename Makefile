fmt:
	find . -type f -name "*.py" | xargs black

test:
	python -m unittest discover -s app/tests
# videoSubs app/*.py
# videoSubs app/*/*.py

# coverage:
# 	coverage run -m unittest discover
# 	coverage report


# lint:


# format:
#  black .

# .PHONY: test coverage lint format


# run:
# 	${PYTHON} our_app.py

# clean:
#     rm -r *.project

# help:
