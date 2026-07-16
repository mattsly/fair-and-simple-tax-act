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

# Render an essay to rich text on the clipboard, ready to paste into Substack.
# Usage: make substack-copy ESSAY=lifetime-gains-essay.md
.PHONY: substack-copy
substack-copy:
	python3 internal/scripts/substack_export.py --copy $(ESSAY)

# Which published essays have drifted from their Substack copies?
.PHONY: substack-status
substack-status:
	python3 internal/scripts/substack_export.py --status
