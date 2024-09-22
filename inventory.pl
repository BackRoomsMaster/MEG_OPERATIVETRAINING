#!/usr/bin/perl
use strict;
use warnings;

my @inventory = @ARGV;

if (@inventory) {
    print "Il tuo inventario contiene:\n";
    foreach my $item (@inventory) {
        my $description = get_item_description($item);
        print "- $item: $description\n";
    }
} else {
    print "Il tuo inventario è vuoto.\n";
}

sub get_item_description {
    my ($item) = @_;
    my %descriptions = (
        'flashlight' => 'Una torcia affidabile per illuminare le zone buie.',
        'medkit' => 'Un kit di pronto soccorso per curare le ferite.',
        'snack' => 'Uno spuntino per recuperare un po\' di energia.',
        'map' => 'Una mappa parziale delle Backrooms.',
        'radio' => 'Una radio che emette solo statica.',
        'journal' => 'Un diario con appunti criptici sulle Backrooms.',
        'compass' => 'Una bussola che punta sempre in direzioni casuali.',
    );
    return $descriptions{$item} || 'Nessuna descrizione disponibile.';
}
