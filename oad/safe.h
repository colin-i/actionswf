
//typedef long long long;//on windows but later

#if defined __has_builtin  //gcc/clang
#  if ! __has_builtin (__builtin_malloc)  //not the same as #ifndef __builtin_malloc
void*malloc(long unsigned int);
#  endif
#  if ! __has_builtin (__builtin_realloc)
void*realloc(void*,long unsigned int);
#  endif
#  if ! __has_builtin (__builtin_strlen)
long unsigned int strlen(const char*);
#  endif
#endif
