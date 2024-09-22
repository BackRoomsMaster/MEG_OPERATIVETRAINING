CREATE TABLE player_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    current_room TEXT NOT NULL,
    inventory TEXT,
    health INTEGER,
    sanity INTEGER,
    map TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO player_progress (current_room, inventory, health, sanity, map)
VALUES ('entrance', '["flashlight"]', 100, 100, '{"entrance": true}');

SELECT * FROM player_progress ORDER BY timestamp DESC LIMIT 1;
