#include <iostream>
#include <vector>

int count_trees(const std::vector<std::string> &board, const int kr, const int kc) {
    const int rows = board.size();
    const int cols = board[0].size();

    int r = 0, c = 0;
    int count = 0;
    while (r < rows) {
        if (board[r][c % cols] == '#') {
            count++;
        }
        r += kr;
        c += kc;
    }

    return count;
}

int main() {
    auto board = std::vector<std::string>();
    std::string s;

    while (std::cin >> s) {
        board.push_back(s);
    }

    std::cout << "Part 1: " << count_trees(board, 1, 3) << "\n";

    unsigned long long p2 = count_trees(board, 1, 1) * count_trees(board, 1, 3) *
                            count_trees(board, 1, 5) * count_trees(board, 1, 7) *
                            count_trees(board, 2, 1);
    std::cout << "Part 2: " << p2 << "\n";
}