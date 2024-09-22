use std::env;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();
    let room = &args[1];

    let descriptions = HashMap::from([
        ("entrance", "Ti trovi in una stanza con pareti gialle e moquette umida. C'è un'atmosfera inquietante."),
        ("hallway", "Un corridoio infinito si estende davanti a te. Le luci fluorescenti sfarfallano in modo irregolare."),
        ("office", "Una stanza piena di cubicoli vuoti e computer spenti. Fogli sparsi ovunque."),
        ("storage", "Un magazzino buio pieno di scatole impilate. Si sentono rumori strani provenire dagli angoli."),
        ("cafeteria", "Una mensa abbandonata con tavoli rovesciati. C'è un odore nauseabondo nell'aria."),
        ("library", "Scaffali infiniti pieni di libri polverosi. Alcuni sembrano muoversi da soli."),
        ("basement", "Un seminterrato umido e buio. L'acqua gocciola dal soffitto creando pozzanghere sul pavimento."),
    ]);

    println!("{}", descriptions.get(room).unwrap_or(&"Descrizione non trovata."));
}
