proxima_dir := proxima/
html_dir := html/
css_dir := css/

prox_files := $(shell find $(proxima_dir) -type f -name '*.prox')
html_files := $(patsubst $(proxima_dir)%.prox, $(html_dir)%.html, $(prox_files))

all: $(html_files)
	@tailwindcss -i $(css_dir)input.css -o $(css_dir)output.css
	@proxima make $(proxima_dir)index_gh.prox -o index.html
	@go run app.go

$(html_dir)%.html: $(proxima_dir)%.prox
	@mkdir -p $(dir $@)
	@proxima make $< -o $@

clean:
	rm -rf $(html_dir)/*

.PHONY: all clean
