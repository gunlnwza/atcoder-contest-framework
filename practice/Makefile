all: test

OPT := --maxfail=1
test:
	@clear
	@echo '[ submission.py ]'
	@PYTHONPATH=. pytest test_submission.py --quiet $(OPT)


TEMPLATE_DIR := ../framework/template
KEEP_FILES := Makefile __init__.py test_submission.py

SUBMISSION_FILES := submission.py
SCRIPT_FILES := script.py
EMPTY_FILES := 1 2 3
clean:
	@find . -maxdepth 1 -type f $(foreach f,$(KEEP_FILES), ! -name '$(f)') -exec rm {} +

	@for f in $(SUBMISSION_FILES); do cp $(TEMPLATE_DIR)/template_submission.py $$f; done
	@for f in $(SCRIPT_FILES); do cp $(TEMPLATE_DIR)/template_script.py $$f; done
	@touch $(EMPTY_FILES)

	@echo 'Practice directory cleaned'

fclean: clean


.PHONY: all test clean fclean
