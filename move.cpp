#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

int main(int argc, char* argv[]) {
    string current_room = argv[1];
    bool random_move = (argc > 2 && string(argv[2]) == "random");
    
    map<string, vector<string>> connections = {
        {"entrance", {"hallway", "office"}},
        {"hallway", {"entrance", "office", "storage", "cafeteria"}},
        {"office", {"hallway", "storage"}},
        {"storage", {"office", "hallway", "basement"}},
        {"cafeteria", {"hallway", "library"}},
        {"library", {"cafeteria", "basement"}},
        {"basement", {"storage", "library"}}
    };

    if (random_move) {
        srand(time(0));
        int random_index = rand() % connections[current_room].size();
        cout << connections[current_room][random_index];
        return 0;
    }

    cout << "Puoi muoverti verso: ";
    for (const auto& room : connections[current_room]) {
        cout << room << " ";
    }
    cout << endl;

    string new_room;
    cin >> new_room;

    if (find(connections[current_room].begin(), connections[current_room].end(), new_room) != connections[current_room].end()) {
        cout << new_room;
    } else {
        cout << current_room;
    }

    return 0;
}
