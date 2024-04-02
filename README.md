```golang
package main

import (
    "wusthanhdieu"
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
    g.alises = []string{"thanhdieudev", "Tdv"}
    g.location = "localhost, vietnamese"
    g.age = "22+"
    g.occupation = "Freelance Developer"
    g.operating_system = "Windows, Arch, Linux, VPS"
}
```

<div align="center">
<img src="https://i.imgur.com/WLt3W7q.gif"
width="800"  height="3">
</div>
