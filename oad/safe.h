
//typedef long long long;//on windows but later

//gcc/clang with __has_builtin    //not the same as #ifndef __builtin_malloc
#if (! defined(__has_builtin)) || (! __has_builtin (__builtin_malloc))
void*malloc(long unsigned int);
#endif
#if (! defined(__has_builtin)) || (! __has_builtin (__builtin_realloc))
void*realloc(void*,long unsigned int);
#endif
#if (! defined(__has_builtin)) || (! __has_builtin (__builtin_strlen))
long unsigned int strlen(const char*);
#endif
