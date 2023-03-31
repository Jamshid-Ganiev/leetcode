#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, map<char, string>> TABLE_FOR_EVEN = {
        {"q0", { {'a', "q1"}, {'b', "q0"}, {'other', "q0"} }},
        {"q1", { {'a', "q2"}, {'b', "q0"}, {'other', "q0"} }},
        {"q2", { {'a', "q2"}, {'b', "q3"}, {'other', "q0"} }},
        {"q3", { {'a', "q1"}, {'b', "q4"}, {'other', "q0"} }},
        {"q4", { {'a', "q5"}, {'b', "q0"}, {'other', "q0"} }},
        {"q5", { {'a', "P"}, {'b', "q0"}, {'other', "q0"} }}
};

map<string, map<char, string>> TABLE_FOR_ODD = {
        {"q0", { {'a', "q1"}, {'b', "q0"}, {'other', "q0"} }},
        {"q1", { {'a', "q2"}, {'b', "q0"}, {'other', "q0"} }},
        {"q2", { {'a', "q2"}, {'b', "q3"}, {'other', "q0"} }},
        {"q3", { {'a', "q4"}, {'b', "q0"}, {'other', "q0"} }},
        {"q4", { {'a', "q2"}, {'b', "q5"}, {'other', "q0"} }},
        {"q5", { {'a', "P"}, {'b', "q0"}, {'other', "q0"} }}
};

string pattern_matching(map<string, map<char, string>> T, string P, string text) {
    int n = text.length();
    int m = P.length();
    string S = "q0";
    int K = 1;
    
    while (S != "P" && K <= n) {
        char Tk = text[K-1];
        string Sk = T[S][Tk].empty() ? "q0" : T[S][Tk];
        K++;
        if (Sk == "P") {
            int INDEX = K - m - 1;
            return "==>Pattern: '" + P + "'. Index:[" + to_string(INDEX) + ":" + to_string(INDEX + m) + "]";
        }
        S = Sk;
    }
    
    return "No Match Found";
}

int main() {
    int student_id;
    cout << "Enter your Student ID:";
    cin >> student_id;
    
    string Pattern, text_1, text_2;
    map<string, map<char, string>> Table;
    
    if ((student_id % 100) % 2 == 0) {
        Pattern = "aabbaa";
        Table = TABLE_FOR_EVEN;
    }
    else {
        Pattern = "aababa";
        Table = TABLE_FOR_ODD;
    }
    
    text_1 = "abaabcaacbcaccaababaacabba";
    text_2 = "abaabcaacbcaccaabbaacabba";
    
    cout << pattern_matching(Table, Pattern, text_1) << endl;
    cout << pattern_matching(Table, Pattern, text_2) << endl;
    
    return 0;
}
