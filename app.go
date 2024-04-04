package main

import (
	"embed"
	"io/fs"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

//go:embed html/*
var htmlFiles embed.FS

//go:embed css/* js/* assets/*
var staticFiles embed.FS


func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    cssFS, _ := fs.Sub(staticFiles, "css")
    jsFS, _ := fs.Sub(staticFiles, "js")
    assetsFS, _ := fs.Sub(staticFiles, "assets")

    http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.FS(cssFS))))
    http.Handle("/js/", http.StripPrefix("/js/", http.FileServer(http.FS(jsFS))))
    http.Handle("/assets/", http.StripPrefix("/assets/", http.FileServer(http.FS(assetsFS))))

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/" {
            data, err := htmlFiles.ReadFile(filepath.Join("html", "index.html"))
            if err != nil {
                http.Error(w, "404 Not Found", http.StatusNotFound)
                return
            }
            w.Write(data)
            return
        }

        serveDynamicHTMLPage(w, r)
    })

    log.Printf("Listening on http://localhost:%s\n", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}

func serveFile(w http.ResponseWriter, path string) {
    data, err := htmlFiles.ReadFile(path)
    if err != nil {
        data, err = htmlFiles.ReadFile(filepath.Join("html", "404.html"))
        if err != nil {
            http.Error(w, "404 Not Found", http.StatusNotFound)
            return
        }
        w.WriteHeader(http.StatusNotFound)
    }

    w.Write(data)
}

func serveDynamicHTMLPage(w http.ResponseWriter, r *http.Request) {
    path := filepath.Join("html", strings.TrimPrefix(r.URL.Path, "/")+".html")
    serveFile(w, path)
}
