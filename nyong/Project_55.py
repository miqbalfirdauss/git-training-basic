{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project 55"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "249\n",
      "0.10434198379516602\n"
     ]
    }
   ],
   "source": [
    "# time module\n",
    "\n",
    "import time\n",
    "\n",
    "\n",
    "\n",
    "# time at the start of program execution\n",
    "\n",
    "start = time.time()\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def is_lychrel(n):\n",
    "\n",
    "    \"\"\"this function will check if the number\n",
    "\n",
    "    is lychrel number or not\"\"\"\n",
    "\n",
    "    # fifty iterations\n",
    "\n",
    "    for i in range(50):\n",
    "\n",
    "        # sum of number and reverse\n",
    "\n",
    "        number = n + int(str(n)[::-1])\n",
    "\n",
    "        # if is palindrome\n",
    "\n",
    "        if str(number) == str(number)[::-1]:\n",
    "\n",
    "            return False\n",
    "\n",
    "        n = number\n",
    "\n",
    "    return True\n",
    "\n",
    "\n",
    "\n",
    "# counter to count\n",
    "\n",
    "counter = 0\n",
    "\n",
    "\n",
    "\n",
    "# looping till ten thousand\n",
    "\n",
    "for i in range(10001):\n",
    "\n",
    "    if is_lychrel(i):\n",
    "\n",
    "        counter += 1\n",
    "\n",
    "\n",
    "\n",
    "# printing the counter\n",
    "\n",
    "print (counter)\n",
    "\n",
    "\n",
    "\n",
    "# time at the end of program execution\n",
    "\n",
    "end = time.time()\n",
    "\n",
    "\n",
    "\n",
    "# total time of execution\n",
    "\n",
    "print (end - start)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
