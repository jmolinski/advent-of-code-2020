#include <iostream>

int main() {
    int a, b;
    std::string passwd;
    char _, letter;

    int part1 = 0, part2 = 0;
    while(std::cin >> a >> _ >> b >> letter >> _ >> passwd) {
        int appearances = 0;
        for (char c : passwd) {
            if(c == letter) {
                appearances++;
            }
        }
        if (appearances >= a && appearances <= b) {
            part1++;
        }
        if ((passwd[a-1] == letter) != (passwd[b-1] == letter)) {
            part2++;
        }
    }

    std::cout << "Part1: " << part1 << "\n";
    std::cout << "Part2: " << part2 << "\n";
}