# On "Embedding Calls" Page 83

Lutz provides an example of calling python code embedded in C. I decided to try
it out out of curiosity and just a chance at writing and running some C. C still
feels to me like some sort of exotic, dangerous, animal, that's hard to tame, so \
if I get the opportunity to pet, I pet it!


## Running

You need GCC and python3-dev. You might already have it installed, but just in
case:

```

$ sudo apt install build-essential python3-dev

```

Then run:

```

gcc -I/usr/include/python3.8 run_py_in_c.c -lpython3.8
./a.out

```

To make life easier, I created a python script that does the above!

```

python3 run_py_in_c.py

```
