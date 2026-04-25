{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7a86e96b-56fd-4e7b-a72b-daa4f695ff56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your salary:  115000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tax Rate: 25.0%\n",
      "Final Tax: 28750.0\n"
     ]
    }
   ],
   "source": [
    "salary = float(input(\"Enter your salary: \")) \n",
    "\n",
    "if salary < 30000:\n",
    "    tax_rate = 0.05\n",
    "elif 30000 <= salary <=70000:\n",
    "    tax_rate=0.15\n",
    "else:\n",
    "    tax_rate = 0.25\n",
    "tax_amount=salary * tax_rate\n",
    "print(f\"Tax Rate: {tax_rate * 100}%\")\n",
    "print(f\"Final Tax: {tax_amount}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d834875-2f99-4174-a93b-7b89b8e59101",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
