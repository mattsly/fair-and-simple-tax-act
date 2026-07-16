.PHONY: serve
serve:
	bundle exec jekyll serve

.PHONY: build
build:
	bundle exec jekyll build

.PHONY: clean
clean:
	bundle exec jekyll clean

# Usage: make substack ESSAY=lifetime-gains-essay.md
.PHONY: substack
substack:
	python3 internal/scripts/substack_export.py $(ESSAY)

# Which published essays have drifted from their Substack copies?
.PHONY: substack-status
substack-status:
	python3 internal/scripts/substack_export.py --status
