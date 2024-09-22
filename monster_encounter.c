#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

const char* monsters[] = {
    "Hound",
    "Smiler",
    "Skin-Stealer",
    "Clumps",
    "Wretch",
    "none"
};

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <room_name>\n", argv[0]);
        return 1;
    }

    srand(time(NULL));
    const char* room = argv[1];

    // Aumenta la probabilità di incontro in alcune stanze
    float encounter_chance = 0.2; // 20% di base
    if (strcmp(room, "basement") == 0 || strcmp(room, "storage") == 0) {
        encounter_chance = 0.4; // 40% nelle stanze più pericolose
    }

    if ((float)rand() / RAND_MAX < encounter_chance) {
        int monster_index = rand() % (sizeof(monsters) / sizeof(monsters[0]) - 1);
        printf("%s\n", monsters[monster_index]);
    } else {
        printf("none\n");
    }

    return 0;
}
