#include <iostream>
#include <string>
void diro()
{
    std::string word;
    std::cin >> word;
    int length = word.length();
    if (length > 10)
    {
        std::cout << word[0] << (length - 2) << word[length - 1] << std::endl;
    }
    else
    {
        std::cout << word << std::endl;
    }
}
int main()
{
    int k;
    std::cin >> k;
    for (int i = 0; i < k; i++)
    {
        diro();
    }
    return 0;
}