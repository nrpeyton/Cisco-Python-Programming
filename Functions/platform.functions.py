import platform

print(platform.processor()) # Output: Processor Type, e.g., x86 64





print(platform.platform()) # Output: Linux-6.2.0-34-generic-x86_64-with-glibc2.37         OR           Windows-10-10.0.18362-SP0

# Broader platform information (I.E., Linux or Windows) and processor.  It does contain the kernel version, but remember the Linux kernel is developed further
# upstream, so although the version number makes it appear more nuanced its not (see below).




print(platform.version()) # Output: #34-Ubuntu SMP PREEMPT_DYNAMIC Mon Sep  4 13:06:55 UTC 2023         OR           10.0.18362

# The above includes the operating system build date.  Symmetric Multiprocessing (SMP) shows the OS is equipped to handle multiple-CPUs.
# More nuanced and specific to the build details of the kernel, rather than just the kernel version number.  Remember each distribution modifies
# the kernel and/or builds ontop of it, which is a more "upstream" process.  In essence, platform.version() is more nuanced by providing the distribution.
# For Windows however, it is not analogous to the Linux approach at all, because its only handled by Microsoft.
# With Windows its simpler, platform.version() is simply "part of a longer string"






print(platform.python_version_tuple())
