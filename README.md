```golang
package main

import (
    "fmt"
    "github.com/wusthanhdieu"
)

type Github struct {
    username string
    contacts map[string]string
    alises   []string
    location string
    age      string
    occupation string
    operating_system string
}

func (g *Github) Init() {
    g.username = "thanhdieutv"
    g.contacts = map[string]string{
        "Discord": "thanhdieutv#2278",
        "Facebook": "WusThanhDieu",
    }
    g.alises = []string{"namdevel", "HEUSC"}
          g.location = "localhost, vietnamese"
    g.age = "Undefined"
    g.occupation = "Freelance Developer"
    g.operating_system = "Windows, Arch, Linux, VPS"
}
```
