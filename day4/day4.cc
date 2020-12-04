#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
using map_ss = unordered_map<string, string>;

void add_parts_to_map(map_ss &map, string line) {
    string pair;
    istringstream ss(line);

    while (ss >> pair) {
        size_t pos = pair.find(':');
        map.insert({pair.substr(0, pos), pair.substr(pos + 1, pair.size() - pos)});
    }
}

int main() {
    vector<map_ss> passports;

    vector<string> needed = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}; // cid

    string line;
    while (!cin.eof()) {
        map_ss passport;
        while (getline(cin, line)) {
            if (!line.size()) {
                break;
            }
            add_parts_to_map(passport, line);
        }
        passports.push_back(passport);
    }

    vector<map_ss> valid_passports;
    for (auto p : passports) {
        bool ok = true;
        for (string needed_key : needed) {
            if (p.find(needed_key) == p.end()) {
                ok = false;
                break;
            }
        }
        if (ok) {
            valid_passports.push_back(p);
        }
    }

    cout << "Part 1 " << valid_passports.size() << "\n";
}
