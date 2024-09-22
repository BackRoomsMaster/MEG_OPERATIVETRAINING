const map = JSON.parse(process.argv[2]);

const rooms = [
    "entrance", "hallway", "office", "storage",
    "cafeteria", "library", "basement"
];

console.log("Mappa delle Backrooms:");
console.log("---------------------");

for (let room of rooms) {
    if (map[room]) {
        console.log(`[X] ${room}`);
    } else {
        console.log(`[ ] ${room}`);
    }
}

console.log("---------------------");
console.log("X = Stanza esplorata");
