package main

import (
    "net/http"
    "os"
    "path/filepath"
    "strings"
    "fmt"
    "log"
)

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.Dir("./css"))))
    http.Handle("/js/", http.StripPrefix("/js/", http.FileServer(http.Dir("./js"))))
    http.Handle("/assets/", http.StripPrefix("/assets/", http.FileServer(http.Dir("./assets"))))

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/" {
            http.ServeFile(w, r, filepath.Join("html", "index.html"))
            return
        }

        serveDynamicHTMLPage(w, r)
    })

    http.HandleFunc("/404", func(w http.ResponseWriter, r *http.Request) {
        http.ServeFile(w, r, filepath.Join("html", "404.html"))
    })
    
    log.Println("listening on", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}

func serveDynamicHTMLPage(w http.ResponseWriter, r *http.Request) {
    filePath := filepath.Join("html", strings.TrimPrefix(r.URL.Path, "/")+".html")
    if _, err := os.Stat(filePath); os.IsNotExist(err) {
        http.ServeFile(w, r, filepath.Join("html", "404.html"))
    } else if err != nil {
        fmt.Fprint(w, "500 Internal Server Error")
    } else {
        http.ServeFile(w, r, filePath)
    }
}
