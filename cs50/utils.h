#ifndef UTILS_H
#define UTILS_H

#include <sys/resource.h>
#include <sys/time.h>

#undef calculate
#undef getrusage

double calculate(const struct rusage *b, const struct rusage *a);

#endif 