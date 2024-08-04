#include "pch.h"
#include "Btree.h"
#include <iostream>
#include <string>
#include <sstream>
#define DLLEXPORT extern "C" __declspec(dllexport)

// int, std::string 타입 B-tree 함수들
DLLEXPORT Btree<int, std::string>* MakeBtree() {
    return new Btree<int, std::string>();
}

DLLEXPORT void Insert(Btree<int, std::string>* tree, int k, const char* v)
{
    tree->insert({ k, std::string(v) });
}

DLLEXPORT const char* Search(Btree<int, std::string>* tree, int k)
{
    try
    {
        return tree->search(k).c_str();
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
        return nullptr; // 오류 발생 시 반환값
    }
}

DLLEXPORT void Delete(Btree<int, std::string>* tree, int k)
{
    tree->remove(k);
}

DLLEXPORT void DestroyBtree(Btree<int, std::string>* tree)
{
    delete tree;
}

DLLEXPORT const char* TraverseBtree(Btree<int, std::string>* tree)
{
    std::stringstream ss;
    tree->traverse(ss);
    std::string result = ss.str();
    size_t size = result.size() + 1;
    char* cstr_result = new char[size];
    strcpy_s(cstr_result, size, result.c_str()); // Use strcpy_s for safer copying
    return cstr_result;
}
