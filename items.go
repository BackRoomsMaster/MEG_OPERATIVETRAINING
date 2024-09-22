package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

var items = map[string][]string{
	"entrance": {"flashlight", "map"},
	"hallway":  {"snack", "compass"},
	"office":   {"medkit", "journal"},
	"storage":  {"radio", "flashlight"},
	"cafeteria": {"snack", "medkit"},
	"library":   {"journal", "map"},
	"basement":  {"radio", "compass"},
}

func main() {
	rand.Seed(time.Now().UnixNano())
	room := os.Args[1]

	if roomItems, exists := items[room]; exists && len(roomItems) > 0 {
		if rand.Float32() < 0.5 { // 50% chance to find an item
			randomItem := roomItems[rand.Intn(len(roomItems))]
			fmt.Println(randomItem)
		} else {
			fmt.Println("none")
		}
	} else {
		fmt.Println("none")
	}
}
