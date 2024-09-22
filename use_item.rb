#!/usr/bin/env ruby

item = ARGV[0]

effects = {
  'medkit' => 'Hai recuperato 20 punti salute.',
  'snack' => 'Hai recuperato 20 punti sanità mentale.',
  'flashlight' => 'Hai illuminato la stanza, rivelando un passaggio segreto.',
  'map' => 'Hai studiato la mappa, scoprendo una nuova area.',
  'radio' => 'Hai ascoltato la radio, captando un messaggio misterioso.',
  'journal' => 'Hai letto il diario, ottenendo indizi sulle Backrooms.',
  'compass' => 'La bussola gira impazzita, ma ti dà un senso di direzione.'
}

puts effects[item] || "Questo oggetto non ha effetti particolari."
