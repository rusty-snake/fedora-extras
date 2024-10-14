hardened_malloc
===============

https://github.com/GrapheneOS/hardened_malloc

> This is a security-focused general purpose memory allocator providing the
> malloc API along with various extensions. It provides substantial hardening
> against heapcorruption vulnerabilities. The security-focused design also leads
> to much less metadata overhead and memory waste from fragmentation than a more
> traditional allocator design. It aims to provide decent overall performance
> with a focus on long-term performance and memory usage rather than allocator
> micro-benchmarks. It offers scalability via a configurable number of entirely
> independently arenas, with the internal locking within arenas further divided
> up per size class.

Content
-------

- `libhardened_malloc.so`
- `libhardened_malloc-light.so`
- `libhardened_malloc-pkey.so`
