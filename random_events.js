const events = [
    "Senti un rumore inquietante in lontananza.",
    "Le luci lampeggiano per un momento.",
    "Noti una strana ombra con la coda dell'occhio.",
    "Un'aria fredda ti passa accanto.",
    "Senti un sussurro incomprensibile.",
    "Il pavimento scricchiola sotto i tuoi piedi.",
    "Un oggetto cade da uno scaffale nelle vicinanze.",
    "Vedi una figura sfocata in lontananza che scompare rapidamente.",
    "Un forte odore di muffa ti assale improvvisamente.",
    "Senti il suono di passi che si avvicinano, ma non vedi nessuno.",
    "PERICOLO: Il soffitto inizia a crollare!",
    "PERICOLO: Un buco si apre improvvisamente nel pavimento!",
    "PERICOLO: Gas tossico inizia a fuoriuscire dalle pareti!"
];

function getRandomEvent() {
    const index = Math.floor(Math.random() * events.length);
    return events[index];
}

console.log(getRandomEvent());
